from .interface_ingestor import IngestorInterface
from ..QuoteEngine.Quote import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        if ext in TXTIngestor.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path):
        quotes = []
        with open(path, mode="r") as data:
            lines = data.readlines()

        content = [line.strip('\n') for line in lines]

        for item in content:
            _quote, _author = item.split('-')
            a_quote = QuoteModel(_quote.strip(), _author.strip())
            quotes.append(a_quote)

        return quotes
