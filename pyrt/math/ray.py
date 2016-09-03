from .vec3 import *


class HitRecord(object):
    def __init__(self):
        self.point = None  # hit point
        self.normal = None  # hit normal (shading normal!)
        self.normal_g = None  # hit normal (geometric normal!)
        self.texcoord = None  # texture coordinate at hit point
        self.t = None  # intersection parameter of line
        self.obj = None  # hit object/geometry or None if not applicable


class Ray(object):
    def __init__(self, start: Vec3, direction: Vec3) -> None:
        if type(start) != Vec3 or type(direction) != Vec3:
            print("Error: start and direction must be Vec3")
            return

        self.start = start  # todo: Property
        self.direction = direction  # todo: Property

        # self.invdir = Vec3(1.0 / self.direction.x, 1.0 / self.direction.y, 1.0 / self.direction.z)
        # self.sign = sign(self.invdir)
