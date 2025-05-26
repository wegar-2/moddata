import numpy as np

from moddata.pipeline.bankchurn_pipeline import BankchurnPipeline


def test_bankchurn_pipeline_run():
    X_train, X_test, y_train, y_test = BankchurnPipeline(
        random_state=12345,
        train_size=0.8
    ).run()

    assert X_train.shape == (8_000, 10)
    assert X_test.shape == (2_000, 10)
    assert y_train.shape == (8_000, 1)
    assert y_test.shape == (2_000, 1)

    assert np.all(np.array(y_test.index[:3]) == np.array([7867, 1402, 8606]))
