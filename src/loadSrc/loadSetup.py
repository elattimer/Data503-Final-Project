import urllib
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy.engine.base
from passwords.passwords import get_database_password

def server_connection() -> sqlalchemy.engine.base.Engine:
    # Connection details
    server = "127.0.0.1,14330"  # local port forwarded by SSH
    database = "SpartaRecruits2"
    username = "SA"
    password = get_database_password()
    # ODBC connection string
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=no;"
        "TrustServerCertificate=yes;"
    )

    # Encode for sqlalchemy
    conn_url = "mssql+pyodbc:///?odbc_connect={}".format(urllib.parse.quote_plus(conn_str))

    # Create engine
    engine = create_engine(conn_url)

    return engine


