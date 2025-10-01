import pandas as pd
from transform_json import fix_date, get_json_sparta_day_results

# --- Can't import the strips_names func from person_id_mapping - getting a ModuleNotFoundError from inside the person_id_mapping file - JT ---
# from person_id_mapping import strips_names
import string


def strips_names(name: str) -> str:
    stripped_name = (
        name.translate(str.maketrans("", "", string.punctuation))
        .replace(" ", "")
        .upper()
    )
    return stripped_name


# --- #


# Takes two dataframes and maps dates from 'df_map' dataframe onto 'df' dataframe, returns a new dataframe with the changes applied
def align_incorrect_dates(df: pd.DataFrame, df_map: pd.DataFrame) -> pd.DataFrame:
    """
    Written to solve an issue with the JSON DataFrame post-extraction - June dates were incorrectly entered as July.
    
    To fix this problem:
        Params
            df=<json DataFrame>
            df_map=<txt DataFrame>

    Returns new DataFrame with the correct dates
    """
    df_result = df.copy()
    df_map_dates = df_map.copy()[["name", "date"]].drop_duplicates(subset=["name"])

    df_result["stripped_name"] = df_result["name"].apply(strips_names)
    df_map_dates["stripped_name"] = df_map_dates["name"].apply(strips_names)

    return (
        df_result.merge(df_map_dates, on=["stripped_name"], how="left")
        .drop(["date_x", "name_y", "stripped_name"], axis=1)
        .rename(columns={"name_x": "name", "date_y": "date"})
    )