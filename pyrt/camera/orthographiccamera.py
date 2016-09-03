from ..math import Ray, Vec3


class OrthographicCamera(object):
    def __init__(self, width=512, height=512):
        """
        :param width: horizontal resolution of the output image
        :param height: vertical resolution of the output image
        """
        self.width = width
        self.height = height
        self.direction = Vec3(0.0,0.0,-1.0)

        print("[init] Orthographic Camera")

    def primaryRay(self, x, y):
        r = Ray(Vec3(x,y,0), self.direction)
        return r
