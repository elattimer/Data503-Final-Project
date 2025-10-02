# transform_course_interests
import pandas as pd
import pytest
import numpy as np
from datetime import datetime
import sys
from pathlib import Path

# Add src folder to path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from transformationScripts.transform_json_course_interest import transform_course_interest
from transformationScripts.transform_json_date_fix import fix_date
from transformationScripts.transform_json_finincial_support_self import transform_financial_support_self

test_json = pd.read_csv("test/test_json_cvs.csv")


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


"""
def test_missing_column():
    # Test DataFrame without the column
    df = pd.DataFrame({
        "other_col": [1, 2, 3]
    })

    result = transform_financial_support_self(df)

    # The missing column should be created with all True
    assert "financial_support_self" in result.columns
    assert all(result["financial_support_self"] == True)
    
    
"""
