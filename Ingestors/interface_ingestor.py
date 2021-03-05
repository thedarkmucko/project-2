from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    @abstractmethod
    def can_ingest(cls, path) -> bool:
        pass

    @abstractmethod
    def parse(cls, path):
        pass
