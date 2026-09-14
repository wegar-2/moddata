import logging
from typing import Final

import numpy as np
import pandas as pd
import requests

logger = logging.getLogger(__name__)


class DownloadGeomagneticIndexExtractor:

    _DATA_URL: Final[str] = \
        "https://kp.gfz.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt"
    _FIRST_DATA_LINE: Final[int] = 41
    _COLUMNS_TO_TYPES: Final[dict[str, type]] = {
        "year": int, "month": int, "day": int, "days": int, "days_m": float,
        "Bsr": int, "dB": int,
        "Kp1": float, "Kp2": float, "Kp3": float, "Kp4": float,
        "Kp5": float, "Kp6": float, "Kp7": float, "Kp8": float,
        "ap1": int, "ap2": int, "ap3": int, "ap4": int, "ap5": int,
        "ap6": int, "ap7": int,  "ap8": int,
        "Ap": int, "SN": int,
        "F10.7obs": float, "F10.7adj": float, "D": int
    }

    def extract(self) -> pd.DataFrame:
        data = requests.get(self._DATA_URL)
        lines: list[str] = str(data.content).split("\\n")
        data_lines: list[pd.DataFrame] = []
        for i, line in enumerate(lines[self._FIRST_DATA_LINE:], start=1):
            if i % 250 == 0:
                print(f"processing line {i}")
            cols = [col for col in line.split(" ") if col != ""]
            if len(cols) == 28:
                row = pd.DataFrame(
                    data=np.array(cols).reshape(-1, 28),
                    columns=list(self._COLUMNS_TO_TYPES.keys())
                )
                row = row.astype(self._COLUMNS_TO_TYPES) # noqa
                data_lines.append(
                    row # noqa
                )
        return pd.concat(data_lines, axis=0).reset_index(drop=True)
