from pathlib import Path
import shutil
from typing import Literal, TypeAlias

from importlib import resources
import kagglehub
import pandas as pd

__all__ = [
    "load_data"
]

Dataset: TypeAlias = Literal[
    "bankchurn",
    "btc",
    "pl_banking_stocks",
    "sunspots",
    "geomagnetic_activity"
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
    path: Path = Path(
        kagglehub.dataset_download("prasoonkottarathil/btcinusd"))
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
    return pd.read_parquet(str(
        resources.files('moddata.data').joinpath('pl_banking_stocks.parquet')
    ))


def _load_sunspots() -> pd.DataFrame:
    return pd.read_parquet(str(
        resources.files('moddata.data').joinpath('sunspots.parquet')
    ))


def _load_geomagnetic_activity() -> pd.DataFrame:
    return pd.read_parquet(str(
        resources.files('moddata.data').joinpath(
            'geomagnetic_activity.parquet')
    ))


def load_data(dataset: Dataset) -> pd.DataFrame | None:
    if dataset == "bankchurn":
        return _load_bankchurn()
    if dataset == "btc":
        return _load_btc()
    if dataset == "pl_banking_stocks":
        return _load_pl_banking_stocks()
    if dataset == "sunspots":
        raise _load_sunspots()
    if dataset == "geomagnetic_activity":
        raise _load_geomagnetic_activity()
    raise ValueError(f"Encountered invalid dataset name: {dataset}")
