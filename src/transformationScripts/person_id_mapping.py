from extract import extract
import pandas as pd
import string
from datetime import datetime
#----------------------------------------------------------------------------------------------------------------------#

#Get the data from extract
#WILL BE TRANSFORMED DATE WHEN AVAILIABLE
data = extract()


def set_person_id_for_applicants(applicants_df: pd.DataFrame)->pd.DataFrame:
    """
    Get the applicant data, and create the ids using the index
    :param applicants_df:
    :return applicants_df:
    """

    applicants_df.index += 1
    applicants_df["person_id"] = applicants_df.index
    return applicants_df


def strips_names(name: str)->str:
    """
    Removes all punctuation and spaces. Uppercases the name.

    :param name:
    :return stripped_name:
    """
    stripped_name = name.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").upper()
    return stripped_name



def make_person_id_mapping_df(applicants_df: pd.DataFrame)->pd.DataFrame:
    """
    Creates data frame of stripped names, interview dates and person_ids
    :param applicants_df:
    :return df:
    """
    df = applicants_df[['name','invited_date',"person_id"]].rename(columns={'invited_date':'date','person_id':'id'})

    df['date']=pd.to_datetime(df['date'],dayfirst=True)
    #Sets datetime object TO BE REMOVED AFTER TRANSFORMATIONS
    df['date']=df['date'].fillna(datetime(2030,1,1))
    df['name']=df['name'].apply(strips_names)


# Funtion that gets the frequency of names in a list
def get_name_frequency_dict(names: list) -> dict[str, int]:
    """
    Gets the frequency of each name and stores in a dict

    :param names:
    :return dict_names:
    """

    dict_names: dict[str, int] = {}

    for name in names:
        if name in dict_names:
            dict_names[name] += 1
        else:
            dict_names[name] = 1

    return dict_names

def get_frequency_dict(df: pd.DataFrame)->dict[str, int]:
    """

    :param df:
    :return names_freq:
    """
    names_freq = get_name_frequency_dict(df['name'].to_list())
    return names_freq

#Choose person id based on name and course start date
def get_person_id(name: str, date: datetime,course = False)->int:
    """
    Intakes name and date, chooses person id from the mapping table.

    :param name:
    :param date:
    :param course:
    :return:
    """
    id = "NOIDSET"
    name = strips_names(name)

    check = names_freq[name]
    if check == 1:
        id = df.loc[df['name']==name]['id'].iloc[0]
        return id

    if check > 1:
        if not course:
            id = df.loc[(df['name'] == name) & (df['date']==date)]['id'].iloc[0]

            return id

        else:
            options = df.loc[df['name'] == name,df['date']==date]
            options['datediff']= (date - options['date']).days
            options = options.loc[options['datediff']>0]
            options.sort_values(by='datediff', ascending=True, inplace=True)
            id = options.index[0]
            return id

    return id


"""
EXAMPLE
person_ids = []
for index,row in txt_names.iterrows():
    person_ids.append(get_person_id(row['name'],row['date']))

txt_names['person_id']= person_ids

"""