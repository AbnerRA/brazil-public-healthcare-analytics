import pandas as pd

from extract import extract
from transform import transform
from load import load


files = {
    "Febre Amarela": "data/raw/cpnibr17804141303-febreamarela.csv",
    "Poliomielite": "data/raw/cpnibr17804261819-polio.csv",
    "Tríplice Viral D1": "data/raw/cpnibr17804260724-tripliceD1.csv",
    "Tríplice Viral D2": "data/raw/cpnibr17804260890-tripliceD2.csv"
}

dfs = []

for vaccine_name, file in files.items():

    # 1. Extract data from DATASUS files
    print("Extracting " + vaccine_name + " database...")
    extracted_df = extract(file)

    # 2. Transform raw data into analytical format (unpivoted/long)
    print("Transforming "+ vaccine_name + " database...")
    df_unpivoted = transform(vaccine_name, extracted_df)

    dfs.append(df_unpivoted)

#Treated DataFrame export 
#result.to_csv("data/processed/vaccination_coverage.csv", index=False)

df_appended = pd.concat(dfs, ignore_index=True)

# 3. Load data into database (PostgreSQL)
print("Loading full database...")
load(df_appended)

print("Success!")