from typing import Final

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin


class LogStandardScaler(TransformerMixin, BaseEstimator):

    def __init__(
            self,
            shift: float = 0.0,
            log_base: float | int = np.e
    ):
        """
        Scaler for handling log-normal variables. Consists of taking log
        and applying the usual standardization.

        Consistent with sklearn API's:
        (1) Estimator API (.fit method)
        (2) Transformer API (.transform method)

        Note that in line with docs (cf. below) the mixin class is inherited
        first.

        For more detail of sklearn API cf.:
        https://scikit-learn.org/stable/developers/develop.html

        Args:
            shift: positive float, shift to apply to the input values
            before log-transformation
            log_base: base of the log-transformation
        """
        self.shift: Final[float] = shift
        self.log_base: float | int = log_base

        self.feature_names_in_ = None

    @staticmethod
    def _validate_shift(shift: float) -> None:
        if shift < 0:
            raise ValueError(f"Only non-negative shift is allowed! "
                             f"Received value {shift=}")

    def _log_transform(self, X):
        return np.emath.logn(n=self.log_base, x=X + self.shift)

    def fit(self, X: pd.DataFrame):
        self._standard_scaler: StandardScaler = StandardScaler() # noqa
        if not isinstance(X, pd.DataFrame):
            raise ValueError("This estimator only accepts pd.DataFrame input!")
        self.feature_names_in_ = list(X.columns)
        X_log = self._log_transform(X=X)
        self._standard_scaler.fit(X=X_log)
        return self

    def transform(self, X: pd.DataFrame):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("This transformer only accepts pd.DataFrame input!")
        X_log = self._log_transform(X=X)
        return self._standard_scaler.transform(X=X_log + self.shift)

    def fit_transform(self, X, y=None, **fit_params):
        return self.fit(X=X).transform(X=X)

    def get_feature_names_out(self, input_features=None):
        if input_features is None:
            if self.feature_names_in_ is not None:
                input_features = self.feature_names_in_
            else:
                raise ValueError("No input features provided and none "
                                 "were stored during fit! ")
        return [
            f"log_base_{self.log_base:0.2f}_shift_{self.shift:0.2f}_{feature}"
            for feature in input_features
        ]
