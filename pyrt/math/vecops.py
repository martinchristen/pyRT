"""
Vector operations

varius utility functions for vectors
"""

import math
from .vec2 import *
from .vec3 import *
from .vec4 import *


# ---------------------------------------------------------------------------------------------------------------------
def cross3(v1 ,v2):
    """
    Cross product for Vec3
    :param v1: first vector
    :param v2: second vector
    :return: cross product
    """
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vec3(x, y, z)

# ---------------------------------------------------------------------------------------------------------------------

def cross(v1, v2):
    """Calculates cross product. Consider using cross2, cross3, cross4
    v1: vector
    v2: vector
    """
    if type(v1) == Vec2 and type(v2) == Vec2:
        raise TypeError("Vec2 currently not supported for cross(v1,v2)")
    elif type(v1) == Vec3 and type(v2) == Vec3:
        return cross3(v1,v2)
    elif type(v1) == Vec4 and type(v2) == Vec4:
        raise TypeError("Vec4 currently not supported for cross(v1,v2)")
    else:
        raise TypeError("Wrong type for cross(v1,v2)")

# ---------------------------------------------------------------------------------------------------------------------

def dot3(a,b):
    """calculates the dot product"""
    return a.x * b.x + a.y * b.y + a.z * b.z

# ---------------------------------------------------------------------------------------------------------------------

def normalize3(v):
    """Returns the normalized vector without modifying the original vector"""
    l = v.length()
    if l != 0:
        return Vec3(v.x / l, v.y / l, v.z / l)
    else:
        return Vec3(0.0, 0.0, 0.0)

# ---------------------------------------------------------------------------------------------------------------------

def normalize(v):
    """
    Normalizes a vector, consider using normalize2, normalize3, normalize4
    :param v:
    :return:
    """
    if type(v) == Vec2 :
        raise TypeError("Vec2 currently not supported for normalize(v)")
    elif type(v) == Vec3:
        return normalize3(v)
    elif type(v) == Vec4:
        raise TypeError("Vec4 currently not supported for normalize(v)")
    else:
        raise TypeError("Wrong type for normalize(v)")


# ---------------------------------------------------------------------------------------------------------------------

def reflect3(N, I):
    """Reflects a vector
    N: Normal
    I: Incdient vector"""
    return I + N * (-2.0 * dot3(N, I))

# ---------------------------------------------------------------------------------------------------------------------

def faceforward3(N, I):
    """
    faceforward operation
    N: Normal vector
    I: Incident vector
    """
    if dot3(N, I) < 0:
        return N
    else:
        return -N

# ---------------------------------------------------------------------------------------------------------------------

def refract3(N, I, eta):
    """
    refract operation
    N: Normal vector
    I: Incident vector
    eta: Refraction koefficient
    """
    d = dot3(I, N)
    k = 1 - eta * eta * (1 - d * d)
    if k < 0:
        return I
    else:
        return I * eta - N * (eta * d + math.sqrt(k))

# ---------------------------------------------------------------------------------------------------------------------

def sign3(v):
    def fsign(f):
        if f < 0:
            return -1
        if f > 0:
            return 1
        else:
            return 0

    return Vec3(fsign(v.x), fsign(v.y), fsign(v.z))

# ---------------------------------------------------------------------------------------------------------------------
def clamp(v: float, minVal: float, maxVal: float):
    """
        Component-wise clamp

        In case v is smaller than minVal, minVal is returned.
        If v is larger than maxVal, maxVal is returned.

        :param v: vector to clamp
        :param minVal: minimal value (component-wise)
        :param maxVal: maximal value (component-wise)
        :return: clamped value
    """
    if v<minVal:
        return minVal
    elif v>maxVal:
        return maxVal
    else:
        return v

# ---------------------------------------------------------------------------------------------------------------------

def clamp2(v: Vec2, minVal: Vec2, maxVal: Vec2):
    """
    Component-wise clamp

    In case v is smaller than minVal, minVal is returned.
    If v is larger than maxVal, maxVal is returned.

    :param v: vector to clamp
    :param minVal: minimal value (component-wise)
    :param maxVal: maximal value (component-wise)
    :return: clamped value
    """
    result = v.copy()
    if v.x < minVal.x:
        result.x = minVal.x
    if v.y < minVal.y:
        result.y = minVal.y
    if v.x > maxVal.x:
        result.x = maxVal.x
    if v.y > maxVal.y:
        result.y = maxVal.y

    return result

# ---------------------------------------------------------------------------------------------------------------------


def clamp3(v: Vec3, minVal: Vec3, maxVal:Vec3):
    """
    Component-wise clamp

    In case v is smaller than minVal, minVal is returned.
    If v is larger than maxVal, maxVal is returned.

    :param v: vector to clamp
    :param minVal: minimal value (component-wise)
    :param maxVal: maximal value (component-wise)
    :return: clamped value
    """
    result = v.copy()
    if v.x < minVal.x:
        result.x = minVal.x
    if v.y < minVal.y:
        result.y = minVal.y
    if v.z < minVal.z:
        result.z = minVal.z
    if v.x > maxVal.x:
        result.x = maxVal.x
    if v.y > maxVal.y:
        result.y = maxVal.y
    if v.z > maxVal.z:
        result.z = maxVal.z

    return result

# ---------------------------------------------------------------------------------------------------------------------


def clamp4(v: Vec4, minVal: Vec4, maxVal: Vec4):
    """
    Component-wise clamp

    In case v is smaller than minVal, minVal is returned.
    If v is larger than maxVal, maxVal is returned.

    :param v: vector to clamp
    :param minVal: minimal value (component-wise)
    :param maxVal: maximal value (component-wise)
    :return: clamped value
    """
    result = v.copy()
    if v.x < minVal.x:
        result.x = minVal.x
    if v.y < minVal.y:
        result.y = minVal.y
    if v.z < minVal.z:
        result.z = minVal.z
    if v.w < minVal.w:
        result.w = minVal.w
    if v.x > maxVal.x:
        result.x = maxVal.x
    if v.y > maxVal.y:
        result.y = maxVal.y
    if v.z > maxVal.z:
        result.z = maxVal.z
    if v.w > maxVal.w:
        result.w = maxVal.w

    return result

