# Matrix Operations

import math
from .vec2 import *
from .vec3 import *
from .vec4 import *
from .mat4 import *


def deg2rad(v):
    return v * math.pi / 180.


def rad2deg(v):
    return 180. * v / math.pi


def CreateIdentity4():
    """
    Create a 4x4 identity matrix
    """
    return Mat4((1,0,0,0,
                 0,1,0,0,
                 0,0,1,0,
                 0,0,0,1))


def CreateZero4():
    """
    Create a 4x4 zero matrix
    """
    return Mat4()


def CreateTranslation4(x,y,z,w=1):
    """
    Create a 4x4 translation matrix
    """
    return Mat4((1, 0, 0, x,
                 0, 1, 0, y,
                 0, 0, 1, z,
                 0, 0, 0, w))


def CreateScale4(x,y,z,w=1):
    """
    Create a 4x4 scale matrix
    """
    return Mat4((x, 0, 0, 0,
                 0, y, 0, 0,
                 0, 0, z, 0,
                 0, 0, 0, w))


def CreateRotationX4(angle=0):
    """
    Create a rotation matrix
    :param angle: rotation about x-axis (radiant)
    :return: rotation matrix
    """
    return Mat4((1, 0, 0, 0,
                 0, math.cos(angle), math.sin(angle), 0,
                 0, -math.sin(angle), math.cos(angle), 0,
                 0, 0, 0, 1))


def CreateRotationY4(angle=0):
    """
    Create a rotation matrix
    :param angle: rotation about y-axis (radiant)
    :return: rotation matrix
    """
    return Mat4((math.cos(angle), 0, -math.sin(angle), 0,
                 0, 1, 0, 0,
                 math.sin(angle), 0, math.cos(angle), 0,
                 0, 0, 0, 1))

def CreateRotationZ4(angle=0):
    """
    Create a rotation matrix
    :param angle: rotation about z-axis (radiant)
    :return: rotation matrix
    """
    return Mat4((math.cos(angle), math.sin(angle), 0, 0,
                 -math.sin(angle), math.cos(angle), 0, 0,
                 0, 0, 1, 0,
                 0, 0, 0, 1))


