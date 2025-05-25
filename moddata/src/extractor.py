from typing import Protocol


class Extractor(Protocol):

    def extract(self, *args, **kwargs):
        pass
    