""""
This file contains all bounding box realated stuff

The main class is "BBox"
"""

from ..math import Vec3, Ray, HitRecord
from ..math.vecops import *
from ..geometry import Shape

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

    def expand(self, bbox: BBox):
        """
        Expands the bounding box by another box

        :param bbox: bounding box to expand
        """
        self.min = min3(self.min, bbox.min)
        self.max = max3(self.max, bbox.max)
        self.extent = self.max - self.min

    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        return False # TODO: Ray Box intersection

    def hitShadow(self, ray: Ray) -> bool:
        return False # TODO: Ray Box intersection

    def surfaceArea(self) -> float:
        return 2. * (self.extent.x * self.extent.z +
                     self.extent.x * self.extent.y +
                     self.extent.y * self.extent.z)

