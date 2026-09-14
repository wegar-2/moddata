from functools import reduce

import pandas as pd

from moddata.common.aliases import JoinStyle


class MergeStooqDataTransformer:

    def __init__(self, join_style: JoinStyle = "outer"):
        self._join_style: JoinStyle = join_style

    def transform(self, data: dict[str, pd.DataFrame]) -> pd.DataFrame:
        data: pd.DataFrame = reduce(
            lambda l_, r_: pd.merge(
                left=l_,
                right=r_,
                left_index=True,
                right_index=True,
                how=self._join_style # noqa
            ),
            data.values()
        )
        data = data.reset_index(drop=False).set_index("date")
        if self._join_style == "outer":
            data = data.ffill().bfill()
        return data
