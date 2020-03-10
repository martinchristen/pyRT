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

    def __init__(self, position: Vec3, direction: Vec3, angle: float, coef:float) -> None:
        """
        Constructor:
        param position: position of the light
        param direction: direction of the light
        param angle: light angle around direction(0 - 180)
        """
        Light.__init__(self, coef, "SpotLight")
        self.position = position
        self.direction = direction
        self.angle = angle
        self.dir_ray = Ray(position, self.direction - self.position)

    def intensity(self, shadowray):
        """
        Point intensity calculation:
        param shadowray: ray from light to hitrecord point
        """
        fs = 0.0
        radians = np.arccos(self.direction.dot(-shadowray.direction) / (self.direction.length() * shadowray.direction.length()))
        if(np.degrees(radians) <= self.angle):
            fs += 1 - np.degrees(radians) / (1.5 * self.angle)
        return fs * self.coef


