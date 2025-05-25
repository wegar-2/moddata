from typing import Any, Protocol

import pandas as pd


class Transformer(Protocol):

    def transform(self, data: pd.DataFrame, **kwargs) -> Any:
        pass
