"""
This is the geometric object trianglemesh

(renderable object)
"""

from ..geometry import Shape, Vertex
from ..material import PhongMaterial
from ..math import *


class TriangleMesh(Shape):
    def __init__(self):
        Shape.__init__(self, "TriangleMesh")


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


    def getBBox(self):
        """
        Retrieve axis aligned bounding box of the triangle mesh


        :return: bounding box
        """
        return BBox(Vec3(0,0,0), Vec3(1,1,1))

    def getCentroid(self) -> Vec3:
        """
        Retrieve centroid of triangle mesh
        :return:
        """
        return Vec3(0,0,0)

    def getSurfaceArea(self) -> float:
        """
        Retrieve Surface area of the triangle mesh (area of all triangles)

        :return: surface area
        """
        return 0