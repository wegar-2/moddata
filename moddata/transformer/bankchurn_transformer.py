from typing import Final

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    OneHotEncoder, StandardScaler, MinMaxScaler
)
from sklearn.compose import ColumnTransformer

from moddata.src.constants import EncodingAndScalingModelType
from moddata.sklearn_extensions.log_standard_scaler import LogStandardScaler
from moddata.src.config import BankchurnTransformerConfig
from moddata.src.constants import TrainTestXyDataFrames


class BankchurnTransformer:

    def __init__(self, config: BankchurnTransformerConfig):
        self._config: Final[BankchurnTransformerConfig] = config

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
    def _age_scaler() -> LogStandardScaler:
        return LogStandardScaler()

    @staticmethod
    def _balance_scaler() -> LogStandardScaler:
        return LogStandardScaler(shift=1E-6)

    def _get_column_transformer(
            self,
            encoding_and_scaling_model_type: EncodingAndScalingModelType
    ) -> ColumnTransformer:
        if encoding_and_scaling_model_type == "tree_like":
            return ColumnTransformer(
                transformers=[
                    ("ohe_gender_encoder", self._ohe_gender_encoder(), ["gender"]),
                    ("ohe_encode_country", self._ohe_encode_country(), ["country"])
                ],
                remainder="passthrough",
                force_int_remainder_cols=False,
                verbose=False
            )
        elif encoding_and_scaling_model_type == "other":
            return ColumnTransformer(
                transformers=[
                    ("ohe_gender_encoder", self._ohe_gender_encoder(), ["gender"]),
                    ("ohe_encode_country", self._ohe_encode_country(), ["country"]),
                    ("credit_score_dist_scaler", self._credit_score_dist_scaler(), ["credit_score"]),
                    ("estimated_salary_scaler", self._estimated_salary_scaler(), ["estimated_salary_scaler"]),
                    ("age_scaler", self._age_scaler(), ["age"]),
                    ("balance_scaler", self._balance_scaler(), ["balance"])
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
    ) -> TrainTestXyDataFrames:
        X, y = data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            train_size=self._config.train_size,
            random_state=self._config.random_state
        )
        if self._config.encoding_and_scaling_model_type is not None:
            col_trfm: ColumnTransformer = self._get_column_transformer(
                encoding_and_scaling_model_type=self._config.encoding_and_scaling_model_type
            )
            X_train, y_train = col_trfm.fit_transform(X=X_train, y=y_train)
            X_test, y_test = col_trfm.transform(X=X_test, y=y_test)
        return X_train, X_test, y_train, y_test
