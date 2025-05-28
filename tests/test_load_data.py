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


