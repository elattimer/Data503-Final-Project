import pandas as pd
import string
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from pandas._libs.tslibs.parsing import DateParseError

def transform_applicants(data):
    data = data.drop_duplicates(keep = 'first')
    data['name'] = data['name'].str.upper()
    data['name'] = data['name'].str.replace('[{}]'.format(string.punctuation), '', regex = True)

    data['gender'] = data['gender'].fillna('Undisclosed')
    data['gender'] = data['gender'].str.title()

    data['dob'] = data['dob'].fillna(pd.Timestamp('1900-01-01'))
    for n in range(len(data['dob'])):
        try:
            data.loc[n,'dob'] = pd.to_datetime(data.loc[n,'dob'], format = 'mixed', dayfirst= True)
        except DateParseError: 
            data.loc[n, 'dob'] = pd.Timestamp('1900-01-01')


    data['email'] = data['email'].str.lower()
    data['email'] = data['email'].fillna('example@example.com')

    data['city'] = data['city'].str.title()
    data['city'] = data['city'].fillna('Unknown')

    data['address'] = data['address'].fillna('Unknown')

  
    data['postcode'] = data['postcode'].str.upper()
    data['postcode'] = data['postcode'].fillna('Unknown')

    if 'phone_number' in data.columns:
        data = data.drop(columns='phone_number')

    data['uni'] = data['uni'].str.title()
    def fix_uni_degree(row):
        if pd.isna(row['uni']) and pd.isna(row['degree']):
            row['uni'] = 'Did not attend'
            row['degree'] = 'Did not attend'
        return row
    data = data.apply(fix_uni_degree, axis = 1)

    data['degree'] = data['degree'].str.replace('1st', '1:1')
    data['degree'] = data['degree'].str.replace('3rd', '3:1')

    data["invited_date"] = data['invited_date'].astype(str) + " " + data["month"]
    for n in range(len(data['invited_date'])):
        try:
            data.loc[n, 'invited_date'] = pd.to_datetime(data.loc[n,'invited_date'], format = 'mixed', dayfirst= True)
        except DateParseError: 
            data.loc[n, 'invited_date'] = pd.Timestamp('1900-01-01')
    
    if 'month' in data.columns:
        data = data.drop(columns='month')
    
    data['invited_by'] = data['invited_by'].fillna('Not Invited')
    data['invited_by'] = data['invited_by'].str.title()
    data['invited_by'] = data['invited_by'].str.replace('Bruno Belbrook','Bruno Bellbrook')
    data['invited_by'] = data['invited_by'].str.replace('Fifi Etton', 'Fifi Eton')

    return data

# clean_data = transform(data)
# print(clean_data)

# print(clean_data.isna().sum())



