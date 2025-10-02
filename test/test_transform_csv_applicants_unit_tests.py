from transformationScripts.transform_csv_applicants import transform_applicants as transform
import pandas as pd

def dummy_sample():
    return pd.DataFrame({
            'name': ['Alice!', 'b;ob dylan'],
            'gender': ['male', None],
            'dob': ['05/07/1993', None],
            'email': ['ALICE@EMAIL.COM', None],
            'city': ['london', None],
            'address': ['123 Baker St', None],
            'postcode': ['ab12cd', None],
            'phone_number': ['12345', '67890'],
            'uni': [None, 'university of oxford'],
            'degree': [None, '1st'],
            'invited_date': ['12', None],
            'month': ['March 2020', 'April 2021'],
            'invited_by': ['bruno belbrook', None]
        })

def test_name():
    df = transform(dummy_sample())
    assert df.loc[0, 'name'] == 'ALICE'
    assert df.loc[1, 'name'] == 'BOB DYLAN'

def test_gender():
    df = transform(dummy_sample())
    assert df.loc[0, 'gender'] == 'Male'
    assert df.loc[1, 'gender'] == 'Undisclosed'

def test_dob():
    df = transform(dummy_sample())
    assert df.loc[0, 'dob'] == '1993-07-05 00:00:00'
    assert df.loc[1, 'dob'] == '1900-01-01 00:00:00'

def test_email():
    df = transform(dummy_sample())
    assert df.loc[0, 'email'] == 'alice@email.com'
    assert df.loc[1, 'email'] == 'example@example.com'

def test_city():
    df = transform(dummy_sample())
    assert df.loc[0, 'city'] == 'London'
    assert df.loc[1, 'city'] == 'Unknown'

def test_address():
    df = transform(dummy_sample())
    assert df.loc[0, 'address'] == '123 Baker St'
    assert df.loc[1, 'address'] == 'Unknown'

def test_postcode():
    df = transform(dummy_sample())
    assert df.loc[0, 'postcode'] == 'AB12CD'
    assert df.loc[1, 'postcode'] == 'Unknown'

def test_phone_number():
    df = transform(dummy_sample())
    assert 'phone_number' not in df.columns

def test_uni():
    df = transform(dummy_sample())
    assert df.loc[0, 'uni'] == 'Did not attend'
    assert df.loc[0, 'degree'] == 'Did not attend'
    assert df.loc[1, 'uni'] == 'University Of Oxford'

def test_degree():
    df = transform(dummy_sample())
    assert df.loc[1, 'degree'] == '1:1'

def test_invited_date():
    df = transform(dummy_sample())
    assert df.loc[0, 'invited_date'] == '2020-03-12 00:00:00'
    assert df.loc[1, 'invited_date'] == '1900-01-01 00:00:00'

def test_month():
    df = transform(dummy_sample())
    assert 'month' not in df.columns

def test_invited_by():
    df = transform(dummy_sample())
    assert df.loc[0,'invited_by'] == 'Bruno Bellbrook'
    assert df.loc[1,'invited_by'] == 'Not invited'
