from typing import List

from .ingestor import IngestorInterface
from ..QuoteEngine.quote import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def can_ingest(cls, path) -> bool:
        return super().can_ingest(path)

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes: list[QuoteModel] = []
        with open(path, mode="r", newline='\n') as data:
            line = data.readline()
            quote, author = line.split('-')
            a_quote = QuoteModel(quote.strip(), author.strip())
            quotes.append(a_quote)

        return quotes
