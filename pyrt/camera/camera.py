"""
Base class for cameras

Inherit from this if you create a new camera model
"""

from abc import abstractmethod
from ..math import Vec3, createLookAt4, createIdentity4, Ray, Mat4


class Camera(object):

    """This defines the base class for all cameras"""

    def __init__(self):
        self.position = Vec3(0.,0.,0.)
        self.view = createIdentity4()

    def setView(self, eye: Vec3, center: Vec3, up: Vec3):
        """
        Set View Matrix using look-at (from eye to center)

        :param eye: current position
        :param center: position where to look at
        :param up: up-axis when looking at
        :return:
        """
        self.view = createLookAt4(eye, center, up)

    @abstractmethod
    def primaryRay(self, x: float, y: float) -> Ray:
        """
        Calculate primary ray

        :param x: screen position x (subpixel)
        :param y: screen position y (subpixel)
        :return: ray
        """
        pass

    @abstractmethod
    def getMatrix(self) -> Mat4:
        """
        Returns the view-projection matrix

        :return:
        """
        pass
