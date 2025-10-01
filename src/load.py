from loadSrc.loadSetup import server_connection
import urllib
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy.engine.base

def load(data : pd.DataFrame):
    engine = server_connection()
    df_strengths = pd.DataFrame(data["strengths"])
    df_strengths.to_sql('sparta_day_strengths_results', engine, if_exists='append', index=False)
    df_weaknesses = pd.DataFrame(data["weaknesses"])
    df_weaknesses.to_sql('sparta_day_weaknesses_results', engine, if_exists='append', index=False)
    df_tech = pd.DataFrame(data["tech_skills"])
    df_tech.to_sql('sparta_day_tech_results', engine, if_exists='append', index=False)