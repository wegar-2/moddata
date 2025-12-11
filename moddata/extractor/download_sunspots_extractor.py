import logging
from typing import Final

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class DownloadSunspotsExtractor:

    _DAILY_TOTAL_SUNSPOT_NUMBER_URL: Final[str] = "https://www.sidc.be/SILSO/INFO/sndtotcsv.php"

    def extract(self) -> pd.DataFrame:
        data = pd.read_csv(
            self._DAILY_TOTAL_SUNSPOT_NUMBER_URL,
            delimiter=";",
            decimal=".",
            names=[
                "year", "month", "day", "yearfrac_date",
                "daily_sunspots_number",
                "daily_std_across_stations",
                "obs_num", "is_definitive"
            ],
            na_values=-1
        )
        data = data[["year", "month", "day", "daily_sunspots_number"]]
        data["day"] = (
                data["year"].astype(str) + "-" +
                data["month"].apply(lambda x: f"{x:02}") + "-" +
                data["day"].apply( lambda x: f"{x:02}")
        )
        data = data[["day", "daily_sunspots_number"]]
        data["daily_sunspots_number"] = np.where(
            data["daily_sunspots_number"] == -1,
            np.nan,
            data["daily_sunspots_number"]
        )
        return data


if __name__ == "__main__":
    from pathlib import Path
    data = DownloadSunspotsExtractor().extract()
    data.to_parquet(
        Path(__file__).parent.parent / "data" / "sunspots.parquet"
    )
    print("halt")
