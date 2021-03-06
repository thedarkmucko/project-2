from typing import List
import subprocess
from .interface_ingestor import IngestorInterface


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path) -> bool:
        return super().can_ingest(cls,path=path)

    @classmethod
    def parse(cls, path):
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        cmd = ["pdftotxt", path]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        
        output, _ = process.communicate()
        output = output.splitlines()

        for item in output:
            quote, author = item.split('-')
            a_quote = quote.QuoteModel(quote, author)
            quotes.append(a_quote)

        return quotes
