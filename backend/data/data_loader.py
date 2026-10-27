import pandas as pd

def load_answers() -> pd.DataFrame:
    """
    Load the answers from the CSV file and return a DataFrame.
    """
    return pd.read_csv(r"data\answers.csv", index_col=0, encoding="utf-8-sig")

def load_conditions() -> pd.DataFrame:
    """
    Load the conditions from the CSV file and return a DataFrame.
    """
    return pd.read_csv(r"data\conditions.csv", index_col=0, encoding="utf-8-sig")