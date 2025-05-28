import numpy as np
import pandas as pd

from moddata import load_data


def test_load_data_bankchurn():
    data: pd.DataFrame = load_data(dataset="bankchurn")
    assert data.shape == (10_000, 12)
    assert set(data.columns) == {
        'customer_id', 'credit_score', 'country', 'gender', 'age', 'tenure',
        'balance', 'products_number', 'credit_card', 'active_member',
        'estimated_salary', 'churn'
    }
    assert data.at[17, "credit_card"] == np.int64(1)


def test_load_data_btc():
    data: pd.DataFrame = load_data(dataset="btc")
    assert data.shape == (2_590_118, 6)
    assert set(data.columns) == {
        'open', 'high', 'low', 'close', 'vol_btc', 'vol_usd'
    }
    assert data.index[0] == pd.Timestamp("2017-01-01 00:01:00")


def test_load_data_pl_banking_stocks():
    data: pd.DataFrame = load_data(dataset="pl_banking_stocks")
    assert data.shape == (5_003, 40)
    assert set(data.columns.unique(0)) == {
        'citi', 'bos', 'ing', 'mbank', 'mil', 'pekao', 'pkobp', 'santander'
    }
