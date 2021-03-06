from PIL import Image, UnidentifiedImageError, ImageDraw, ImageFont
from random import randint

def resize_image(_in: str, _width: int):
    """resize an image to max width 500px and height ratio-ed"""
    try:
        img = Image.open(_in)
    except UnidentifiedImageError:
        print("failed to open image")

    img_width, img_height = img.size

    output_file = randint(100000,200000)
    if img_width > 500:
        width = _width
        ratio = width / img_width
        height = int(ratio * float(img_height))
        img = img.resize((width, height), Image.NEAREST)
        img.save(f"./Engines/tmp/{output_file}.jpg")
    else:
        img.save(f"./Engines/tmp/{output_file}.jpg")

    return f"./Engines/tmp/{output_file}.jpg"


def fill_text(path: str, body: str, author: str):
    try:
        img = Image.open(path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/OpenSans-Regular.ttf', size=20)
        message = '\"'+ body + '\", said ' + author
        draw.text((10, 30), message, font=font, fill='red')
        img.save("./Engines/tmp/printme.jpeg")
    except Exception as e:
        print("Exception caught: ",e)

    return "./Engines/tmp/printme.jpg"


def make_housekeeping(path):
    from pathlib import Path
    import os

    _path = Path(path).resolve()
    os.chdir(_path)
    for child in _path.iterdir():
        child.unlink(missing_ok=True)
    os.chdir('../..')


class MemeEngine:
    @staticmethod
    def make_meme(img, body: str, author: str, width=500):
        make_housekeeping("./Engines/tmp")
        resized_image = resize_image(img, width)
        outfile = fill_text(resized_image, body, author)
        return outfile

