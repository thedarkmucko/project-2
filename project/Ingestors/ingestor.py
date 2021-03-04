from .csvingestor import CSVIngestor
from .docxingestor import DocxIngestor
from .interface_ingestor import IngestorInterface
from .pdfingestor import PDFIngestor
from .txtingestor import TXTIngestor


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
