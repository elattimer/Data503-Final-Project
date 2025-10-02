from datetime import datetime
import pandas as pd
from src.transformationScripts.person_id_mapping import (
    set_person_id_for_applicants,
    strips_names,
    make_person_id_mapping_df,
    get_name_frequency_dict,
    set_person_id)

def test_set_person_id():
    df = pd.DataFrame({'name': ['Alice', 'Bob']})
    result = set_person_id_for_applicants(df.copy())

    assert 'person_id' in result.columns
    assert result['person_id'].tolist() == [1, 2]

def test_strips_names():
    assert strips_names("Jo hn") == "JOHN"
    assert strips_names("Mary-Jane!") == "MARYJANE"
    assert strips_names("O'Neil") == "ONEIL"

def test_make_person_id_mapping_df():
    df = pd.DataFrame({
        'name': ['John Doe', 'Jane Smith'],
        'invited_date': ['01/09/2025', None],
        'person_id': [1, 2]
    })

    result = make_person_id_mapping_df(df.copy())

    assert list(result.columns) == ['name', 'date', 'id']
    assert result['name'].tolist() == ['JOHNDOE', 'JANESMITH']
    assert result.loc[1, 'date'] == datetime(2030, 1, 1)



    assert list(result.columns) == ['name', 'date', 'id']
    assert result['name'].tolist() == ['JOHNDOE', 'JANESMITH']
    assert result.loc[1, 'date'] == datetime(2030, 1, 1)

def test_get_name_frequency_dict():
    names = ['ALICE', 'BOB', 'ALICE']
    freq = get_name_frequency_dict(names)

    assert freq == {'ALICE': 2, 'BOB': 1}


def test_set_person_id_unique_name():
    data = pd.DataFrame({'name': ['Alice'], 'date': [pd.Timestamp('2025-09-01')]})
    mapping_df = pd.DataFrame({'name': ['ALICE'], 'date': [pd.Timestamp('2025-09-01')], 'id': [101]})
    freq = {'ALICE': 1}

    result = set_person_id(data.copy(), mapping_df, freq)
    assert result['id'].tolist() == [101]


def test_set_person_id_duplicate_name():
    data = pd.DataFrame({'name': ['John'], 'date': [pd.Timestamp('2025-09-01')]})
    mapping_df = pd.DataFrame({
        'name': ['JOHN', 'JOHN'],
        'date': [pd.Timestamp('2025-09-01'), pd.Timestamp('2025-10-01')],
        'id': [201, 202]
    })
    freq = {'JOHN': 2}

    result = set_person_id(data.copy(), mapping_df, freq)
    assert result['id'].tolist() == [201]