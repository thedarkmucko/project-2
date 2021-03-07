from flask import Flask, render_template
from Engines.MemeEngine.memeEngine import MemeEngine
from Engines.Ingestors import Ingestor
import os, random

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'Engines/tmp')
print(template_path, static_path)
app = Flask(__name__, template_folder=template_path, static_folder=static_path)


# finished setup()
def setup():
    """ Load all resources """

    all_quotes = []

    quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                   './Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                   './Engines/_data/DogQuotes/DogQuotesPDF.pdf',
                   './Engines/_data/DogQuotes/DogQuotesCSV.csv']

    for f in quote_files:
        all_quotes.extend(Ingestor.parse(f))

    images = "./Engines/_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]

    return all_quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    out = MemeEngine.make_meme(img, quote.body, quote.author)
    print(out)
    return render_template('meme.html', path=out)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
