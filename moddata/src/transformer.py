from typing import Any, Protocol, TypeAlias

import pandas as pd

DataIn: TypeAlias = pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]


class Transformer(Protocol):

    def transform(
            self,
            data: pd.DataFrame,
            **kwargs
    ) -> Any:
        pass
