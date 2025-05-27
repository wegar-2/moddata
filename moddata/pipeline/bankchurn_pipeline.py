from typing import Final, Optional

import pandas as pd

from moddata.extractor.bankchurn_extractor import BankchurnExtractor
from moddata.transformer.bankchurn_transformer import BankchurnTransformer
from moddata.src.constants import EncodingAndScalingModelType


class BankchurnPipeline:

    def __init__(
            self,
            train_size: float | int,
            random_state: Optional[int] = None,
            encoding_and_scaling_model_type: Optional[EncodingAndScalingModelType] = None
    ):
        self._random_state: Optional[int] = random_state
        self._encoding_and_scaling_model_type: Optional[EncodingAndScalingModelType] = encoding_and_scaling_model_type
        self._transformer: Final[BankchurnTransformer] = (
            BankchurnTransformer(
                train_size=train_size,
                random_state=random_state,
                encoding_and_scaling_model_type=self._encoding_and_scaling_model_type
            )
        )

    def run(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        x, y = BankchurnExtractor().extract()
        return self._transformer.transform(data=(x, y))
