"""
This is the geometric object sphere

(renderable object)
"""

from ..geometry import Shape
from ..math import Ray, HitRecord, Vec3, Vec4, dot3,  normalize3
from math import sqrt


class Sphere(Shape):

    """The Sphere class for raytracing"""

    def __init__(self, center: Vec3, radius: float, color: Vec4 = Vec4(1.,1.,1.,1.)) -> None:
        Shape.__init__(self, "Sphere")

        self.center = center
        self.radius = radius
        self.color = color


    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        """
        Hit ray with sphere. Code based on: Shirley P., Morley R.K. (2003) "Realistic RayTracing", 2nd edition

        :param ray: the ray to check hit
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        """

        temp = ray.start - self.center
        a = dot3(ray.direction, ray.direction)
        b = 2.*dot3(ray.direction, temp)
        c = dot3(temp, temp) - self.radius * self.radius

        discriminant = b*b-4*a*c

        if discriminant>0.0:
            discriminant = sqrt(discriminant)
            t = -b-discriminant / (2*a)

            if t < 0.0:
                t = -b + discriminant / (2*a)
            if t < 0.0:
                return False

            # there is a valid hit!
            hitrecord.t = t
            hitrecord.normal = hitrecord.normal_g = normalize3(ray.start + t  * ray.direction - self.center)
            hitrecord.color = self.color
            return True

        return False

    def hitShadow(self, ray: Ray) -> bool:
        """
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        """
        pass
