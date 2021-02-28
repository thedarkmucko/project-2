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
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
