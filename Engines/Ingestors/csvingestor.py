import pandas
from .interface_ingestor import IngestorInterface
from ..QuoteEngine.Quote import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def can_ingest(cls, path) -> bool:
        return super().can_ingest(path)

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes= []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            a_quote = QuoteModel(row['body'], row['author'])
            quotes.append(a_quote)

        return quotes