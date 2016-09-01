from ..geometry import *
from ..math import *


class Triangle(Shape):
    def __init__(self, a: Vertex, b: Vertex, c: Vertex):
        if type(a) != Vertex or type(b) != Vertex or type(c) != Vertex:
            raise ValueError("Please initialize Triangle with 3x Vertex")

        Shape.__init__(self)

        self.a = a
        self.b = b
        self.c = c

        print("[init] Triangle")
        print(str(self))


    def __str__(self):
        return "△ABC: Position[" + str(self.a.position) + ", " + str(self.b.position) + ", " + str(self.c.position) + "]"

    def area(self) -> float:
        pass

    def circumradius(self) -> float:
        pass

    def inradius(self) -> float:
        pass

    def circumcenter(self) -> Vec3:
        pass

    def incenter(self) -> Vec3:
        pass

    def centroid(self) -> Vec3:
        pass

    def hit(self, ray: Ray, tmin: float, tmax: float, hitrecord: HitRecord) -> bool:
        '''
        :param ray: the ray to check hit
        :param tmin: tmin to test intersection
        :param tmax: tmax to test intersection
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        '''
        pass

    def hitShadow(self, ray: Ray, tmin: float, tmax: float) -> bool:
        '''
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        '''
        pass

