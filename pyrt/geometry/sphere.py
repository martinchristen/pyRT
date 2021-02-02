"""
This is the geometric object sphere

(renderable object)
"""

from ..geometry import Shape
from ..math import Ray, HitRecord, Vec2, Vec3, dot3, G_EPSILON
from ..material import Material, PhongMaterial
from .bbox import BBox
from math import sqrt, pi, asin, atan2


class Sphere(Shape):

    """The Sphere class for raytracing"""

    def __init__(self, center: Vec3, radius: float, material: Material = PhongMaterial()) -> None:
        Shape.__init__(self, "Sphere")

        self.center = center
        self.radius = radius
        self.material = material


    def calcTexcoord(self, p: Vec3) -> Vec2:
        """
        Returns texture-coordinate at cartesian position p
        :param p:
        :return: returns
        """

        # change coordinate system's origin to sphere's center
        p_central = p - self.center

        # sphere radius
        r = p_central.length()

        u = 1.0 - (atan2(p_central.z, p_central.x) + pi) / (2.0 * pi)
        v = (asin(p_central.y / r) + pi / 2) / pi
        return Vec2(u, v)


    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        """
        Hit ray with sphere.

        :param ray: the ray to check hit
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        """
        t0 = hitrecord.t

        a = dot3(ray.direction, ray.direction)
        b = dot3(ray.direction, (2.0 * (ray.start - self.center)))
        c = dot3(self.center, self.center) + dot3(ray.start, ray.start) \
            - 2.0 * dot3(ray.start,self.center) - self.radius * self.radius
        D = b * b + (-4.0) * a * c

        if D < G_EPSILON:
            return False

        D = sqrt(D)
        t = -0.5*(b + D) / a

        if t0 is not None and t0 < t:
            return False

        if t>0:
            hitrecord.t = t
            hitrecord.point = ray.start + t * ray.direction
            hitrecord.normal_g = (hitrecord.point - self.center) / self.radius
            hitrecord.normal = hitrecord.normal_g
            hitrecord.color = Vec3(1., 1., 1.)  # spheres don't have interpolated colors, set to white
            hitrecord.material = self.material
            return True
        return False



    def hitShadow(self, ray: Ray) -> bool:
        """
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        """
        a = dot3(ray.direction, ray.direction)
        b = dot3(ray.direction, (2.0 * (ray.start - self.center)))
        c = dot3(self.center, self.center) + dot3(ray.start, ray.start) \
            - 2.0 * dot3(ray.start, self.center) - self.radius * self.radius
        D = b * b + (-4.0) * a * c

        if D < G_EPSILON:
            return False

        D = sqrt(D)
        t = -0.5 * (b + D) / a

        if t > 0:
            return True
        return False


    def getBBox(self):
        """
        Retrieve axis aligned bounding box of the sphere


        :return: bounding box
        """
        bbmin = Vec3(self.center - Vec3(self.radius, self.radius, self.radius))
        bbmax = Vec3(self.center + Vec3(self.radius, self.radius, self.radius))
        return BBox(bbmin, bbmax)


    def getCentroid(self) -> Vec3:
        """
        Retrieve center of sphere
        :return:
        """
        return self.center


    def getSurfaceArea(self):
        """
        Retrieve surface area

        :return: surface area
        """
        return 4. * pi * self.radius**2