import pathlib
import PIL


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
    return pathlib.Path(p/'resized.jpeg')


def fill_text(path: str, body: str, author: str) -> pathlib.Path:
    img = PIL.Image.open(path)
    draw = PIL.ImageDraw.Draw(img)
    font = PIL.ImageFont.truetype('./fonts/OpenSans-Regular.ttf', size=20)
    message = body + ': ' + author
    draw.text((10, 30), message, font=font, fill='white')

    p = pathlib.Path.resolve(path).parent

    img.save(p / 'texted', "JPEG")
    return pathlib.Path(p/'texted.jpeg')


class MemeEngine(object):

    @staticmethod
    def make_meme(img, body: str, author: str) -> str:
        """return a resized meme with body and text, path to this JPEG"""
        resized_image = resize_image(img)
        outfile = fill_text(resized_image, body, author)
        return outfile

