from ..geometry import *
from ..math import *

class Sphere(Shape):
    def __init__(self):
        Shape.__init__(self)
        print("[init] sphere")

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

