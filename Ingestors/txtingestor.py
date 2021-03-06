from .interface_ingestor import IngestorInterface
from ..QuoteEngine import quote


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        if ext in cls.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path):
        print("parsing request", path)

        quotes = []
        with open(path, mode="r") as data:
            line = data.readline()
            _quote, _author = line.split('-')
            a_quote = quote.QuoteModel(_quote.strip(), _author.strip())
            print(a_quote)
            quotes.append(a_quote)

        return quotes
