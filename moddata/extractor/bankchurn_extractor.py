from typing import Optional, TypeAlias

from moddata import load_data
import pandas as pd
from sklearn.model_selection import train_test_split


class BankchurnExtractor:

    def extract(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        data: pd.DataFrame = load_data(dataset="bankchurn")
        x: pd.DataFrame = data.loc[:, data.columns != "churn"]
        x = x.drop(columns=["customer_id"])
        y: pd.DataFrame = data.loc[:, ["churn"]]
        return x, y
