from pathlib import Path
from typing import Final

import pandas as pd


class StooqDataExtractor:

    def __init__(
            self,
            data_folder: Path,
            files: list[str]
    ):
        self._data_folder: Final[Path] = data_folder
        self._files: Final[list[str]] = files

    def _retrieve_ticker(self, file: str) -> str:
        return file.split(".")[0].split("_")[0]

    def _extract_file(self, file: str) -> pd.DataFrame:
        data = pd.read_csv(self._data_folder / file, sep=",", decimal=".",)
        data.columns = [c.lower() for c in data.columns]
        data["date"] = pd.to_datetime(data["date"])
        data = data.set_index("date")
        data.columns = pd.MultiIndex.from_product([
            [self._retrieve_ticker(file)],
            list(data.columns),
        ], names=["ticker", "variable"])
        return data

    def extract(self) -> dict[str, pd.DataFrame]:
        return {file: self._extract_file(file) for file in self._files}
