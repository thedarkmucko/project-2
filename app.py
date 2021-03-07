from flask import Flask, render_template
from Engines.MemeEngine.memeEngine import MemeEngine
from Engines.Ingestors import Ingestor
import os, random
import requests as req

app = Flask(__name__, template_folder='./templates')


def setup():
    """ Load all resources """

    all_quotes = list()

    quote_files = ['./Engines/_data/DogQuotes/DogQuotesTXT.txt',
                   './Engines/_data/DogQuotes/DogQuotesDOCX.docx',
                   './Engines/_data/DogQuotes/DogQuotesPDF.pdf',
                   './Engines/_data/DogQuotes/DogQuotesCSV.csv']

    for f in quote_files:
        all_quotes.extend(Ingestor.parse(f))

    images = "./Engines/_data/photos/dog/"
    img_list = list()
    for root, dirs, files in os.walk(images):
        img_list = [os.path.join(root, name) for name in files]

    return all_quotes, img_list


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    output = MemeEngine.make_meme(img, quote.body, quote.author)
    return render_template('meme.j2', path=output)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.j2')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    from flask import request
    url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    r = req.get(url, allow_redirects=True)

    open('created.jpg', 'wb').write(r.content)
    path = MemeEngine.make_meme('created.jpg', body, author)
    os.unlink('created.jpg')

    return render_template('meme.j2', path=path)


if __name__ == "__main__":
    app.run()
