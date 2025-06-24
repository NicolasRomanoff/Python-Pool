import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Load and return data from csv files'''
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(e)
    return None
