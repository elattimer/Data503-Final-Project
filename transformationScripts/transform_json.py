from extract_json import extract_json
from transform_finincial_support_self import transform_financial_support_self
from transform_json_lists import *


data = extract_json()

def get_strengths_frame():
    return transform_strengths(data)

def get_weaknesses_frame():
    return transform_weaknesses(data)