from pathlib import Path
from typing import Literal

import pandas as pd

__all__ = [
    "load_data"
]


def _load_bankchurn() -> pd.DataFrame:
    return pd.read_csv(
        Path(__file__).parent / "data" / "bankchurn.csv",
        decimal=".",
        sep=",",
        header=0,
        index_col=False
    )


def load_data(
        dataset: Literal["bankchurn"]
) -> pd.DataFrame | None:
    if dataset == "bankchurn":
        return _load_bankchurn()
    else:
        raise ValueError(
            f"Encountered invalid dataset name: {dataset}"
        )
