from extract_json import extract_json
import pandas as pd
from datetime import datetime
import json

def get_tech_self_score(data: pd.DataFrame) -> pd.DataFrame:
    df_all = pd.DataFrame()
    first = True
    for index, row in data.iterrows():

        #set data to datetime format d/m/y
        date_data = str(row["date"]).split('/')
        cleaned = [x for x in date_data if x and x.strip()]
        date = cleaned[0] +"/"+ cleaned[1] + "/" + cleaned[2]
        dt = datetime.strptime(date, "%d/%m/%Y")

        #loop through skills of each person
        d = row["tech_self_score"]
        try:
            for key, value in d.items():
                new_data = {
                    "name": [str(row["name"]).upper()],
                    "tech_name": [key],
                    "date" : [dt.date()],
                    "score" : [value],
                }
                new_df = pd.DataFrame(new_data)
                #check if already exists
                if first == False:
                    # Extract the single row as a Series
                    row_series = new_df.iloc[0]

                    # Compare to the larger DataFrame
                    mask = (df_all[list(row_series.index)] == row_series).all(axis=1)
                    if mask.any():
                        print(str(index) + " Row exists in the DataFrame: " + new_df.to_string())
                    else:
                        df_all = pd.concat([df_all,new_df], ignore_index=True)
                else:
                    first = False
                    df_all = pd.concat([df_all,new_df], ignore_index=True)
        except:
            print(row["name"] + ": has no tech scores")

    return df_all


# with open("13482.json", "r", encoding="utf-8-sig") as f:
#     record = json.load(f)  # json.load for a single object

# # Wrap in a list to make a DataFrame
# df = pd.DataFrame([record])
df = extract_json()
print(get_tech_self_score(df))