import pandas as pd

def extract(file):
    
    extracted_df = pd.read_csv(file, sep=";", encoding="latin-1")
    return extracted_df