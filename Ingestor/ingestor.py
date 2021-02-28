from abc import abstractmethod
from typing import List

from src.Ingestor.csvingestor import CSVIngestor
from src.Ingestor.docxingestor import DocxIngestor
from src.Ingestor.interface_ingestor import IngestorInterface
from src.Ingestor.pdfingestor import PDFIngestor
from src.Ingestor.txtingestor import TXTIngestor
from src.QuoteEngine.quote import QuoteModel


class Ingestor(IngestorInterface):
    allowed_extensions = []
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def can_ingest(cls, path) -> bool:
        for ingest in cls.ingestors:
            if ingest.can_ingest(path):
                return True
            else:
                return False

    @abstractmethod
    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        pass
