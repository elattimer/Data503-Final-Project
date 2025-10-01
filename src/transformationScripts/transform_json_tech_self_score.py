import pandas as pd
from datetime import datetime
from transform_json_date_fix import fix_date

def get_tech_self_score(data: pd.DataFrame) -> pd.DataFrame:
    df_all = pd.DataFrame()
    first = True

    data = fix_date(data)

    for index, row in data.iterrows():

        #loop through skills of each person
        d = row["tech_self_score"]
        try:
            for key, value in d.items():
                new_data = {
                    "name": [str(row["name"]).upper()],
                    "tech_name": [key],
                    "date" : [row["date"]],
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
                        #print(str(index) + " Row exists in the DataFrame: " + new_df.to_string())
                        continue
                    else:
                        df_all = pd.concat([df_all,new_df], ignore_index=True)
                else:
                    first = False
                    df_all = pd.concat([df_all,new_df], ignore_index=True)
        except:
            #print(row["name"] + ": has no tech scores")
            continue

    return df_all