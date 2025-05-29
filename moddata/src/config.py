"""Stores pydantic-style configuration classes.

These are mainly bundles of values used not to clutter __init__-s
"""

from typing import Optional, TypeAlias

from pydantic import BaseModel, ConfigDict

from moddata.src.constants import EncodingAndScalingModelType

__all__ = [
    "BankchurnTransformerConfig",
    "BankchurnPipelineConfig"
]


class BankchurnTransformerConfig(BaseModel):
    """
    train_size: parameter passed to the train_test_split method
    used to create train and test datasets
    random_state: analogous to train_size
    encoding_and_scaling_model_type: Literal, defines what type of
    model data should be prepared for
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)

    train_size: float | int
    random_state: Optional[int] = None,
    encoding_and_scaling_model_type: Optional[EncodingAndScalingModelType]


BankchurnPipelineConfig: TypeAlias = BankchurnTransformerConfig
