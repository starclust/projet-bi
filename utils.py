# utils.py

import pandas as pd
import pyodbc

# Connexion SQL Server
def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-8COGQR0;"
        "DATABASE=DW_Fico;"
        "UID=PI_SA;"
        "PWD=Nour123;"
        "TrustServerCertificate=yes;"
        "MARS_Connection=yes;"
    )

def get_historical_data():
    conn = get_connection()
    query = """
        SELECT 
            FORMAT(d.date, 'yyyy-MM-01') AS ds,
            SUM(f.Amount_payement_Customer) AS y
        FROM FACT_Fico f
        JOIN Dim_Date d ON f.FK_DatePayement = d.code_date
        WHERE f.Amount_payement_Customer IS NOT NULL
        GROUP BY FORMAT(d.date, 'yyyy-MM-01')
        ORDER BY ds
    """
    df = pd.read_sql(query, conn)
    df["ds"] = pd.to_datetime(df["ds"])
    return df

def create_features(date_str):
    date = pd.to_datetime(date_str)

    # Charger l'historique directement depuis SQL
    historique = get_historical_data()

    # Ajouter la nouvelle date cible avec valeur fictive
    nouvelle_ligne = pd.DataFrame({"ds": [date], "y": [0]})
    full_df = pd.concat([historique, nouvelle_ligne], ignore_index=True)

    # Tri et features
    full_df = full_df.sort_values("ds").reset_index(drop=True)
    full_df["month"] = full_df["ds"].dt.month
    full_df["year"] = full_df["ds"].dt.year
    full_df["lag_1"] = full_df["y"].shift(1)
    full_df["lag_2"] = full_df["y"].shift(2)
    full_df["rolling_mean_3"] = full_df["y"].rolling(window=3).mean()

    # Retourner uniquement la ligne pour la date demandée
    return full_df[full_df["ds"] == date][["month", "year", "lag_1", "lag_2", "rolling_mean_3"]]
