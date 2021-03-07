import os
import random
from Engines.MemeEngine.memeEngine import MemeEngine
from Engines.Ingestors import Ingestor
from Engines.QuoteEngine.Quote import QuoteModel
from typing import List


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    quotes = []
    if path is None:
        images = "./Engines/_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)

    else:
        img = path[0]

    if body is None:
        quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                       './Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                       './Engines/_data/DogQuotes/DogQuotesPDF.pdf',
                       './Engines/_data/DogQuotes/DogQuotesCSV.csv']

        for f in quote_files:
            print("processing ", f)
            quotes.extend(Ingestor.parse(f))

        try:
            _quote = random.choice(quotes)
            path = MemeEngine.make_meme(img, _quote.body, _quote.author)
            return path
        except Exception as e:
            print("Error caught:", e)

    path = MemeEngine.make_meme(path, body, author)
    return path


def make_parser():
    import argparse
    parser = argparse.ArgumentParser("An argument parser for meme generator")
    parser.add_argument('--path', help="Path to a picture")
    parser.add_argument('--body', help="Quote text to be added to a picture")
    parser.add_argument('--author', help="Author of the quote")

    parsed = parser.parse_args()
    return parsed


if __name__ == "__main__":
    args = make_parser()
    print(generate_meme(args.path, args.body, args.author))
