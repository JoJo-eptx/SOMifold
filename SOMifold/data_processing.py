import pandas as pd

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df['Latitude'] = df['Latitude'].replace("No Data", pd.NA)
    df['Longitude'] = df['Longitude'].replace("No Data", pd.NA)
    df = df.dropna(subset=['Latitude', 'Longitude'])
    df = df.query("`Person Type` not in ['4 - PEDESTRIAN', '3 - PEDALCYCLIST'] and `On System Flag` == 'No'")
    return df
