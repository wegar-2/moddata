"""Contains definition of various package-wide constants.

EncodingAndScalingModelType - defines groups of models for which the
data is to be prepared for (needed to pick right transformations)
"""


from typing import TypeAlias, Literal

import pandas as pd

EncodingAndScalingModelType: TypeAlias = Literal[
    "tree_like",
    "other"
]

XyDataFrames: TypeAlias = tuple[pd.DataFrame, pd.DataFrame]

TrainTestXyDataFrames: TypeAlias = (
    tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
)
