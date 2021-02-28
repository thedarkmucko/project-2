import os
import random
import PIL
import pathlib

from . import Ingestor
from .QuoteEngine.quote import QuoteModel


def resize_image(path: str) -> pathlib.Path:
    """resize an image to max widht 500px and height ratio-ed"""
    try:
        img = PIL.Image.open(path)
    except PIL.UnidentifiedImageError:
        print("failed to open image")

    img_width, img_height = img.size
    if img_width > 500:
        width = 500
        ratio = width / img_width
        height = int(ratio * float(img_height))

    img = img.resize((width, height), PIL.Image.NEAREST)
    p = pathlib.Path.resolve(path).parent

    img.save(p / 'resized', "JPEG")
    return pathlib.Path(img)


def fill_text(path: str) -> pathlib.Path:
    pass


class MemeEngine(object):
    def __init__(self) -> pathlib.Path:
        pass

    @staticmethod
    def make_meme(img, body: str, author: str) -> str:
        """return a resized meme with body and text, path to this JPEG"""
        resized_image = resize_image(img)
        outfile = fill_text(resized_image)
        return outfile


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
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine()
    path = meme.make_meme(img, quote.body, quote.author)
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
