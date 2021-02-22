"""
This is the geometric shape description

(renderable object)
"""

from abc import abstractmethod, abstractclassmethod
from ..math import Ray, HitRecord, Vec2, Vec3
import uuid


class Shape(object):
    """This is the base class for all geometries"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.material = None
        self.id = str(uuid.uuid4())

    @abstractmethod
    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        """
        :param ray: the ray to check hit
        :param tmin: tmin to test intersection
        :param tmax: tmax to test intersection
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        """
        pass

    @abstractmethod
    def hitShadow(self, ray: Ray) -> bool:         # TODO: This method should be renamed to "hitTest".
        """
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        """
        pass


    @abstractmethod
    def getBBox(self):
        """
        Retrieve axis aligned bounding box of the shape


        :return: bounding box
        """
        return BBox(Vec3(0,0,0), Vec3(1,1,1))

    @abstractmethod
    def getCentroid(self) -> Vec3:
        """
        Retrieve centroid of shape
        :return:
        """
        return Vec3(0,0,0)

    @abstractmethod
    def getSurfaceArea(self) -> float:
        """
        Retrieve Surface area of Triangle

        :return: surface area
        """
        return 0


        ####################
        # TODO: MATERIAL
        #       handle shape material (color, textures, ...)
        ####################
