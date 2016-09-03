"""
Base class for cameras

Inherit from this if you create a new camera model
"""
from abc import abstractmethod
from ..math import Vec3, Mat4, createLookAt4, createIdentity4, Ray


class Camera(object):

    """This defines the base class for all cameras"""

    def __init__(self):
        self.view = createIdentity4()
        pass

    def setView(self, eye: Vec3, center: Vec3, up: Vec3):
        self.view = createLookAt4(eye, center, up)
        pass

    @abstractmethod
    def primaryRay(self, x: float, y: float) -> Ray:
        pass