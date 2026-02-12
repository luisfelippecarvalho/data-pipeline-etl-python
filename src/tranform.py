import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply basic transformations to the dataframe.

    Steps:
    - Standardize column names to lowercase
    - Remove rows with missing values
    """

    # Padroniza nomes das colunas
    df.columns = df.columns.str.lower()

    # Remove valores nulos
    df = df.dropna()

    return df
