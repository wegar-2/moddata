import numpy as np

from moddata.pipeline.bankchurn_pipeline import BankchurnPipeline
from moddata.src.config import BankchurnPipelineConfig


def test_bankchurn_pipeline_tree_like():
    X_train, X_test, y_train, y_test = BankchurnPipeline(
        config=BankchurnPipelineConfig(
            random_state=12345,
            train_size=0.8,
            encoding_and_scaling_model_type="tree_like"
        )
    ).run()

    assert X_train.shape == (8_000, 11)
    assert X_test.shape == (2_000, 11)
    assert y_train.shape == (8_000, 1)
    assert y_test.shape == (2_000, 1)

    assert np.all(np.array(y_test.index[:3]) == np.array([7867, 1402, 8606]))


test_bankchurn_pipeline_tree_like