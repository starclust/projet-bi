
import pandas as pd
from sqlalchemy import create_engine

def load_data():
    server = 'DESKTOP-DN3R828'
    database = 'DW_Fico'
    username = 'sam'
    password = 'sam0507'
    driver = '{ODBC Driver 17 for SQL Server}'

    engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")
    
    df_ventes = pd.read_sql("SELECT * FROM FACT_Fico", engine)
    df_clients = pd.read_sql("SELECT * FROM Dim_clients", engine)
    df_dates = pd.read_sql("SELECT * FROM Dim_Date", engine)

    df = df_ventes.merge(df_clients, left_on="FK_client", right_on="code_client", how="left") \
              .merge(df_dates, left_on="FK_DatePayement", right_on="code_date", how="left")
    
    return df
