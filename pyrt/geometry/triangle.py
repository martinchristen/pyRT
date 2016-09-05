"""
This is the geometric object triangle

(renderable object)
"""

from ..geometry import Shape, Vertex
from ..material import PhongMaterial
from ..math import *


class Triangle(Shape):

    """Triangle class for raytracing"""

    def __init__(self, a: Vertex, b: Vertex, c: Vertex, material=PhongMaterial()):
        if type(a) != Vertex or type(b) != Vertex or type(c) != Vertex:
            raise ValueError("Please initialize Triangle with 3x Vertex")
        Shape.__init__(self, "Triangle")
        self.a = a
        self.b = b
        self.c = c
        self.material = material
        self.EPSILON = 0.000001

    def __str__(self):
        return "△ABC: Position[" + str(self.a.position) + ", " + str(self.b.position) + ", " + str(
            self.c.position) + "]"

    # ------------------------------------------------------------------------------------------------------------------
    def area(self) -> float:
        """
        Calculate area of triangle
        :return: area
        """
        return cross3(self.b.position - self.a.position,
                      self.c.position - self.a.position).length() / 2.0

    # ------------------------------------------------------------------------------------------------------------------
    def toBarycentric(self, p: Vec3) -> Vec3:
        """
        Calculate barycentric coordinate of point p
        :param P: the input point (cartesian)
        :return: barycentric coordinate
        """
        abc = triangleArea(self.a.position, self.b.position, self.c.position)
        pbc = triangleArea(p, self.b.position, self.c.position)
        apc = triangleArea(self.a.position, p, self.c.position)

        if abc == 0.0:
            return Vec3(0, 0, 0)

        x = pbc / abc
        y = apc / abc
        return Vec3(x, y, 1.0 - x - y)

    # ------------------------------------------------------------------------------------------------------------------
    def fromBarycentric(self, b: Vec3) -> Vec3:
        """
        Calculate cartesian coordinate from barycentric coordinate
        :param b: barycentric coordinate
        :return: cartesian coordinate
        """
        return self.a.position * b.x + self.b.position * b.y + self.c.position * b.z

    # ------------------------------------------------------------------------------------------------------------------
    def circumradius(self) -> float:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()

        s = (a + b + c) / 2.0  # semiperimeter
        z = a * b * c
        n = 4.0 * math.sqrt(s * (a + b - s) * (a + c - s) * (b + c - s))
        if n == 0.0:
            return 0.0
        return z / n

    # ------------------------------------------------------------------------------------------------------------------
    def inradius(self) -> float:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()
        s = (a + b + c) / 2.0
        if s == 0.0:
            return 0.0
        return math.sqrt((s - a) * (s - b) * (s - c) / s)

    # ------------------------------------------------------------------------------------------------------------------
    def circumcenter(self) -> Vec3:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()
        q = a * a * (-a * a + b * b + c * c)
        w = b * b * (a * a - b * b + c * c)
        e = c * c * (a * a + b * b - c * c)
        n = q + w + e
        if n == 0.0:
            return Vec3(0, 0, 0)
        return self.fromBarycentric(Vec3(q / n, w / n, e / n))

    # ------------------------------------------------------------------------------------------------------------------
    def incenter(self) -> Vec3:
        a = (self.c.position - self.b.position).length()
        b = (self.c.position - self.a.position).length()
        c = (self.b.position - self.a.position).length()
        n = a + b + c
        if n == 0.0:
            return Vec3(0, 0, 0)

        return self.fromBarycentric(Vec3(a / n, b / n, c / n))

    # ------------------------------------------------------------------------------------------------------------------
    def centroid(self) -> Vec3:
        return (self.a.position + self.b.position + self.c.position) / 3.0

    # ------------------------------------------------------------------------------------------------------------------
    def calcTexcoord(self, p: Vec3) -> Vec2:
        """
        Returns texture-coordinate at cartesian position p
        :param p:
        :return: returns
        """
        pb = self.toBarycentric(p)
        u = self.a.texcoord.x * pb.x + self.b.texcoord.x * pb.y + self.c.texcoord.x * pb.z
        v = self.a.texcoord.y * pb.x + self.b.texcoord.y * pb.y + self.c.texcoord.y * pb.z
        return Vec2(u, v)

    # ------------------------------------------------------------------------------------------------------------------

    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        """
        Ray Triangle Intersection
        Original Code from:
        "Practical Analysis of Optimized Ray-Triangle Intersection"
        Tomas Möller
        Department of Computer Engineering, Chalmers University of Technology, Sweden.
        http://fileadmin.cs.lth.se/cs/Personal/Tomas_Akenine-Moller/raytri/

        :param ray: the ray to check hit
        :param tmin: tmin to test intersection
        :param tmax: tmax to test intersection
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        """
        t0 = hitrecord.t

        # find vectors for two edges sharing vert0
        edge1 = self.b.position - self.a.position
        edge2 = self.c.position - self.a.position

        # begin calculating determinant - also used to calculate U parameter
        pvec = cross3(ray.direction, edge2)

        # if determinant is near zero, ray lies in plane of triangle
        det = dot3(edge1, pvec)

        if det > self.EPSILON:
            tvec = ray.start - self.a.position
            u = dot3(tvec, pvec)
            if u < 0.0 or u > det:
                return False

            qvec = cross3(tvec, edge1)
            v = dot3(ray.direction, qvec)
            if v < 0.0 or u + v > det:
                return False
        elif det < -self.EPSILON:
            tvec = ray.start - self.a.position
            u = dot3(tvec, pvec)
            if u > 0.0 or u < det:
                return False

            qvec = cross3(tvec, edge1)
            v = dot3(ray.direction, qvec)
            if v > 0.0 or u + v < det:
                return False
        else:
            return False

        inv_det = 1.0 / det
        t = dot3(edge2, qvec) * inv_det
        u *= inv_det
        v *= inv_det

        if t0 is not None and t > t0:
            return False

        if t > 0.0:  # and t<tmax
            hitrecord.t = t
            hitrecord.point = ray.start + t * ray.direction
            hitrecord.normal = cross3(edge1, edge2)
            if self.a.normal is not None and self.b.normal is not None and self.c.normal is not None:
                nU = self.b.normal - self.a.normal
                nV = self.c.normal - self.a.normal
                hitrecord.normal_g = self.a.normal + nU * u + nV * v
            else:
                hitrecord.normal_g = hitrecord.normal

            # Calculate color
            cU = self.b.color - self.a.color
            cV = self.c.color - self.a.color
            hitrecord.color = self.a.color + cU * u + cV * v
            hitrecord.material = self.material

            hitrecord.point = ray.start + t * ray.direction

            return True

        return False

    def hitShadow(self, ray: Ray) -> bool:
        """
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        """
        # find vectors for two edges sharing vert0
        edge1 = self.b.position - self.a.position
        edge2 = self.c.position - self.a.position

        # begin calculating determinant - also used to calculate U parameter
        pvec = cross3(ray.direction, edge2)

        # if determinant is near zero, ray lies in plane of triangle
        det = dot3(edge1, pvec)

        if det > self.EPSILON:
            tvec = ray.start - self.a.position
            u = dot3(tvec, pvec)
            if u < 0.0 or u > det:
                return False

            qvec = cross3(tvec, edge1)
            v = dot3(ray.direction, qvec)
            if v < 0.0 or u + v > det:
                return False
        elif det < -self.EPSILON:
            tvec = ray.start - self.a.position
            u = dot3(tvec, pvec)
            if u > 0.0 or u < det:
                return False

            qvec = cross3(tvec, edge1)
            v = dot3(ray.direction, qvec)
            if v > 0.0 or u + v < det:
                return False
        else:
            return False

        inv_det = 1.0 / det
        t = dot3(edge2, qvec) * inv_det
        u *= inv_det
        v *= inv_det

        if t > 0.0:
            return True

        return False


# ----------------------------------------------------------------------------------------------------------------------
# Utility functions related to triangles

def triangleArea(a: Vec3, b: Vec3, c: Vec3) -> float:
    """
    Calculate area of triangle
    :return: area
    """
    return cross3(b - a, c - a).length() / 2.0
