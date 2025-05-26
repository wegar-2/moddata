from typing import Optional

import pandas as pd
from sklearn.model_selection import train_test_split


class BankchurnTransformer:

    def __init__(
            self,
            train_size: float | int,
            random_state: Optional[int] = None,
    ):
        self._train_size: float | int = train_size
        self._random_state: Optional[int] = random_state

    def transform(
            self,
            data: tuple[pd.DataFrame, pd.DataFrame]
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        X, y = data
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            train_size=self._train_size,
            random_state=self._random_state
        )
        return X_train, X_test, y_train, y_test
