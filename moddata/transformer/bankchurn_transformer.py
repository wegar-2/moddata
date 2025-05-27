from typing import Optional

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    OneHotEncoder, StandardScaler, MinMaxScaler
)
from sklearn.compose import ColumnTransformer

from moddata.src.constants import EncodingAndScalingModelType


class BankchurnTransformer:

    def __init__(
            self,
            train_size: float | int,
            random_state: Optional[int] = None,
            encoding_and_scaling_model_type: Optional[EncodingAndScalingModelType] = None,
    ):
        """

        Args:
            train_size: parameter passed to the train_test_split method
            used to create train and test datasets
            random_state: analogous to train_size
            encoding_and_scaling_model_type: Literal, defines what type of
            model data should be prepared for
        """
        self._train_size: float | int = train_size
        self._random_state: Optional[int] = random_state
        self._encoding_model_type: Optional[EncodingAndScalingModelType] = (
            encoding_and_scaling_model_type)

    @staticmethod
    def _ohe_gender_encoder() -> OneHotEncoder:
        return OneHotEncoder(
            categories=[["Female", "Male"]],
            drop="first"
        )

    @staticmethod
    def _ohe_encode_country() -> OneHotEncoder:
        return OneHotEncoder(
            categories=[["France", "Germany", "Spain"]],
            drop="first"
        )

    @staticmethod
    def _credit_score_dist_scaler() -> StandardScaler:
        return StandardScaler()

    @staticmethod
    def _estimated_salary_scaler() -> MinMaxScaler:
        return MinMaxScaler()

    @staticmethod
    def _age_scaler():
        pass

    def _get_column_transformer(
            self,
            encoding_and_scaling_model_type: EncodingAndScalingModelType
    ) -> ColumnTransformer:
        if encoding_and_scaling_model_type == "tree_like":
            return ColumnTransformer(
                transformers=[
                    (),
                ],
                remainder="passthrough",
                force_int_remainder_cols=False,
                verbose=False
            )
        elif encoding_and_scaling_model_type == "other":
            return ColumnTransformer(
                transformers=[

                ],
                remainder="passthrough",
                force_int_remainder_cols=False,
                verbose=False
            )
        else:
            raise ValueError(f"Encountered unhandled "
                             f"{encoding_and_scaling_model_type=}")

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


if __name__ == "__main__":

    from moddata.extractor.bankchurn_extractor import BankchurnExtractor

    data = BankchurnExtractor().extract()
    BankchurnTransformer(
        train_size=0.8,
        random_state=1234
    ).transform(data=data)
