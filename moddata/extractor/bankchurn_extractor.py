from typing import Optional, TypeAlias

from moddata import load_data
import pandas as pd
from sklearn.model_selection import train_test_split


class BankchurnPipeline:

    def __init__(
            self,
            random_state: Optional[int] = None,
    ):
        self._random_state: Optional[int] = random_state

    def run(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        data: pd.DataFrame = load_data(dataset="bankchurn")
        x: pd.DataFrame = data.loc[:, data.columns != "churn"]
        x = x.drop(columns=["customer_id"])
        y: pd.DataFrame = data.loc[:, ["churn"]]
        return x, y
