import pandas as pd

# On ne supprime que les colonnes vraiment optionnelles
# 'sucre', 'calories', 'graisses' sont NOT NULL en base → on les garde
col_drop = []  # rien à supprimer pour l'instant

def transform_data(aliment_df: pd.DataFrame, utilisateur_df: pd.DataFrame):
    """
    Transforme les données sans supprimer les colonnes obligatoires en base.
    """
    # Convertir bio en float et créer 'nom complet' comme colonne calculée
    aliment_df['bio'] = aliment_df['bio'].astype(float)

    aliment_df['nom_marque'] = (
            aliment_df['nom']
            + ' '
            + aliment_df['marque'].fillna('').str.strip()
    )



    # Utilisateur : créer 'nom complet' comme colonne calculée
    utilisateur_df['nom complet'] = (
        utilisateur_df['nom'] + ' ' + utilisateur_df['prenom'].fillna('')
    ).str.strip()

    print("Transformation terminée.")
    print("Aperçu aliment :\n", aliment_df.head(3))
    print("Aperçu utilisateur :\n", utilisateur_df[['nom', 'prenom', 'nom complet']].head(3))

    return aliment_df, utilisateur_df