""""
This file contains all bounding box realated stuff

The main class is "BBox"
"""

from .shape import Shape
from ..math import Vec3, Ray, HitRecord
from ..math.vecops import *



class BBox(Shape):
    """
    This class represents an axis aligned bounding box.
    """
    def __init__(self, vmin: Vec3, vmax):
        """

        :param vmin: minimum coord of bbox
        :param vmax: maximum coord of bbox
        """
        self.min = vmin
        self.max = vmax
        self.extent = self.max - self.min

    def __setitem__(self, key, value):
        assert type(value) is Vec3, "value is not a Vec3"

        if key == 0:
            self.min = value
        elif key == 1:
            self.max = value
        else:
            raise IndexError("Can only set index 0 (min) and index 1 (max)")

    def __getitem__(self, key):
        if key == 0:
            return self.min
        elif key == 1:
            return self.max
        else:
            raise IndexError("Can only get index 0 (min) and index 1 (max)")

        pass

    def __str__(self):
        return "BBOX: " + str(self.min) + "-" + str(self.max)

    def maxComponent(self):
        """
        Return the max component of bounding box
        
        :return: max component (x=0, y=1, z=2)
        """
        r = 0
        if self.extent.y > self.extent.x:
            r = 1
        if self.extent.z > self.extent.y:
            r = 2
        return r

    def expandPoint(self, pt: Vec3):
        """
        Expands the bounding box by a point (represented as Vec3)

        :param pt: point to expand bounding box
        """
        self.min = min3(self.min, pt)
        self.max = max3(self.max, pt)
        self.extent = self.max - self.min

    def expand(self, bbox):
        """
        Expands the bounding box by another box

        :param bbox: bounding box to expand
        """
        self.min = min3(self.min, bbox.min)
        self.max = max3(self.max, bbox.max)
        self.extent = self.max - self.min

    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        tmin = (self[ray.sign[0]].x - ray.start.x) * ray.invdir.x
        tmax = (self[1 - ray.sign[0]].x - ray.start.x) * ray.invdir.x
        tymin = (self[ray.sign[1]].y - ray.start.y) * ray.invdir.y
        tymax = (self[1 - ray.sign[1]].y - ray.start.y) * ray.invdir.y
        tzmin = (self[ray.sign[2]].z - ray.start.z) * ray.invdir.z
        tzmax = (self[1 - ray.sign[2]].z - ray.start.z) * ray.invdir.z
        tmin = max(max(tmin, tymin), tzmin)
        tmax = min(min(tmax, tymax), tzmax)
        tmin = (self[ray.sign[0]].x - ray.start.x) * ray.invdir.x

        if tmin > tmax:
            return False

        hitrecord.t = tmin
        hitrecord.point = ray.start + ray.direction * tmin
        return True

    def hitShadow(self, ray: Ray) -> bool:
        tmin = (self[ray.sign[0]].x - ray.start.x) * ray.invdir.x
        tmax = (self[1 - ray.sign[0]].x - ray.start.x) * ray.invdir.x
        tymin = (self[ray.sign[1]].y - ray.start.y) * ray.invdir.y
        tymax = (self[1 - ray.sign[1]].y - ray.start.y) * ray.invdir.y
        tzmin = (self[ray.sign[2]].z - ray.start.z) * ray.invdir.z
        tzmax = (self[1 - ray.sign[2]].z - ray.start.z) * ray.invdir.z
        tmin = max(max(tmin, tymin), tzmin)
        tmax = min(min(tmax, tymax), tzmax)
        tmin = (self[ray.sign[0]].x - ray.start.x) * ray.invdir.x

        return tmin < tmax


    def surfaceArea(self) -> float:
        return 2. * (self.extent.x * self.extent.z +
                    self.extent.x * self.extent.y +
                    self.extent.y * self.extent.z)

