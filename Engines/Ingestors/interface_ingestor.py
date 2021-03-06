from abc import ABC


class IngestorInterface(ABC):
    @classmethod
    def can_ingest(cls, path) -> bool:
        pass

    @classmethod
    def parse(cls, path):
        pass
