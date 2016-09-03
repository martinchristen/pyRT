"""
This is the geometric object sphere

(renderable object)
"""

from ..geometry import Shape
from ..math import Ray, HitRecord


class Sphere(Shape):
    """The Sphere class for raytracing spheres"""

    def __init__(self):
        Shape.__init__(self, "Sphere")
        print("[init] sphere")

    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        """
        :param ray: the ray to check hit
        :param tmin: tmin to test intersection
        :param tmax: tmax to test intersection
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        """
        pass

    def hitShadow(self, ray: Ray) -> bool:
        """
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        """
        pass
