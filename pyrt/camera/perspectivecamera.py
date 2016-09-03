from ..math import Ray, createPerspective4
from .camera import Camera
from math import pi, tan


class PerspectiveCamera(Camera):

    """This defines a perspective camera"""

    def __init__(self, width: int = 640, height: int = 480, fov: float = 45) -> None:
        """
        Initialize perspective camera

        :param width: horizontal resolution of the output image
        :param height: vertical resolution of the output image
        :param fov: field of view (degree)
        """
        Camera.__init__(self)

        self.width = width
        self.height = height
        znear = 0.1
        zfar = 1000.0
        aspect = width / height
        self.projection = createPerspective4(fov, aspect, znear, zfar)

    def primaryRay(self, x: float, y: float) -> Ray:
        pass
