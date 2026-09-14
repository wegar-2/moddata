from typing import Final

import pandas as pd


class CboeVIXDataExtractor:

    _URL: Final[str] = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"

    def extract(self) -> pd.DataFrame:
        data: pd.DataFrame = pd.read_csv(self._URL)
        data.columns = [c.lower() for c in data.columns]
        data["date"] = pd.to_datetime(data["date"])
        data = data.set_index("date")
        data.columns = pd.MultiIndex.from_product([["VIX"], list(data.columns)])
        return data
