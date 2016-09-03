"""
Orthographic Camera

This is for a standard orthographic camera
"""

from ..math import Ray, Vec3
from .camera import Camera

class OrthographicCamera(Camera):

    """This defines an orthographic camera"""

    def __init__(self, width=512, height=512):
        """
        :param width: horizontal resolution of the output image
        :param height: vertical resolution of the output image
        """
        Camera.__init__(self)

        self.width = width
        self.height = height
        self.direction = Vec3(0.0, 0.0, -1.0)

        print("[init] Orthographic Camera")

    def primaryRay(self, x: float, y: float) -> Ray:
        r = Ray(Vec3(x, y, 0.), self.direction)
        return r
