"""
Texture

"""
from PIL import Image
from numpy import asarray
from ..math import Vec3


class Texture:

    """Texture Class"""

    def __init__(self, path: str):
        image = Image.open(path)
        self._pixels = asarray(image.getdata())
        self._w, self._h = image.size

    def color(self, u: float, v: float):
        rgb = self._pixels[int(v * self._h)][int(u * self._w)]
        return Vec3(rgb[0], rgb[1], rgb[2])
