import pandas as pd

from moddata import load_data


class BankchurnExtractor:

    def extract(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        data: pd.DataFrame = load_data(dataset="bankchurn")
        x: pd.DataFrame = data.loc[:, data.columns != "churn"]
        x = x.drop(columns=["customer_id"])
        y: pd.DataFrame = data.loc[:, ["churn"]]
        return x, y
