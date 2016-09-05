"""
Base Material

This is the description of a base material. If you want to add new materials, inherit from this class.
"""

from abc import abstractmethod
from ..math import Vec3, Ray, HitRecord
from ..camera import Camera


class Material(object):

    """Base Material Class"""

    def __init__(self, color: Vec3 = Vec3(0.,0.,0.), shininess: float = 0.0, reflectivity: float = 0.5, refraction: float = 1.0):
        self.color = color
        self.shininess = shininess
        self.reflectivity = reflectivity
        """
        some important refractive indices:

        vacuum: 1.0
        water: 1.33
        diamond: 2.4
        more indices can be found at: https://en.wikipedia.org/wiki/List_of_refractive_indices

        Also check the "refract3" function in math/vecops.py
        """
        self.refraction = refraction

    @abstractmethod
    def shade(self, camera: Camera, ray: Ray, hitrecord: HitRecord,  lights: list) -> Vec3:
        """
        Shade method

        This is the base shade method.
        """
        pass

