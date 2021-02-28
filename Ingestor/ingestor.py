from abc import abstractmethod

from ..Ingestor.csvingestor import CSVIngestor
from ..Ingestor.docxingestor import DocxIngestor
from ..Ingestor.interface_ingestor import IngestorInterface
from ..Ingestor.pdfingestor import PDFIngestor
from ..Ingestor.txtingestor import TXTIngestor


class Ingestor(IngestorInterface):
    allowed_extensions = []
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def can_ingest(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                ingestor.parse(path)

    @abstractmethod
    @classmethod
    def parse(cls, path):
        """will never be called"""
        pass
