"""Contains definition of various package-wide constants.

EncodingAndScalingModelType - defines groups of models for which the
data is to be prepared for (needed to pick right transformations)
"""


from typing import TypeAlias, Literal


EncodingAndScalingModelType: TypeAlias = Literal[
    "tree_like",
    "other"
]