import pandas as pd
import os

def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame.

    Args:
        path (str): The file path of the dataset.

    Returns:
        pd.DataFrame: The loaded dataset or None if an error occurs.
    """
    if not os.path.exists(path):
        print("Error: The file does not exist:", path)
        return None

    if not path.lower().endswith('.csv'):
        print("Error: The file format is not .csv")
        return None

    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as error:
        print("Error loading CSV:", error)
        return None
