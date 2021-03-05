import os
import random

import Ingestors
import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestors.ingestor.Ingestor.parse(f))

        _quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        _quote = MemeEngine.generate_meme(body, author)

    path = MemeEngine.make_meme(img, _quote.body, _quote.author)
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
    print(__name__)
    print(dir(MemeEngine))
    """args = make_parser()
    print(generate_meme(args.path, args.body, args.author))"""
