from typing import Final

from moddata.extractor.bankchurn_extractor import BankchurnExtractor
from moddata.transformer.bankchurn_transformer import BankchurnTransformer
from moddata.src.constants import TrainTestXyDataFrames
from moddata.src.config import BankchurnPipelineConfig


class BankchurnPipeline:

    def __init__(self, config: BankchurnPipelineConfig):
        self._config: Final[BankchurnPipelineConfig] = config
        self._transformer: Final[BankchurnTransformer] = (
            BankchurnTransformer(config=self._config)
        )

    def run(self) -> TrainTestXyDataFrames:
        x, y = BankchurnExtractor().extract()
        return self._transformer.transform(data=(x, y))
