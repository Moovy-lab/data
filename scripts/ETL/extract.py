import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


def get_engine():
    """Crée un engine SQLAlchemy vers MySQL/foodly."""
    return create_engine(
        f"mysql+mysqlconnector://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )


def extraction_data(table_name, columns_list):
    """Extrait des colonnes spécifiques d'une table MySQL."""
    engine = get_engine()
    cols_str = ", ".join([f"`{col}`" for col in columns_list])
    query = f"SELECT {cols_str} FROM `{table_name}`"

    df = pd.read_sql(query, engine)
    print(f"Extraction réussie : {len(df)} lignes depuis '{table_name}'")
    return df


def extract_data_dpt(table_name):
    """Extrait l'intégralité d'une table MySQL."""
    engine = get_engine()
    query = f"SELECT * FROM `{table_name}`"

    df = pd.read_sql(query, engine)
    print(f"Extraction réussie : {len(df)} lignes depuis '{table_name}'")
    return df