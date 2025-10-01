#from extract_csv_applicants import extract
import pandas as pd
import string

# data = extract()
#print(data.columns)

def transform_applicants(data):
    data = data.drop_duplicates(keep = 'first')
    data['name'] = data['name'].str.upper()
    data['name'] = data['name'].str.replace(f'{{string.punctuation}}', '', regex = True)

    data['gender'] = data['gender'].fillna('Undisclosed')

    data['dob'] = data['dob'].fillna(pd.Timestamp('1900-01-01'))
    data['dob'] = pd.to_datetime(data['dob'], format = 'mixed', dayfirst= True)

    data['email'] = data['email'].str.lower()
    data['email'] = data['email'].fillna('example@example.com')

    data['city'] = data['city'].str.title()
    data['city'] = data['city'].fillna('Unknown')
    data['address'] = data['address'].fillna('Unknown')
    data['postcode'] = data['postcode'].str.upper()
    data['postcode'] = data['postcode'].fillna('Unknown')

   # Drop unwanted column
    if 'phone_number' in data.columns:
        data = data.drop(columns='phone_number')

    data['uni'] = data['uni'].str.title()
    def fix_uni_degree(row):
        if pd.isna(row['uni']) and pd.isna(row['degree']):
            row['uni'] = 'Did not attend'
            row['degree'] = 'Did not attend'
        elif pd.isna(row['uni']):
            row['uni'] = 'Unknown'
        return row
    data = data.apply(fix_uni_degree, axis = 1)

    data['degree'] = data['degree'].str.replace('1st', '1:1')
    data['degree'] = data['degree'].str.replace('3rd', '3:1')

    data["invited_date"] = data['invited_date'].astype(str) + " " + data["month"]
    data['invited_date'] = data['invited_date'].fillna(pd.Timestamp('1900-01-01'))
    data['invited_date'] = pd.to_datetime(data['invited_date'], format = 'mixed', dayfirst= True)
    
    if 'month' in data.columns:
        data = data.drop(columns='month')
    
    data['invited_by'] = data['invited_by'].fillna('Not invited')
    data['invited_by'] = data['invited_by'].str.title()

    return data

# clean_data = transform(data)
# print(clean_data)

# null = clean_data.head(1000)
# print(null)