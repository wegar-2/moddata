from pathlib import Path
import shutil
from typing import Literal, TypeAlias

import importlib.resources as resources
import kagglehub
import pandas as pd

__all__ = [
    "load_data"
]

Dataset: TypeAlias = Literal[
    "bankchurn",
    "btc",
    "pl_banking_stocks"
]


def _load_bankchurn() -> pd.DataFrame:
    with (
        resources.files('moddata.data').joinpath('bankchurn.csv').open('r')
        as f
    ):
        return pd.read_csv(
            f,
            decimal=".",
            sep=",",
            header=0,
            index_col=False
        )


def _load_btc():
    path: Path = Path(kagglehub.dataset_download("prasoonkottarathil/btcinusd"))
    datas: list[pd.DataFrame] = []
    for p in path.glob("*min.csv"):
        datas.append(
            pd.read_csv(
                p,
                sep=",",
                decimal=".",
                usecols=[
                    "date", "open", "high", "low", "close", "Volume BTC",
                    "Volume USD"
                ],
                parse_dates=["date"]
            )
        )
    data: pd.DataFrame = pd.concat(datas, axis=0)
    data = data.rename(columns={
        "date": "dt", "Volume BTC": "vol_btc", "Volume USD": "vol_usd"
    })
    data = data.sort_values("dt")
    data = data.set_index("dt")
    data = data[:"2021-12-31 23:59:00"]
    shutil.rmtree(path=path)
    return data


def _load_pl_banking_stocks() -> pd.DataFrame:
    with (
        resources.files('moddata.data').joinpath('pl_banking_stocks.parquet')
        as f
    ):
        return pd.read_parquet(f)


def load_data(dataset: Dataset) -> pd.DataFrame | None:
    if dataset == "bankchurn":
        return _load_bankchurn()
    elif dataset == "btc":
        return _load_btc()
    elif dataset == "pl_banking_stocks":
        return _load_pl_banking_stocks()
    else:
        raise ValueError(
            f"Encountered invalid dataset name: {dataset}"
        )


if __name__ == "__main__":
    _load_btc()
