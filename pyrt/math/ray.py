"""
Ray - Handling rays for ray tracing

This is the code for handling 3D rays
"""

from .vec3 import Vec3
from .vecops import sign3


class HitRecord(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.t = None  # intersection parameter of line
        self.point = None  # hit point (in world coordinates)
        self.normal = None  # hit normal (shading normal)
        self.normal_g = None  # hit normal (geometric normal)
        self.color = None  # interpolated color
        self.material = None  # Material
        self.texcoord = None  # texture coordinate at hit point
        self.obj = None  # hit object/geometry or None if not applicable

    def copy(self):
        n = HitRecord()
        n.t = self.t
        if self.point is not None:
            n.point = self.point.copy()
        if self.normal is not None:
            n.normal = self.normal.copy()
        if self.normal_g is not None:
            n.normal_g = self.normal_g.copy()
        if self.color is not None:
            n.color = self.color.copy()

        n.material = self.material # Material is still reference!

        if self.texcoord is not None:
            n.texcoord = self.texcoord.copy()
        n.obj = self.obj

        return n


#-----------------------------------------------------------------------------------------------------------------------


class Ray(object):
    def __init__(self, start: Vec3, direction: Vec3) -> None:
        if type(start) != Vec3 or type(direction) != Vec3:
            print("Error: start and direction must be Vec3")
            return

        self.start = start
        self.direction = direction
        self.invdir = Vec3(1e20, 1e20, 1e20)  # TODO: make this IEEE 754 compliant
        if abs(self.direction.x)>0.000000000001:
            self.invdir.x = 1.0 / self.direction.x
        if abs(self.direction.y)>0.000000000001:
            self.invdir.y = 1.0 / self.direction.y
        if abs(self.direction.z)>0.000000000001:
            self.invdir.z = 1.0 / self.direction.z

        self.sign = [0,0,0]
        if self.invdir.x < 0:
            self.sign[0] = 1
        if self.invdir.y < 0:
            self.sign[1] = 1
        if self.invdir.z < 0:
            self.sign[2] = 1

    def copy(self):
        """
        Create a copy of the reay

        :return: copy of ray
        """
        return Ray(self.start.copy(), self.direction.copy())
