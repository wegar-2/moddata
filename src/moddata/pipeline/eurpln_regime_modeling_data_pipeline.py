from datetime import date
from pathlib import Path

import pandas as pd

from moddata.extractor.stooq_data_extractor import StooqDataExtractor
from moddata.extractor.cboe_vix_data_extractor import CboeVIXDataExtractor
from moddata.transformer.merge_stooq_data_transformer import (
    MergeStooqDataTransformer)


class EURPLNRegimeModelingDataPipeline:

    def __init__(
            self,
            start: date = date(2016, 1, 1),
            end: date = date(2025, 12, 31)
    ):
        self._start, self._end = start, end
        self._stooq_extractor = StooqDataExtractor(
            data_folder=(
                    Path(__file__).parent.parent /
                    "data" /
                    "regime_model_data"
            ),
            files=[
                "10ydey_b_d.csv",
                "10yply_b_d.csv",
                "10yusy_b_d.csv",
                "^uslc_d.csv",
                "eurczk_d.csv",
                "eurhuf_d.csv",
                "eurpln_d.csv",
                "eurusd_d.csv",
                "usdpln_d.csv"
            ]
        )
        self._stooq_transformer = MergeStooqDataTransformer()
        self._vix_extractor = CboeVIXDataExtractor()

    def run(self):
        stooq_data = self._stooq_extractor.extract()
        stooq_data = self._stooq_transformer.transform(stooq_data)

        vix_data = self._vix_extractor.extract()

        data = pd.merge(
            left=stooq_data,
            right=vix_data,
            how="outer",
            left_index=True,
            right_index=True
        )
        data = data[f"{self._start:%Y-%m-%d}":f"{self._end:%Y-%m-%d}"]
        data = data.ffill().bfill()
        return data


if __name__ == "__main__":
    data = EURPLNRegimeModelingDataPipeline().run()
    print("halt! ")
