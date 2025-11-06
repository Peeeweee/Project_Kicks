# /dashboard/data_loader.py

import pandas as pd

def load_data(path):
    """Loads and prepares the dataset."""
    df = pd.read_csv(path)
    df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])
    return df