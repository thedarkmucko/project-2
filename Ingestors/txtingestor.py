from .interface_ingestor import IngestorInterface


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def can_ingest(cls, path) -> bool:
        return super().can_ingest(path)

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, mode="r", newline='\n') as data:
            line = data.readline()
            quote, author = line.split('-')
            from meme_proj.QuoteEngine.quote import QuoteModel
            a_quote = QuoteModel(quote.strip(), author.strip())
            quotes.append(a_quote)

        return quotes
