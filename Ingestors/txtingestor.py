from .interface_ingestor import IngestorInterface
from ..QuoteEngine.quote import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def can_ingest(cls, path) -> bool:
        print("Yes I can ingest", cls.allowed_extensions)
        return super().can_ingest(cls, path=path)

    @classmethod
    def parse(cls, path):
        print("parsing request", path)
        if cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, mode="r", newline='\n') as data:
            line = data.readline()
            _quote, _author = line.split('-')
            a_quote = QuoteModel(_quote.strip(), _author.strip())
            quotes.append(a_quote)
        print(quotes)
        return quotes
