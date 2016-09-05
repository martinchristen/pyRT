"""
Vec2: 2 dimensional vector class

This is the class for handling 2 dimensional vectors
"""

import math
from .constants import *


class Vec2(object):
    """Class representing a 2D-Vector. Values are always stored as float
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        """Convert vector to string
        """
        return "Vec2(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):
        """add two vectors
        other: vector to add"""
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """subtract two vectors
        other: vector to subtract"""
        return Vec2(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) == list or type(other) == tuple:  # not checking type within tuple/list
            if len(other) == 2:
                return (abs(self.x - other[0]) < G_EPSILON) and (abs(self.y - other[1]) < G_EPSILON)
            else:
                raise ValueError("Can't compare vector with list or tuple of length != 3")
        elif type(other) == Vec2:
            return (abs(self.x - other.x) < G_EPSILON) and (abs(self.y - other.y) < G_EPSILON)
        else:
            raise ValueError("Can't compare this type")

    def __mul__(self, s):
        if type(s) == Vec2:
            return Vec2(self.x * s.x, self.y * s.y)
        elif type(s) == float or type(s) == int:
            return Vec2(self.x * s, self.y * s)
        else:
            raise ValueError("Multiplicaton with wrong type: " + str(type(s)))

    def __rmul__(self, s):
        if type(s) == Vec2:
            return Vec2(self.x * s.x, self.y * s.y)
        elif type(s) == float or type(s) == int:
            return Vec2(self.x * s, self.y * s)
        else:
            raise ValueError("Multiplicaton with wrong type:" + str(type(s)))

    def __truediv__(self, s):
        if type(s) == Vec2:
            return Vec2(self.x / s.x, self.y / s.y)
        elif type(s) == float or type(s) == int:
            return Vec2(self.x / s, self.y / s)
        else:
            raise ValueError("Division with wrong type" + str(type(s)))

    def __rtruediv__(self, s):
        if type(s) == Vec2:
            return Vec2(s.x / self.x, s.y / self.y)
        elif type(s) == float or type(s) == int:
            return Vec2(s / self.x, s / self.y)
        else:
            raise ValueError("Division with wrong type: " + str(type(s)))

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Vec2 has 3 components: [0] [1] and [2]")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = float(value)
        elif key == 1:
            self.y = float(value)
        else:
            raise IndexError("Vec2 has 3 components: [0] [1] and [2]")

    def copy(self):
        """
        :return: copy of current vector
        """
        return Vec2(self.x, self.y)

    def length(self):
        """
        :return: return length of vector
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        """
        normalize this vector
        """
        l = self.length()
        if l != 0:
            self.x /= l
            self.y /= l
