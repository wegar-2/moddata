from typing import Final

import numpy as np
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
        self._shift: Final[float] = shift
        self._standard_scaler: StandardScaler = StandardScaler()
        self._log_base: float | int = log_base

    @staticmethod
    def _validate_shift(shift: float) -> None:
        if shift < 0:
            raise ValueError(f"Only non-negative shift is allowed! "
                             f"Received value {shift=}")

    def _log_transform(self, X):
        return np.emath.logn(n=self._log_base, x=X + self._shift)

    def fit(self, X, y=None):
        X_log = self._log_transform(X=X)
        self._standard_scaler.fit(X=X_log)
        return self

    def transform(self, X):
        X_log = self._log_transform(X=X)
        return self._standard_scaler.transform(X=X_log + self._shift)

    def fit_transform(self, X, y=None, **fit_params):
        return self.fit(X=X).transform(X=X)
