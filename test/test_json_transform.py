# transform_course_interests
import pandas as pd
import pytest
import numpy as np
from datetime import datetime
import sys
from pathlib import Path
import ast

# Add src folder to path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from transformationScripts.transform_json_course_interest import transform_course_interest
from transformationScripts.transform_json_date_fix import fix_date
from transformationScripts.transform_json_finincial_support_self import transform_financial_support_self
from transformationScripts.transform_json_geo_flex import transform_geo_flex
from transformationScripts.transform_json_lists import transform_strengths
from transformationScripts.transform_json_lists import transform_weaknesses
from transformationScripts.transform_json_result import transform_result
from transformationScripts.transform_json_self_development import transform_self_development
from transformationScripts.transform_json_tech_self_score import get_tech_self_score

test_json = pd.read_csv("test/test_json_cvs.csv")
# Convert column
test_json['strengths'] = test_json['strengths'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])
test_json['weaknesses'] = test_json['weaknesses'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else [])


def test_transform_course_interest():
    input = test_json
    expected_course_interests = ["No interest",
                                 "Data",
                                 "Business",
                                 "Data",
                                 "Engineering",
                                 "Business",
                                 "Business",
                                 "Business",
                                 "Data",
                                 "No interest",
                                 "Business"]
    output = transform_course_interest(input)["course_interest"].to_list()

    assert expected_course_interests == output


def test_fix_date():
    # Create a test DataFrame with messy dates
    df = pd.DataFrame({
        "date": [
            "22/08/2019",      # normal
            " 01 /08/2019",    # leading space
            "07/08 /2019 ",    # trailing space
            "  14 / 09 / 2020 " # spaces everywhere
        ]
    })

    # Apply the function
    result = fix_date(df)

    # Check that the 'date' column is now datetime
    assert all(isinstance(x, datetime) for x in result["date"])

    # Check that the dates are correctly parsed
    expected_dates = [
        datetime(2019, 8, 22),
        datetime(2019, 8, 1),
        datetime(2019, 8, 7),
        datetime(2020, 9, 14)
    ]
    assert result["date"].tolist() == expected_dates


def test_transform_financial_support_self():
    # Test DataFrame with mixed values
    df = pd.DataFrame({
        "financial_support_self": ["Yes", "no", "TRUE", "false", 1, 0, True, False, np.nan, "  yes  ", "0"]
    })

    result = transform_financial_support_self(df)

    expected = [True, False, True, False, True, False, True, False, False, True, False]

    assert result["financial_support_self"].tolist() == expected


def test_missing_column():
    # Test DataFrame without the column
    df = pd.DataFrame({
        "other_col": [1, 2, 3]
    })

    result = transform_financial_support_self(df)

    # The missing column should be created with all True
    assert "financial_support_self" in result.columns
    assert all(result["financial_support_self"] == True)
    
    
def test_transform_geo_flex_with_various_inputs():
    data = {
        "geo_flex": [
            "Yes", "no", "TRUE", "false", "1", "0", 
            True, False, None, 123, "" 
        ]
    }
    df = pd.DataFrame(data)

    result = transform_geo_flex(df)

    expected = [
        True,   # "Yes"
        False,  # "no"
        True,   # "TRUE"
        False,  # "false"
        True,   # "1"
        False,  # "0"
        True,   # True
        False,  # False
        False,  # None -> False
        True,   # 123 -> bool(123) = True
        False,  # "" -> not in yes/no, fallback bool("") = False
    ]

    assert result["geo_flex"].tolist() == expected

def test_transform_geo_flex_when_column_missing():
    df = pd.DataFrame({"other_column": [1, 2, 3]})
    result = transform_geo_flex(df)

    # Should add the column and fill with False
    assert "geo_flex" in result.columns
    assert result["geo_flex"].tolist() == [False, False, False]


def test_transform_strengths_creates_correct_rows():
    result = transform_strengths(test_json)
    
    # All names uppercased
    assert all(name.isupper() for name in result["name"])
    
    #Expected
    expected_strengths = pd.DataFrame({
    "name": [
        "STILLMANN CASTANO",
        "HILARY WILLMORE", "HILARY WILLMORE", "HILARY WILLMORE",
        "EFREM WHIPPLE", "EFREM WHIPPLE", "EFREM WHIPPLE",
        "SYDEL FENNE",
        "MICHEL LEBARREE",
        "COOPER INGRAHAM", "COOPER INGRAHAM",
        "BIRD LE COUNT",
        "ORLY LORENS", "ORLY LORENS", "ORLY LORENS",
        "HANNAH MESSUM", "HANNAH MESSUM",
        "GAVIN LAMBREGTS", "GAVIN LAMBREGTS", "GAVIN LAMBREGTS",
        "LETTA HALSTON", "LETTA HALSTON"
    ],
    "strength": [
        "Charisma",
        "Patient", "Curious", "Problem Solving",
        "Courteous", "Independent", "Patient",
        "Passionate",
        "Versatile",
        "Versatile", "Rational",
        "Collaboration",
        "Ambitious", "Independent", "Passionate",
        "Reliable", "Passionate",
        "Altruism", "Empathy", "Problem Solving",
        "Listening", "Passionate"
    ],
    "date": pd.to_datetime([
        "2019-08-22",
        "2019-08-01", "2019-08-01", "2019-08-01",
        "2019-08-22", "2019-08-22", "2019-08-22",
        "2019-08-28",
        "2019-08-07",
        "2019-08-14", "2019-08-14",
        "2019-08-22",
        "2019-08-01", "2019-08-01", "2019-08-01",
        "2019-08-29", "2019-08-29",
        "2019-08-21", "2019-08-21", "2019-08-21",
        "2019-08-08", "2019-08-08"
    ])
})

    
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_strengths)

def test_transform_weaknesses_creates_correct_rows():
    result = transform_weaknesses(test_json)
    
    # All names uppercased
    assert all(name.isupper() for name in result["name"])
    
    #Expected
    expected_weaknesses = pd.DataFrame({
        "name": [
            "HILARY WILLMORE", "HILARY WILLMORE", "HILARY WILLMORE",
            "EFREM WHIPPLE", "EFREM WHIPPLE", "EFREM WHIPPLE",
            "SYDEL FENNE", "SYDEL FENNE",
            "MICHEL LEBARREE", "MICHEL LEBARREE", "MICHEL LEBARREE",
            "COOPER INGRAHAM",
            "BIRD LE COUNT", "BIRD LE COUNT", "BIRD LE COUNT",
            "ORLY LORENS", "ORLY LORENS",
            "HANNAH MESSUM",
            "GAVIN LAMBREGTS", "GAVIN LAMBREGTS",
            "LETTA HALSTON", "LETTA HALSTON", "LETTA HALSTON"
        ],
        "weakness": [
            "Overbearing", "Chatty", "Indifferent",
            "Introverted", "Impulsive", "Anxious",
            "Perfectionist", "Sensitive",
            "Controlling", "Perfectionist", "Chatty",
            "Immature",
            "Impatient", "Conventional", "Undisciplined",
            "Conventional", "Passive",
            "Intolerant",
            "Chaotic", "Selfish",
            "Perfectionist", "Immature", "Passive"
        ],
        "date": pd.to_datetime([
            "2019-08-01", "2019-08-01", "2019-08-01",
            "2019-08-22", "2019-08-22", "2019-08-22",
            "2019-08-28", "2019-08-28",
            "2019-08-07", "2019-08-07", "2019-08-07",
            "2019-08-14",
            "2019-08-22", "2019-08-22", "2019-08-22",
            "2019-08-01", "2019-08-01",
            "2019-08-29",
            "2019-08-21", "2019-08-21",
            "2019-08-08", "2019-08-08", "2019-08-08"
        ])
    })

    
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_weaknesses)


def test_transform_results():
    result = transform_result(test_json)['result']
    expected = pd.DataFrame({'result':[True,
                  False,
                  True,
                  True,
                  True,
                  False,
                  False,
                  False,
                  False,
                  True,
                  False]})['result']


    pd.testing.assert_series_equal(result, expected)

def test_transform_self_development():
    result = transform_self_development(test_json)['self_development']
    expected = pd.Series(
        [True, False, True, True, True, False, False, False, False, True, False],
        name='self_development',
        dtype=bool
    )

    pd.testing.assert_series_equal(result, expected)

def test_get_tech_self_score():
    # Sample input data
    test_data = pd.DataFrame({
        "name": ["Alice Smith", "Bob Jones", "Charlie King"],
        "date": ["01/01/2020", "02/01/2020", "03/01/2020"],
        "tech_self_score": [
            {"Python": 5, "Java": 3},
            {"C++": 4},
            {}  # No tech scores for Charlie
        ]
    })

    # Convert dates to datetime
    test_data["date"] = pd.to_datetime(test_data["date"], format="%d/%m/%Y")

    # Call the function
    result = get_tech_self_score(test_data)

    # Expected output
    expected = pd.DataFrame({
        "name": ["ALICE SMITH", "ALICE SMITH", "BOB JONES"],
        "tech_name": ["Python", "Java", "C++"],
        "date": pd.to_datetime(["2020-01-01", "2020-01-01", "2020-01-02"]),
        "score": [5, 3, 4]
    })

    # Ensure all columns exist and are in same order
    result = result[expected.columns]

    # Test equality
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))