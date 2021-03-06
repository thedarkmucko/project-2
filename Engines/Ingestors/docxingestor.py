import docx
from .interface_ingestor import IngestorInterface
from ..QuoteEngine.Quote import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        if ext in DocxIngestor.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path):

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                a_quote = QuoteModel(parse[0], parse[1])
                quotes.append(a_quote)

        return quotes
