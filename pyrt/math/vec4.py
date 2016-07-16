import math
from .constants import *


class Vec4:
    """Class representing a 3D-Vector
    params:
       x,y,z,w Component of vector (float or int)
    """
    def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

