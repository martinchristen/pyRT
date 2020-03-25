"""
This is the definition for a point light

A point light emits light to all directions. It can be somewhat compared to a light bulb.

"""
from .light import Light
from ..math import Vec3


class PointLight(Light):

    """Class describing a point light source"""

    def __init__(self, position: Vec3) -> None:
        """
        Constructor

        Not yet complete - params will change in near future!
        :param position: position of the light
        """
        Light.__init__(self, "PointLight")
        self.position = position



