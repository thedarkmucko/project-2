from abc import ABC
from typing import List
from ..QuoteEngine.Quote import QuoteModel


class IngestorInterface(ABC):
    @classmethod
    def can_ingest(cls, path) -> bool:
        pass

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        pass
