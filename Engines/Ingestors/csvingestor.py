import pandas
from .interface_ingestor import IngestorInterface
from ..QuoteEngine.Quote import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        if ext in CSVIngestor.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path):
        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            a_quote = QuoteModel(row['body'], row['author'])
            quotes.append(a_quote)

        return quotes
