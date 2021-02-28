from typing import List
import docx
from . import ingestor
from src.QuoteEngine.quote import QuoteModel


class DocxIngestor(ingestor.IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path) -> bool:
        return super().can_ingest(path)

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
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
