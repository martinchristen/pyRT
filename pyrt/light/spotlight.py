"""
This is the definition for a spot light

A spot light emits light to one directions with some angle around it. 

"""
from .light import Light
from ..math import Vec3
from ..math import Ray
from ..renderer.rgbimage import *


class SpotLight(Light):

    """Class describing a spot light source"""

    def __init__(self, position: Vec3, direction: Vec3, p: int, a = 0.02, b = 0.1, c = 0) -> None:
        """
        Constructor:
        param position: position of the light
        param direction: direction of the light
        param p: controls how much the spotlight is focussed
        params a, b, c: quadratic equation coefficients for ad^2 + bd + c
        """
        Light.__init__(self,  "SpotLight")
        self.position = position
        self.direction = direction
        self.p = p
        self.dir_ray = Ray(position, self.direction - self.position)
        self.a = a
        self.b = b
        self.c = c

    def intensity(self, shadowray):
        """
        Point intensity calculation:
        param shadowray: ray from light to hitrecord point
        """

        d = shadowray.direction.length()
        f_att = np.clip(1 / (self.c + self.b * d + self.a * d * d), 0, 1)
        cos_angle = self.direction.dot(-shadowray.direction) / (self.direction.length() * shadowray.direction.length())
        return f_att * (cos_angle ** self.p)


