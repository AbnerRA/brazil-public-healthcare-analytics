import pandas as pd

files = {
    "Febre Amarela": "data/raw/cpnibr17804141303-febreamarela.csv",
    "Poliomielite": "data/raw/cpnibr17804261819-polio.csv",
    "Tríplice Viral D1": "data/raw/cpnibr17804260724-tripliceD1.csv",
    "Tríplice Viral D2": "data/raw/cpnibr17804260890-tripliceD2.csv"
}

dfs = []
    
def process_vaccine_data(vaccine_name, file):

    df = pd.read_csv(file, sep=";", encoding="latin-1")
    
    #Removes leading/trailing spaces in the 'Ano' column values
    df["Ano"] = df["Ano"].str.strip()

    df = df[df["Ano"] != "Total"]

    df_unpivoted = df.melt(id_vars=["Ano"], var_name="State", value_name="Coverage")

    #Removes leading/trailing spaces in the 'State' column values
    df_unpivoted["State"] = df_unpivoted["State"].str.strip()

    df_unpivoted = df_unpivoted[df_unpivoted["State"] != "Total"]

    df_unpivoted["Vaccine"] = vaccine_name

    df_unpivoted["Coverage"] = df_unpivoted["Coverage"].astype(str).str.replace(",", ".").astype(float)

    df_unpivoted["Year"] = df_unpivoted["Ano"].astype(int)

    #print(df_unpivoted.head())

    df_unpivoted = df_unpivoted[["Year", "State", "Vaccine", "Coverage"]]

    dfs.append(df_unpivoted)

for vaccine_name, file in files.items():
    process_vaccine_data(vaccine_name, file)

result = pd.concat(dfs, ignore_index=True)

result.to_csv("data/processed/vaccination_coverage.csv", index=False)

print("Shape: " + str(result.shape))
print("DataFrame Info: ")
print(result.info())
print("DataFrame Description: ")
print(result.describe())
print("Null rows count: ")
#print(result.isna.sum())

print(result.head())
print()
print('Row count:', len(result))