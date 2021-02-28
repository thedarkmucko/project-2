from abc import abstractmethod
from typing import List

from ..Ingestor.csvingestor import CSVIngestor
from ..Ingestor.docxingestor import DocxIngestor
from ..Ingestor.interface_ingestor import IngestorInterface
from ..Ingestor.pdfingestor import PDFIngestor
from ..Ingestor.txtingestor import TXTIngestor
from ..QuoteEngine.quote import QuoteModel


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
