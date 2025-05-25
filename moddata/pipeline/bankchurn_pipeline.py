from typing import Optional

from moddata.extractor.bankchurn_extractor import BankchurnExtractor
import pandas as pd

from sklearn.model_selection import train_test_split


class BankchurnPipeline:

    def __init__(
            self,
            random_state: Optional[int] = None,
    ):
        self._random_state: Optional[int] = random_state

    def run(self):
        x, y = BankchurnExtractor().extract()
