import numpy as np
from pytest import fixture


from moddata.sklearn_extensions.log_standard_scaler import LogStandardScaler


@fixture(scope="session")
def make_log_normal_array() -> np.ndarray:
    np.random.seed(32123)
    return np.random.lognormal(mean=2, sigma=4, size=5).reshape(-1, 1)


def test_log_standard_scaler_no_shift(make_log_normal_array):
    lss: LogStandardScaler = LogStandardScaler()
    X_trfmd: np.ndarray = lss.fit_transform(X=make_log_normal_array)
    assert round(float(X_trfmd[0, 0]), 8) == -1.41835861
    assert X_trfmd.shape == (5, 1)
    assert round(float(X_trfmd[-1, 0]), 8) == -0.64893433


def test_log_standard_scaler_with_shift(make_log_normal_array):
    lss: LogStandardScaler = LogStandardScaler(shift=2)
    X_trfmd: np.ndarray = lss.fit_transform(X=make_log_normal_array)
    assert round(float(X_trfmd[0, 0]), 8) == -0.03121367
    assert X_trfmd.shape == (5, 1)
    assert round(float(X_trfmd[-1, 0]), 8) == -0.02281377


def test_log_standard_scaler_with_base(make_log_normal_array):
    lss: LogStandardScaler = LogStandardScaler(log_base=2)
    X_trfmd: np.ndarray = lss.fit_transform(X=make_log_normal_array)
    # print(f"{X_trfmd=}")
    assert round(float(X_trfmd[0, 0]), 8) == -1.41835861
    assert X_trfmd.shape == (5, 1)
    assert round(float(X_trfmd[-1, 0]), 8) == -0.64893433


def test_log_standard_scaler_with_shift_and_base(make_log_normal_array):
    lss: LogStandardScaler = LogStandardScaler(log_base=2, shift=20)
    X_trfmd: np.ndarray = lss.fit_transform(X=make_log_normal_array)
    assert round(float(X_trfmd[0, 0]), 8) == 7.12454284
    assert X_trfmd.shape == (5, 1)
    assert round(float(X_trfmd[-1, 0]), 8) == 7.1258186
