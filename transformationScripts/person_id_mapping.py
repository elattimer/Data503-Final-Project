from src.extract import extract
import pandas as pd
import string
from datetime import datetime

data = extract()
applicants_df = data['applicants_csv']



def strips_names(name: str)->str:
    stripped_name = name.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").upper()
    return stripped_name


#Create df with int date, name and created id
df = applicants_df[['name','invited_date']].rename(columns={'invited_date':'date'})

df['date']=pd.to_datetime(df['date'],dayfirst=True)
df['date']=df['date'].fillna(datetime(2030,1,1))
df['name']=df['name'].apply(strips_names)

# Creates a unique id using index
df.index += 1
df["id"] = df.index



def get_name_frequency_dict(names: list) -> dict[str, int]:
    dict_names: dict[str, int] = {}

    for name in names:
        if name in dict_names:
            dict_names[name] += 1
        else:
            dict_names[name] = 1

    return dict_names

names_freq = get_name_frequency_dict(df['name'].to_list())

#Choose person id based on name and course start date
def get_person_id(name, date,course = False):
    id = "NOIDSET"
    name = strips_names(name)

    check = names_freq[name]
    if check == 1:
        id = df.loc[df['name']==name]['id']
        return id

    if check > 1:
        if not course:
            print(name)
            id = df.loc[(df['name'] == name) & (df['date']==date)]['id']

            return id

        else:
            options = df.loc[df['name'] == name,df['date']==date]
            options['datediff']= (date - options['date']).days
            options = options.loc[options['datediff']>0]
            options.sort_values(by='datediff', ascending=True, inplace=True)
            id = options.index[0]
            return id

    return id
