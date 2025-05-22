from pathlib import Path
import zipfile

import pandas as pd


def _make_btc_dataset():
    zip_file: Path = Path(__file__).parent / "archive.zip"
    datas: list[pd.DataFrame] = []
    with zipfile.ZipFile(zip_file, mode="r") as btc_archive:
        for filename in btc_archive.namelist():
            if filename.endswith("min.csv"):
                with btc_archive.open(filename) as file:
                    datas.append(
                        pd.read_csv(
                            file,
                            sep=",",
                            decimal=".",
                            usecols=[
                                "date", "open", "high", "low", "close",
                                "Volume BTC", "Volume USD"
                            ],
                            parse_dates=["date"]
                        )
                    )

    data: pd.DataFrame = pd.concat(datas, axis=0)
    data = data.sort_values(by="date", ascending=True).reset_index(drop=True)
    data = data.rename(columns={"date": "dt", "Volume BTC": "vol_btc", "Volume USD": "vol_usd"})
    data = data.set_index("dt")
    data = data[:"2021-12-31 23:59:00"]
    data.to_parquet(Path(__file__).parent / "btc.parquet")


if __name__ == "__main__":
    _make_btc_dataset()
    print("done")
