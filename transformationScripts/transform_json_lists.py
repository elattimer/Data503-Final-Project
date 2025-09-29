from extract_json import extract_json
import pandas as pd
from datetime import datetime
import json

def transform_strengths(data: pd.DataFrame) -> pd.DataFrame:

    df_all = pd.DataFrame()
    first = True
    for index, row in data.iterrows():

        #set data to datetime format d/m/y
        date_data = str(row["date"]).split('/')
        cleaned = [x for x in date_data if x and x.strip()]
        date = cleaned[0] +"/"+ cleaned[1] + "/" + cleaned[2]
        dt = datetime.strptime(date, "%d/%m/%Y")

        #loop through strengths of each person
        for j in row["strengths"]:
            new_data = {
                "name": [str(row["name"]).upper()],
                "strength": [j],
                "date" : [dt.date()],
            }
            new_df = pd.DataFrame(new_data)
            #check if already exists
            if first == False:
                # Extract the single row as a Series
                row_series = new_df.iloc[0]

                # Compare to the larger DataFrame
                mask = (df_all[list(row_series.index)] == row_series).all(axis=1)
                if mask.any():
                    print("Row exists in the DataFrame: " + new_df.to_string())
                else:
                    df_all = pd.concat([df_all,new_df], ignore_index=True)
            else:
                first = False
                df_all = pd.concat([df_all,new_df], ignore_index=True)


    return df_all


def transform_weaknesses(data: pd.DataFrame) -> pd.DataFrame:

    df_all = pd.DataFrame()
    first = True
    for index, row in data.iterrows():
        
        #set data to datetime format d/m/y
        date_data = str(row["date"]).split('/')
        cleaned = [x for x in date_data if x and x.strip()]
        date = cleaned[0] +"/"+ cleaned[1] + "/" + cleaned[2]
        dt = datetime.strptime(date, "%d/%m/%Y")

        #loop through strengths of each person
        for j in row["weaknesses"]:
            new_data = {
                "name": [str(row["name"]).upper()],
                "weakness": [j],
                "date" : [dt.date()],
            }
            new_df = pd.DataFrame(new_data)
            #check if already exists
            if first == False:
                # Extract the single row as a Series
                row_series = new_df.iloc[0]

                # Compare to the larger DataFrame
                mask = (df_all[list(row_series.index)] == row_series).all(axis=1)
                if mask.any():
                    print("Row exists in the DataFrame: " + new_df.to_string())
                else:
                    df_all = pd.concat([df_all,new_df], ignore_index=True)
            else:
                first = False
                df_all = pd.concat([df_all,new_df], ignore_index=True)


    return df_all