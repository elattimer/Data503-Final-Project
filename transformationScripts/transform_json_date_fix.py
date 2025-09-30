from datetime import datetime
import pandas as pd


def fix_date(data: pd.DataFrame) -> pd.DataFrame:
    def fix_date(val):
        #set data to datetime format d/m/y
        date_data = str(val).split('/')
        cleaned = [x for x in date_data if x and x.strip()]
        date = cleaned[0] +"/"+ cleaned[1] + "/" + cleaned[2]
        dt = datetime.strptime(date, "%d/%m/%Y")

        return dt
    if "date" in data.columns:
        data["date"] = data["date"].apply(fix_date)
    return data


