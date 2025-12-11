from typing import Final

import pandas as pd


class DownloadGeomagneticIndexExtractor:

    _DATA_URL: Final[str] = "https://kp.gfz.de/app/files/Kp_ap_Ap_SN_F107_since_1932.txt"

    def extract(self) -> pd.DataFrame:
        pass


if __name__ == '__main__':
    DownloadGeomagneticIndexExtractor()