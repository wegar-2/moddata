from typing import Any, Protocol


class Pipeline(Protocol):

    def run(self) -> Any:
        pass
    