"""
Texture

"""
from PIL import Image
from numpy import asarray
from ..math import Vec2, Vec3


class Texture:

    """Texture Class"""

    def __init__(self, path: str):
        image = Image.open(path)
        self._pixels = asarray(image.getdata())
        self._w, self._h = image.size

    def color(self, u: float, v: float):
        rgb = self._pixels[int(v * self._h) * self._w + int(u * self._w)]
        return Vec3(float(rgb[0]) / 255.0, float(rgb[1]) / 255.0, float(rgb[2]) / 255.0)


    def color(self, uv: Vec2):
        rgb = self._pixels[int(uv.y * self._h) * self._w + int(uv.x * self._w)]
        return Vec3(float(rgb[0]) / 255.0, float(rgb[1]) / 255.0, float(rgb[2]) / 255.0)
