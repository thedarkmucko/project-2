import docx
from .interface_ingestor import IngestorInterface
from ..QuoteEngine.Quote import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path):
        return super().can_ingest(path)

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                a_quote = QuoteModel(parse[0], parse[1])
                quotes.append(a_quote)

        return quotes