from src.transformationScripts.extract_csv_course_behaviours import extract_csv_course_behaviours, create_combined_course_behaviours
import pytest
import pandas as pd
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_container_client():
    return MagicMock()


def test_no_blobs_return_empty_df(mock_container_client):
    mock_container_client.list_blobs.return_value = []

    result = extract_csv_course_behaviours(mock_container_client, "missing")

    assert isinstance(result, pd.DataFrame)
    assert result.empty


def test_single_blob_returns_correct_data(mock_container_client):
    sample_csv = 'name,trainer,Analytic_W1\nJohn,Frank,5'

    mock_blob = MagicMock()
    mock_blob.name = 'Engineering_17_2019-02-18.csv'

    mock_blob_client = MagicMock()
    mock_blob_client.download_blob.return_value.readall.return_value = sample_csv.encode('utf-8')

    mock_container_client.list_blobs.return_value = [mock_blob]
    mock_container_client.get_blob_client.return_value = mock_blob_client

    result = extract_csv_course_behaviours(mock_container_client, 'Engineering')

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result.iloc[0]['name'] == 'John'
    assert result.iloc[0]['trainer'] == 'Frank'
    assert result.iloc[0]['Analytic_W1'] == 5
    assert result.iloc[0]['file_name'] == 'Engineering_17_2019-02-18.csv'


def test_two_blobs_returns_correct_data(mock_container_client):
    sample_csv1 = 'name,trainer,Analytic_W1\nJohn,Frank,5'
    sample_csv2 = 'name,trainer,Analytic_W1\nDarla,Carly,8'

    mock_blob1 = MagicMock()
    mock_blob1.name = 'Engineering_17_2019-02-18.csv'

    mock_blob2 = MagicMock()
    mock_blob2.name = 'Engineering_20_2019-05-06.csv'

    mock_blob_client1 = MagicMock()
    mock_blob_client1.download_blob.return_value.readall.return_value = sample_csv1.encode('utf-8')

    mock_blob_client2 = MagicMock()
    mock_blob_client2.download_blob.return_value.readall.return_value = sample_csv2.encode('utf-8')

    mock_container_client.list_blobs.return_value = [mock_blob1, mock_blob2]
    mock_container_client.get_blob_client.side_effect = [mock_blob_client1, mock_blob_client2]

    result = extract_csv_course_behaviours(mock_container_client, 'Engineering')

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert result.iloc[0]['name'] == 'John'
    assert result.iloc[0]['trainer'] == 'Frank'
    assert result.iloc[0]['Analytic_W1'] == 5
    assert result.iloc[0]['file_name'] == 'Engineering_17_2019-02-18.csv'
    assert result.iloc[1]['name'] == 'Darla'
    assert result.iloc[1]['trainer'] == 'Carly'
    assert result.iloc[1]['Analytic_W1'] == 8
    assert result.iloc[1]['file_name'] == 'Engineering_20_2019-05-06.csv'


def test_create_combined_course_behaviours_combines_data():
    data_df = pd.DataFrame({'name': ['John'], 'trainer': ['Frank'], 'Analytic_W1': [5]})
    engineering_df = pd.DataFrame({'name': ['Darla'], 'trainer': ['Carly'], 'Analytic_W1': [8]})
    business_df = pd.DataFrame({'name': ['Gary'], 'trainer': ['Sandra'], 'Analytic_W1': [6]})

    with patch('src.transformationScripts.extract_csv_course_behaviours.extract_csv_course_behaviours', side_effect=[data_df, engineering_df, business_df]) as mock_extract:
        result = create_combined_course_behaviours(mock_container_client)

        mock_extract.assert_any_call(mock_container_client, 'data')
        mock_extract.assert_any_call(mock_container_client, 'engineering')
        mock_extract.assert_any_call(mock_container_client, 'business')
        assert mock_extract.call_count == 3

        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3
        assert list(result['name']) == ['John', 'Darla', 'Gary']