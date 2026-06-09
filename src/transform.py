import pandas as pd
 
def transform(vaccine_name, df):
    
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

    df_unpivoted.rename(columns = {'Ano':'year', 'State':'state', 'Coverage':'coverage', 'Vaccine':'vaccine'}, inplace=True)

    df_unpivoted = df_unpivoted[["year", "state", "vaccine", "coverage"]]

    return df_unpivoted