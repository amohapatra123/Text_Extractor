# import packages

from typing import IO
from sys import argv
from PIL import Image
import pytesseract as p


def extract(image_object):
    return p.image_to_string(Image.open(image_object))


