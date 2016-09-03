"""
Matrix Operations

This file contains all important external matrix operations and some utility functions
"""

import math
from .vec2 import *
from .vec3 import *
from .vec4 import *
from .mat4 import *
from math import sqrt, pi, tan


def deg2rad(v: float) -> float:
    return v * math.pi / 180.
# ---------------------------------------------------------------------------------------------------------------------


def rad2deg(v: float) -> float:
    return 180. * v / math.pi
# ---------------------------------------------------------------------------------------------------------------------


def createIdentity4() -> Mat4:
    """
    Create a 4x4 identity matrix
    """
    return Mat4((1., 0., 0., 0.,
                 0., 1., 0., 0.,
                 0., 0., 1., 0.,
                 0., 0., 0., 1.))
# ---------------------------------------------------------------------------------------------------------------------


def createZero4() -> Mat4:
    """
    Create a 4x4 zero matrix
    """
    return Mat4()
# ---------------------------------------------------------------------------------------------------------------------


def createTranslation4(x: float, y: float, z: float, w: float = 1.) -> Mat4:
    """
    Create a 4x4 translation matrix
    """
    return Mat4((1., 0., 0., x,
                 0., 1., 0., y,
                 0., 0., 1., z,
                 0., 0., 0., w))
# ---------------------------------------------------------------------------------------------------------------------


def createScale4(x: float, y: float, z: float, w: float = 1.) -> Mat4:
    """
    Create a 4x4 scale matrix
    """
    return Mat4((x, 0., 0., 0.,
                 0., y, 0, 0.,
                 0., 0., z, 0.,
                 0., 0., 0., w))
# ---------------------------------------------------------------------------------------------------------------------


def createRotationX4(angle: float = 0.) -> Mat4:
    """
    Create a rotation matrix

    :param angle: rotation about x-axis (radiant)
    :return: rotation matrix
    """
    return Mat4((1., 0., 0., 0.,
                 0., math.cos(angle), math.sin(angle), 0.,
                 0., -math.sin(angle), math.cos(angle), 0.,
                 0., 0., 0., 1.))
# ---------------------------------------------------------------------------------------------------------------------


def createRotationY4(angle: float = 0) -> Mat4:
    """
    Create a rotation matrix

    :param angle: rotation about y-axis (radiant)
    :return: rotation matrix
    """
    return Mat4((math.cos(angle), 0., -math.sin(angle), 0.,
                 0., 1., 0., 0.,
                 math.sin(angle), 0., math.cos(angle), 0.,
                 0., 0., 0., 1.))
# ---------------------------------------------------------------------------------------------------------------------


def createRotationZ4(angle: float = 0) -> Mat4:
    """
    Create a rotation matrix

    :param angle: rotation about z-axis (radiant)
    :return: rotation matrix
    """
    return Mat4((math.cos(angle), math.sin(angle), 0., 0.,
                 -math.sin(angle), math.cos(angle), 0., 0.,
                 0., 0., 1., 0.,
                 0., 0., 0., 1.))
# ---------------------------------------------------------------------------------------------------------------------


def createLookAt4(eye: Vec3, center: Vec3, up: Vec3) -> Mat4:
    """
    Create a look-at matrix

    :param eye:
    :param center:
    :param up:
    :return:
    """
    z0 = eye.x - center.x
    z1 = eye.y - center.y
    z2 = eye.z - center.z
    l1 = sqrt(z0 * z0 + z1 * z1 + z2 * z2)
    z0 /= l1
    z1 /= l1
    z2 /= l1

    x0 = up.y * z2 - up.z * z1
    x1 = up.z * z0 - up.x * z2
    x2 = up.x * z1 - up.y * z0
    l1 = sqrt(x0 * x0 + x1 * x1 + x2 * x2)

    if l1 == 0.:
        x0 = 0.
        x1 = 0.
        x2 = 0.
    else:
        x0 /= l1
        x1 /= l1
        x2 /= l1

    y0 = z1 * x2 - z2 * x1
    y1 = z2 * x0 - z0 * x2
    y2 = z0 * x1 - z1 * x0

    l1 = sqrt(y0 * y0 + y1 * y1 + y2 * y2)
    if l1 == 0.:
        y0 = 0
        y1 = 0
        y2 = 0
    else:
        y0 /= l1
        y1 /= l1
        y2 /= l1

    return Mat4((x0, x1, x2, -(x0*eye.x + x1*eye.y + x2*eye.z),
                 y0, y1, y2, -(y0*eye.x + y1*eye.y + y2*eye.z),
                 z0, z1, z2, -(z0*eye.x + z1*eye.y + z2*eye.z),
                 0., 0., 0., 1.))
# ---------------------------------------------------------------------------------------------------------------------


def createPerspective4(fovy: float, aspect: float, znear: float, zfar : float) -> Mat4:
    """
    Create a perspective transform

    :param fovy: field of view
    :param aspect: aspect ratio
    :param znear: near plane
    :param zfar: far plane
    :return: Matrix holding the transformation
    """
    f = 1.0 / tan(fovy * pi / 360.0)
    r0 = f / aspect
    r10 = (zfar + znear) / (znear - zfar)
    r11 = 2 * zfar * znear / (znear - zfar)

    return Mat4((r0, 0., 0., 0.,
                 0., f, 0., 0.,
                 0., 0., r10, r11,
                 0., 0., -1., 0.))
# ---------------------------------------------------------------------------------------------------------------------
#pylint: disable-msg=R0913


def createOrtho4(left: float, right : float, bottom: float, top: float, znear: float, zfar: float) -> Mat4:
    """
    Create an orthogonal transform

    :param left: left plane
    :param right:  right plane
    :param bottom:  bottom plane
    :param top: top plane
    :param znear: near plane
    :param zfar: far plane
    :return: Matrix holding the transformation
    """
    rl = (right - left)
    tb = (top - bottom)
    fn = (zfar - znear)

    return Mat4((2./rl, 0., 0., -(left + right) / rl,
                 0., 2./tb, 0., -(top + bottom) / tb,
                 0., 0., -2./fn, -(zfar + znear) / fn,
                 0., 0., 0., 1.))

# ---------------------------------------------------------------------------------------------------------------------
