"""
This is the abstract Light.

Override if you implement your own light.
"""

#from abc import abstractmethod
from ..math import Vec3
from ..scene import Scene


class Light(object):

    """Base Light Class"""

    def __init__(self, name="UNKNOWN LIGHT"):
        """
        Base Constructor

        :param name: Name of Light type, for example "PointLight".
        """
        self.name = name
        self.position = Vec3(0.,0.,0.)
