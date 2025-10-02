from src.transformationScripts.extract_csv_applicants import extract_csv_apps
import pytest
import pandas as pd
from unittest.mock import MagicMock


@pytest.fixture
def mock_container_client():
    return MagicMock()


def test_extract_csv_apps_returns_empty_df_with_non_applicant_file_name(mock_container_client):
    test_csv = 'name,gender,dob,email\nEsme Trusslove,Female,04/08/1994,etrusslove0@google.es'
    
    mock_container_client.list_blob_names.return_value = ['April2019.csv']

    mock_blob_client = MagicMock()
    mock_blob_client.download_blob.return_value.readall.return_value = test_csv.encode("utf-8")

    mock_container_client.get_blob_client.return_value = mock_blob_client

    result = extract_csv_apps(mock_container_client)

    assert result.empty
    assert isinstance(result, pd.DataFrame)


def test_extract_csv_apps_returns_empty_df_when_given_empty_data(mock_container_client):
    test_csv = ''
    
    mock_container_client.list_blob_names.return_value = ['April2019Applicants.csv']

    mock_blob_client = MagicMock()
    mock_blob_client.download_blob.return_value.readall.return_value = test_csv.encode("utf-8")

    mock_container_client.get_blob_client.return_value = mock_blob_client

    result = extract_csv_apps(mock_container_client)

    assert result.empty
    assert isinstance(result, pd.DataFrame)


def test_extract_csv_apps_returns_single_df(mock_container_client):
    test_csv = 'name,gender,dob,email\nEsme Trusslove,Female,04/08/1994,etrusslove0@google.es'
    
    mock_container_client.list_blob_names.return_value = ['April2019Applicants.csv']

    mock_blob_client = MagicMock()
    mock_blob_client.download_blob.return_value.readall.return_value = test_csv.encode("utf-8")

    mock_container_client.get_blob_client.return_value = mock_blob_client

    result = extract_csv_apps(mock_container_client)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result.iloc[0]['name'] == 'Esme Trusslove'
    assert result.iloc[0]['gender'] == 'Female'
    assert result.iloc[0]['dob'] == '04/08/1994'
    assert result.iloc[0]['email'] == 'etrusslove0@google.es'
    assert list(result.columns) == ['name', 'gender', 'dob', 'email']


def test_extract_csv_apps_returns_combined_df(mock_container_client):
    test_csv1 = 'name,gender,dob,email\nEsme Trusslove,Female,04/08/1994,etrusslove0@google.es'
    test_csv2 = 'name,gender,dob,email\nStillmann Castano,Male,25/07/1992,scastano0@geocities.jp'
    mock_container_client.list_blob_names.return_value = ['April2019Applicants.csv', 'Aug2019Applicants.csv']

    mock_blob_client1 = MagicMock()
    mock_blob_client1.download_blob.return_value.readall.return_value = test_csv1.encode("utf-8")

    mock_blob_client2 = MagicMock()
    mock_blob_client2.download_blob.return_value.readall.return_value = test_csv2.encode("utf-8")

    mock_container_client.get_blob_client.side_effect = [mock_blob_client1, mock_blob_client2]

    result = extract_csv_apps(mock_container_client)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert result.iloc[0]['name'] == 'Esme Trusslove'
    assert result.iloc[1]['name'] == 'Stillmann Castano'
    assert result.iloc[0]['gender'] == 'Female'
    assert result.iloc[1]['gender'] == 'Male'
    assert result.iloc[0]['dob'] == '04/08/1994'
    assert result.iloc[1]['dob'] == '25/07/1992'
    assert result.iloc[0]['email'] == 'etrusslove0@google.es'
    assert result.iloc[1]['email'] == 'scastano0@geocities.jp'
    assert list(result.columns) == ['name', 'gender', 'dob', 'email']