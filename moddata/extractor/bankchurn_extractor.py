import pandas as pd

from moddata import load_data
from moddata.src.constants import XyDataFrames

class BankchurnExtractor:

    def extract(self) -> XyDataFrames:
        data: pd.DataFrame = load_data(dataset="bankchurn")
        x: pd.DataFrame = data.loc[:, data.columns != "churn"]
        x = x.drop(columns=["customer_id"])
        y: pd.DataFrame = data.loc[:, ["churn"]]
        return x, y
