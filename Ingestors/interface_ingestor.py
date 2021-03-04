from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    @abstractmethod
    @classmethod
    def can_ingest(cls, path) -> bool:
        pass

    @abstractmethod
    @classmethod
    def parse(cls, path):
        """will never be called"""
        pass
