import subprocess
from .interface_ingestor import IngestorInterface
from ..QuoteEngine.Quote import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        if ext in PDFIngestor.allowed_extensions:
            return True
        return False

    @classmethod
    def parse(cls, path):
        quotes = []

        cmd = ["pdftotext", path]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        
        output, _ = process.communicate()
        output = output.splitlines()

        for item in output:
            quote, author = item.split('-')
            a_quote = QuoteModel(quote, author)
            quotes.append(a_quote)

        return quotes
