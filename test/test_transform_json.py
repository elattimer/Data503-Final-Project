# transform_course_interests
import pandas as pd
import pytest

from src.transformationScripts.transform_json_course_interest import transform_course_interest
import pandas as pd
from datetime import datetime
from src.transformationScripts.transform_json_date_fix import fix_date
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
