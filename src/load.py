from loadSrc.loadSetup import server_connection
import urllib
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy.engine.base

def load(data : pd.DataFrame):
    """
    Takes in the transformed DataFrames which mirror the tables in the SQL database.
    Creates a connection to the SQL database and appends all data to each table.

    :param data:
    :return:
    """

    engine = server_connection()


    df_person = pd.DataFrame(data["applicants"])
    df_person.to_sql('person', engine, if_exists='append', index=False)

    df_postcode = pd.DataFrame(data["sparta_day"])
    df_postcode.to_sql('sparta_day', engine, if_exists='append', index=False)

    df_strengths = pd.DataFrame(data["strengths"])
    df_strengths.to_sql('sparta_day_strengths_results', engine, if_exists='append', index=False)
    
    df_weaknesses = pd.DataFrame(data["weaknesses"])
    df_weaknesses.to_sql('sparta_day_weaknesses_results', engine, if_exists='append', index=False)
    
    df_tech = pd.DataFrame(data["tech_skills"])
    df_tech.to_sql('sparta_day_tech_results', engine, if_exists='append', index=False)
    
    df_postcode = pd.DataFrame(data["sparta_day_results"])
    df_postcode.to_sql('sparta_day_results', engine, if_exists='append', index=False)

    df_postcode = pd.DataFrame(data["postcode"])
    df_postcode.to_sql('post_codes', engine, if_exists='append', index=False)

    df_person = pd.DataFrame(data["address"])
    df_person.to_sql('address', engine, if_exists='append', index=False)
    
    df_postcode = pd.DataFrame(data["address_person"])
    df_postcode.to_sql('person_addresses', engine, if_exists='append', index=False)

    df_postcode = pd.DataFrame(data["courses"])
    df_postcode.to_sql('courses', engine, if_exists='append', index=False)

    df_postcode = pd.DataFrame(data["behaviours"])
    df_postcode.to_sql('behavioursScore', engine, if_exists='append', index=False)