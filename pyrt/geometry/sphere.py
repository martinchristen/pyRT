"""
This is the geometric object sphere

(renderable object)
"""

from ..geometry import Shape
from ..math import Ray, HitRecord, Vec3, dot3, G_EPSILON
from ..material import Material, PhongMaterial
from math import sqrt


class Sphere(Shape):

    """The Sphere class for raytracing"""

    def __init__(self, center: Vec3, radius: float, material: Material = PhongMaterial()) -> None:
        Shape.__init__(self, "Sphere")

        self.center = center
        self.radius = radius
        self.material = material


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