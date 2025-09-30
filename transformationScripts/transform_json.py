from extract_json import extract_json
from transform_json_finincial_support_self import transform_financial_support_self
from transform_json_lists import *
from transform_json_tech_self_score import get_tech_self_score

def get_strengths_frame(data : pd.dataFrame) -> pd.DataFrame:
    return transform_strengths(data)

def get_weaknesses_frame(data : pd.dataFrame) -> pd.DataFrame:
    return transform_weaknesses(data)

def get_tech_skills_frame(data : pd.dataFrame) -> pd.DataFrame:
    return get_tech_self_score(data)


