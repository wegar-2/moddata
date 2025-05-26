from typing import Final, Optional

import pandas as pd

from moddata.extractor.bankchurn_extractor import BankchurnExtractor
from moddata.transformer.bankchurn_transformer import BankchurnTransformer


class BankchurnPipeline:

    def __init__(
            self,
            train_size: float | int,
            random_state: Optional[int] = None,
    ):
        self._random_state: Optional[int] = random_state
        self._transformer: Final[BankchurnTransformer] = (
            BankchurnTransformer(
                train_size=train_size,
                random_state=random_state
            )
        )

    def run(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        x, y = BankchurnExtractor().extract()
        return self._transformer.transform(data=(x, y))
