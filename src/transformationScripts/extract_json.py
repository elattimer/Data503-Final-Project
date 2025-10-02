import pandas as pd
import json
from tqdm import tqdm

def extract_json(container_client) -> pd.DataFrame:

    dict_df = []
    for blob in tqdm(container_client.list_blobs(), desc="Extracting JSONs"):
        #checks for only json files
        if blob.name.endswith(".json"):
            blob_client = container_client.get_blob_client(blob)
            data = blob_client.download_blob().readall().decode("utf-8-sig")
            parsed = json.loads(data)
            try:
                df = pd.DataFrame([{
                    "name": parsed["name"],
                    "date": parsed["date"],
                    "tech_self_score": parsed["tech_self_score"],
                    "strengths": parsed["strengths"],
                    "weaknesses": parsed["weaknesses"],
                    "self_development": parsed["self_development"],
                    "geo_flex": parsed["geo_flex"],
                    "financial_support_self": parsed["financial_support_self"],
                    "result": parsed["result"],
                    "course_interest": parsed["course_interest"]
                }])
            except:
                df = pd.DataFrame([{
                    "name": parsed["name"],
                    "date": parsed["date"],
                    "tech_self_score": [],
                    "strengths": parsed["strengths"],
                    "weaknesses": parsed["weaknesses"],
                    "self_development": parsed["self_development"],
                    "geo_flex": parsed["geo_flex"],
                    "financial_support_self": parsed["financial_support_self"],
                    "result": parsed["result"],
                    "course_interest": parsed["course_interest"]
                }])
            dict_df.append(df)

    # Safe concatenation
    if dict_df:
        combined_df = pd.concat(dict_df, ignore_index=True, sort=False)
    else:
        combined_df = pd.DataFrame()  # returns empty DF if no JSONs this was added after failed testing 

    return combined_df