import sys
import os
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scripts.ETL.extract import extraction_data, extract_data_dpt
from scripts.ETL.transform import transform_data
from scripts.ETL.load import load_data

with open('config.yaml', 'r') as file:
    config_data = yaml.safe_load(file)

def run_pipeline():
    # step 1 — extract
    df_ali  = extraction_data(config_data['table_aliment'], config_data['select_col'])
    df_user = extract_data_dpt(config_data['table_utilisateur'])

    # step 2 — transform (les deux df sont nécessaires)
    df_ali, df_user = transform_data(df_ali, df_user)

    # step 3 — load
    load_data(df_ali,  'aliment')
    load_data(df_user, 'utilisateur')

if __name__ == "__main__":
    run_pipeline()