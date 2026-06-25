import mysql.connector
import pandas as pd  # Utilisation de l'alias standard 'pd'
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Connexion à MySQL
con = mysql.connector.connect(
    f"mysql+mysqlconnector://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}/"
    f"{os.getenv('DB_NAME')}"
)

# 2. Chargement direct dans un DataFrame Pandas avec read_sql
df_data = pd.read_sql("SELECT * FROM utilisateur", con)

# 3. Chargement de la deuxième requête
requete_aliment = """
    SELECT
        nom,
        marque,
        sucre,
        calories,
        graisses,
        proteines,
        bio
    FROM
        aliment
"""
df_fimo = pd.read_sql(requete_aliment, con)

# Optionnel : Fermer la connexion une fois terminé
con.close()

# Vérification (pour tester le résultat)
print(df_data.head())
print(df_fimo.head())
