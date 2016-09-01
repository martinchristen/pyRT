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

    #-------------------------------------------------------------------------------------------------------------------
    def area(self) -> float:
        '''
        Calculate area of triangle
        :return: area
        '''
        return cross3(self.b.position-self.a.position,
               self.c.position-self.a.position).length() / 2.0
    #-------------------------------------------------------------------------------------------------------------------
    def toBarycentric(self, p : Vec3) -> Vec3:
        '''
        Calculate barycentric coordinate of point p
        :param P: the input point (cartesian)
        :return: barycentric coordinate
        '''
        abc = triangleArea(self.a.position, self.b.position, self.c.position)
        pbc = triangleArea(p, self.b.position, self.c.position)
        apc = triangleArea(self.a.position, p, self.c.position)

        if abc == 0.0:
            return Vec3(0,0,0)

        x = pbc/abc
        y = apc/abc
        return Vec3(x, y, 1.0 - x - y)

    #-------------------------------------------------------------------------------------------------------------------
    def fromBarycentric(self, b : Vec3) -> Vec3:
        '''
        Calculate cartesian coordinate from barycentric coordinate
        :param b: barycentric coordinate
        :return: cartesian coordinate
        '''
        return self.a.position * b.x + self.b.position * b.y + self.c.position * b.z
    #-------------------------------------------------------------------------------------------------------------------
    def circumradius(self) -> float:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()

        s = (a + b + c) / 2.0 # semiperimeter
        z = a*b*c
        n = 4.0 * math.sqrt(s*(a+b-s)*(a+c-s)*(b+c-s))
        if n==0.0:
            return 0.0
        return z/n
    #-------------------------------------------------------------------------------------------------------------------
    def inradius(self) -> float:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()
        s = (a + b + c) / 2.0
        if s == 0.0:
            return 0.0
        return math.sqrt((s - a) * (s - b) * (s - c) / s)

    #-------------------------------------------------------------------------------------------------------------------
    def circumcenter(self) -> Vec3:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()
        q = a * a * (-a * a + b * b + c * c)
        w = b * b * (a * a - b * b + c * c)
        e = c * c * (a * a + b * b - c * c)
        n = q+w+e
        if n==0.0:
            return Vec3(0,0,0)
        return self.fromBarycentric(Vec3(q/n,w/n,e/n))

    #-------------------------------------------------------------------------------------------------------------------
    def incenter(self) -> Vec3:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()
        n = a+b+c
        if n==0.0:
            return Vec3(0,0,0)

        return self.fromBarycentric(Vec3(a/n, b/n, c/n))
    #-------------------------------------------------------------------------------------------------------------------
    def centroid(self) -> Vec3:
        return (self.a.position + self.b.position + self.c.position) / 3.0
    #-------------------------------------------------------------------------------------------------------------------
    def calcTexcoord(self, p : Vec3) -> Vec2:
        '''
        Returns texture-coordinate at cartesian position p
        :param p:
        :return: returns
        '''
        pb = self.toBarycentric(p)
        u = self.a.texcoord.x * pb.x + self.b.texcoord.x * pb.y + self.c.texcoord.x * pb.z
        v = self.a.texcoord.y * pb.x + self.b.texcoord.y * pb.y + self.c.texcoord.y * pb.z
        return Vec2(u,v)
    #-------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------
# Utility functions related to triangles

def triangleArea(a: Vec3,b: Vec3,c: Vec3) -> float:
    '''
    Calculate area of triangle
    :return: area
    '''
    return cross3(b - a, c - a).length() / 2.0


