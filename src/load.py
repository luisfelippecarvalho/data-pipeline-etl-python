import pandas as pd

def load_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save dataframe to CSV file.
    """
    df.to_csv(output_path, index=False)
