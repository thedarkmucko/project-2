from typing import List
import subprocess
from . import ingestor
from ..QuoteEngine.quote import QuoteModel


class PDFIngestor(ingestor.IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path) -> bool:
        return super().can_ingest(path)

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes: list[QuoteModel] = []
        cmd = ["pdftotxt", path]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        
        output, _ = process.communicate()
        output = output.split('\n')

        for item in output:
            quote, author = item.split('-')
            a_quote = QuoteModel(quote, author)
            quotes.append(a_quote)

        return quotes
