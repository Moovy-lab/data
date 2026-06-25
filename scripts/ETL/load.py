import pandas as pd
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv


load_dotenv()

COLONNES_CALCULEES = {
    'utilisateur': ['nom complet'],
    'aliment': ['nom_marque']
}

def get_engine():
    return create_engine(
        f"mysql+mysqlconnector://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )

def load_data(df: pd.DataFrame, target_table: str):
    engine = get_engine()
    try:
        cols_a_exclure = COLONNES_CALCULEES.get(target_table, [])
        df_to_load = df.drop(columns=cols_a_exclure, errors='ignore')

        # Tout dans une seule transaction : si INSERT échoue, TRUNCATE est annulé
        with engine.begin() as conn:
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
            conn.execute(text(f"TRUNCATE TABLE `{target_table}`;"))
            conn.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))

            # Insertion ligne par ligne dans la même transaction
            df_to_load.to_sql(
                name=target_table,
                con=conn,          # ← utilise la connexion de la transaction
                if_exists='append',
                index=False
            )

        print(f"Table '{target_table}' chargée avec succès ({len(df_to_load)} lignes).")

    except Exception as err:
        print(f"Erreur lors du chargement de '{target_table}' : {err}")