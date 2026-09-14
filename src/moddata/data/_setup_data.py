from functools import reduce

from pathlib import Path
from typing import Final

import pandas as pd


_DATA_FOLDER_PATH: Final[Path] = Path(__file__).parent


def _extract_stooq_data(file: str, ticker: str) -> pd.DataFrame:
    data_path: Path = _DATA_FOLDER_PATH / "stooq_data" / file
    data = pd.read_csv(
        data_path,
        sep=",",
        decimal=".",
    )
    data.columns = [c.lower() for c in data.columns]
    data["date"] = pd.to_datetime(data["date"])
    data = data.set_index("date")
    data.columns = pd.MultiIndex.from_product([
        [ticker],
        list(data.columns),
    ], names=["ticker", "variable"])
    return data


def _extract_stooq_datas(file_to_ticker: dict[str, str]) -> pd.DataFrame:
    datas: list[pd.DataFrame] = []
    for file, ticker in file_to_ticker.items():
        datas.append(_extract_stooq_data(file=file, ticker=ticker))
    data: pd.DataFrame = reduce(
        lambda l_, r_: pd.merge(
            left=l_,
            right=r_,
            left_index=True,
            right_index=True,
            how="outer"
        ),
        datas
    )
    data = data.reset_index(drop=False).set_index("date")
    data = data["2005-01-01":"2024-12-31"]
    data = data.ffill().bfill()
    return data


def _setup_pl_banking_stocks() -> None:
    pl_banking_stocks_file_to_ticker: dict[str, str] = {
        "bhw_d.csv": "citi",
        "bos_d.csv": "bos",
        "ing_d.csv": "ing",
        "mbk_d.csv": "mbank",
        "mil_d.csv": "mil",
        "peo_d.csv": "pekao",
        "pko_d.csv": "pkobp",
        "spl_d.csv": "santander"
    }
    data: pd.DataFrame = _extract_stooq_datas(
        file_to_ticker=pl_banking_stocks_file_to_ticker
    )
    data.to_parquet(_DATA_FOLDER_PATH / "pl_banking_stocks.parquet")


if __name__ == "__main__":
    _setup_pl_banking_stocks()
