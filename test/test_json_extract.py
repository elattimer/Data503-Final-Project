import pytest
import pandas as pd
from unittest.mock import MagicMock

from src.transformationScripts.extract_json import extract_json


class FakeBlob:
    def __init__(self, name):
        self.name = name

def make_blob_client(json_content: str):
    blob_client = MagicMock()
    blob_client.download_blob.return_value.readall.return_value = json_content.encode("utf-8-sig")
    return blob_client

def test_basic_json_extraction():
    container_client = MagicMock()
    blob = FakeBlob("test.json")
    container_client.list_blobs.return_value = [blob]
    container_client.get_blob_client.return_value = make_blob_client(
        '{"name": "Alice", "date": "2025-10-01", "tech_self_score": [5], "strengths": "A", "weaknesses": "B", "self_development": "C", "geo_flex": "Yes", "financial_support_self": "No", "result": "Pass", "course_interest": "Data"}'
    )

    df = extract_json(container_client)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 1
    assert df.iloc[0]["name"] == "Alice"

def test_missing_tech_self_score():
    container_client = MagicMock()
    blob = FakeBlob("test.json")
    container_client.list_blobs.return_value = [blob]
    container_client.get_blob_client.return_value = make_blob_client(
        '{"name": "Bob", "date": "2025-10-01", "strengths": "A", "weaknesses": "B", "self_development": "C", "geo_flex": "Yes", "financial_support_self": "No", "result": "Pass", "course_interest": "Data"}'
    )

    df = extract_json(container_client)
    assert df.iloc[0]["tech_self_score"] == []

def test_non_json_files_are_ignored():
    container_client = MagicMock()
    blob1 = FakeBlob("file.txt")
    blob2 = FakeBlob("data.csv")
    container_client.list_blobs.return_value = [blob1, blob2]

    df = extract_json(container_client)
    assert df.empty  # No JSON means empty DataFrame

def test_multiple_json_files_combined():
    container_client = MagicMock()
    blob1 = FakeBlob("a.json")
    blob2 = FakeBlob("b.json")
    container_client.list_blobs.return_value = [blob1, blob2]

    json_1 = '{"name": "A", "date": "2025-10-01", "tech_self_score": [1], "strengths": "X", "weaknesses": "Y", "self_development": "Z", "geo_flex": "Yes", "financial_support_self": "No", "result": "Pass", "course_interest": "ML"}'
    json_2 = '{"name": "B", "date": "2025-10-02", "tech_self_score": [2], "strengths": "M", "weaknesses": "N", "self_development": "O", "geo_flex": "No", "financial_support_self": "Yes", "result": "Fail", "course_interest": "AI"}'

    container_client.get_blob_client.side_effect = [make_blob_client(json_1), make_blob_client(json_2)]

    df = extract_json(container_client)
    assert df.shape[0] == 2
    assert set(df["name"]) == {"A", "B"}

