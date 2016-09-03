"""
Base class for cameras

Inherit from this if you create a new camera model
"""
from abc import abstractmethod


class Camera(object):
    def __init__(self):
        pass

    @abstractmethod
    def primaryRay(self, x, y):
        pass