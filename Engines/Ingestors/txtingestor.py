from .interface_ingestor import IngestorInterface
from ..QuoteEngine.Quote import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    def can_ingest(path) -> bool:
        ext = path.split('.')[-1]
        if ext in TXTIngestor.allowed_extensions:
            print("returning True")
            return True
        return False

    def parse(path):
        quotes = []
        with open(path, mode="r") as data:
            lines = data.readlines()

        content = [line.strip('\n') for line in lines]

        for item in content:
            _quote, _author = item.split('-')
            a_quote = QuoteModel(_quote.strip(), _author.strip())
            quotes.append(a_quote)

        print("==================")
        for i in quotes:
            print(i)
        print("==================")
        return quotes
