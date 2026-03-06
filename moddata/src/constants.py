"""Contains definition of various package-wide constants.

EncodingAndScalingModelType - defines groups of models for which the
data is to be prepared for (needed to pick right transformations)
"""


from typing import TypeAlias, Literal, Final

import pandas as pd

EncodingAndScalingModelType: TypeAlias = Literal[
    "tree_like",
    "other",
    "MICRO_SECS_PER_DAY"
]

XyDataFrames: TypeAlias = tuple[pd.DataFrame, pd.DataFrame]

TrainTestXyDataFrames: TypeAlias = (
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
)

MICRO_SECS_PER_DAY: Final[int] = 24 * 60 * 60 * 1_000
