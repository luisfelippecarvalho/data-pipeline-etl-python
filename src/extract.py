import pandas as pd

def extract_data(path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.

    Args:
        path (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    df = pd.read_csv(path)
    print("Extraction completed successfully.")
    return df

