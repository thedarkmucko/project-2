from .interface_ingestor import IngestorInterface


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
            lines = data.readlines()

        content = [line.strip('\n') for line in lines]

        for item in content:
            _quote, _author = item.split('-')
            print(_quote, _author)
            a_quote = QuoteModel(_quote.strip(), _author.strip())
            print(a_quote)
            quotes.append(a_quote)

        return quotes
