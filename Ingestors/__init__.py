from .docxingestor import DocxIngestor
from .csvingestor import CSVIngestor
from .pdfingestor import PDFIngestor
from .txtingestor import TXTIngestor
from .interface_ingestor import IngestorInterface


class Ingestor(IngestorInterface):
    allowed_extensions = ['txt','docx','pdf','txt']
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        print("returning", ext in cls.allowed_extensions)
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            print(ingestor)
            if ingestor.can_ingest(path=path):
                print("Yes, this ingestor can ingest")
                ingestor.parse(path=path)