from pathlib import Path

import numpy as np
import pandas as pd

__all__ = ["Spx1901To2025Pipeline"]


class Spx1901To2025Pipeline:

    def run(self):
        data = pd.read_csv(
            str(
                Path(__file__).parent.parent / "data" / "stooq_data" /
                "spx_1901-2025.csv"
            ),
            sep=",", decimal="."
        )
        data.columns = [c.lower() for c in data.columns]
        data["date"] = data["date"].astype("datetime64[us]")
        data.loc[
            data["date"] <= pd.Timestamp("1950-01-01"),
            "volume"
        ] = np.nan
        data = data.set_index("date")

        data.to_parquet(
            str(
                Path(__file__).parent.parent / "data" /
                "spx_1901-2025.parquet"
            )
        )


if __name__ == "__main__":
    Spx1901To2025Pipeline().run()
