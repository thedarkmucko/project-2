class QuoteModel:
    def __init__(self, quote: str, author: str):
        self._quote = quote
        self._author = author

    @property
    def body(self):
        return self._quote

    @property
    def author(self):
        return self.author


    def __str__(self):
        return f"{self._quote} - {self._author}"
