from src.transformationScripts.transform_csv_course_behaviours import transform_csv_course_behaviours_course, transform_csv_course_behaviours_behaviour_scores
import pytest
import pandas as pd
import numpy as np

def test_transform_csv_course_behaviours_course_transforms():
    test_df = pd.DataFrame({
    'file_name': ['Engineering_17_2019-02-18.csv'],
    'trainer': ['sherlock']})

    result = transform_csv_course_behaviours_course(test_df)

    assert len(result) == 1
    assert isinstance(result, pd.DataFrame)
    assert result.iloc[0]['subject_name'] == 'Engineering'
    assert result.iloc[0]['trainer_name'] == 'SHERLOCK'
    assert result.iloc[0]['class_number'] == 17
    assert result.iloc[0]['start_date'] == pd.to_datetime('2019-02-18')
    assert list(result.columns) == ['course_id', 'subject_name', 'trainer_name', 'start_date', 'class_number']


def test_transform_csv_course_behaviours_course_drops_duplicates():
    test_df = pd.DataFrame({
    'file_name': ['Engineering_17_2019-02-18.csv', 'Engineering_17_2019-02-18.csv'],
    'trainer': ['sherlock', 'sherlock']})

    result = transform_csv_course_behaviours_course(test_df)

    assert len(result) == 1
    assert result.iloc[0]['course_id'] == 1


def test_transform_csv_course_behaviours_behaviour_scores_transforms():
    test_df = pd.DataFrame({
    'file_name': ['Engineering_17_2019-02-18.csv'],
    'name': ['sherlock'],
    'trainer': ['john'],
    'Analytic_W1': [3],
    'Determined_W1': [4],
    'Imaginative_W1': [5],
    'Independent_W1': [2],
    'Professional_W1': [4],
    'Studious_W1': [5]})

    result = transform_csv_course_behaviours_behaviour_scores(test_df)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 1
    assert result.iloc[0]['start_date'] == pd.to_datetime('2019-02-18')
    assert result.iloc[0]['week'] == 1
    assert result.iloc[0]['name'] == 'SHERLOCK'
    assert result.iloc[0]['analytical'] == 3
    assert result.iloc[0]['determination'] == 4
    assert result.iloc[0]['imaginative'] == 5
    assert result.iloc[0]['independence'] == 2
    assert result.iloc[0]['professionalism'] == 4
    assert result.iloc[0]['studious'] == 5


def test_transform_csv_course_behaviours_behaviour_scores_fills_nulls():
    test_df = pd.DataFrame({
    'file_name': ['Engineering_17_2019-02-18.csv'],
    'name': ['sherlock'],
    'trainer': ['john'],
    'Analytic_W1': [None],
    'Determined_W1': [None],
    'Imaginative_W1': [None],
    'Independent_W1': [None],
    'Professional_W1': [None],
    'Studious_W1': [None]})

    result = transform_csv_course_behaviours_behaviour_scores(test_df)

    assert result.iloc[0]['analytical'] == 0
    assert result.iloc[0]['determination'] == 0
    assert result.iloc[0]['imaginative'] == 0
    assert result.iloc[0]['independence'] == 0
    assert result.iloc[0]['professionalism'] == 0
    assert result.iloc[0]['studious'] == 0

def test_transform_csv_course_behaviours_behaviour_scores_returns_correct_types():
    test_df = pd.DataFrame({
    'file_name': ['Engineering_17_2019-02-18.csv'],
    'name': ['sherlock'],
    'trainer': ['john'],
    'Analytic_W1': [3],
    'Determined_W1': [4],
    'Imaginative_W1': [5],
    'Independent_W1': [2],
    'Professional_W1': [4],
    'Studious_W1': [5]})

    result = transform_csv_course_behaviours_behaviour_scores(test_df)

    assert isinstance(result.iloc[0]['start_date'], pd.Timestamp)
    assert isinstance(result.iloc[0]['week'], np.int64)
    assert isinstance(result.iloc[0]['name'], str)
    assert isinstance(result.iloc[0]['analytical'], np.int64)
    assert isinstance(result.iloc[0]['determination'], np.int64)
    assert isinstance(result.iloc[0]['imaginative'], np.int64)
    assert isinstance(result.iloc[0]['independence'], np.int64)
    assert isinstance(result.iloc[0]['professionalism'], np.int64)
    assert isinstance(result.iloc[0]['studious'], np.int64)