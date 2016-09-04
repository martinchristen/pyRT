"""
Vec4: 4 dimensional vector class

This is the class for handling 4 dimensional vectors
"""

import math
from .constants import *
from .vec3 import *


class Vec4(object):
    """Class representing a 4D-Vector. Values are always stored as float
    """

    def __init__(self, *args, **kwargs):
        """
        Vec3 can be constructed the following way:

        v1 = Vec4(x,y,z,w)     # 4 integers or floats
        v2 = Vec4([x,y,z,w])   # from a list of 4 integers or floats
        v3 = Vec4((x,y,z,w))   # from a tuple of 4 integers or floats
        v4 = Vec4(x)
        v5 = Vec3(Vec3(1,2,3), 4) # from a Vec3 with optional w-Value (if not set, w=1)

        # using named arguments
        v6 = Vec4(z=1)
        v7 = Vec4(x=1, y=2, z=3)
        v8 = Vec4(y=4, x=2)
        v9 = Vec4(x=2, w=2)

        # using nothing (Null-Vector)
        v10 = Vec4()

        """

        if len(kwargs) == 0:
            if len(args) == 4:
                self.x = float(args[0])
                self.y = float(args[1])
                self.z = float(args[2])
                self.w = float(args[3])
            elif len(args) == 1:
                if type(args) == tuple or type(args) == list:
                    self.x = float(args[0][0])
                    self.y = float(args[0][1])
                    self.z = float(args[0][2])
                    self.w = float(args[0][3])
                elif type(args[0]) == Vec3:
                    self.x = args[0].x
                    self.y = args[0].y
                    self.z = args[0].z
                    self.w = 1.0
                else:
                    raise ValueError("Sequencial definition of Vec4 must be list or tuple!")
            elif len(args) == 2:
                if type(args[0]) == Vec3:
                    self.x = args[0].x
                    self.y = args[0].y
                    self.z = args[0].z
                    self.w = float(args[1])

            elif len(args) == 0:
                self.x = self.y = self.z = 0.0
                self.w = 1.0
            else:
                raise ValueError("Wrong number of parameters in Vec3")
        else:
            if len(args) > 0:
                raise ValueError("Use keyword arguments OR normal arguments, both is not permitted")

            if "x" in kwargs:
                self.x = float(kwargs["x"])
            else:
                self.x = 0

            if "y" in kwargs:
                self.y = float(kwargs["y"])
            else:
                self.y = 0

            if "z" in kwargs:
                self.z = float(kwargs["z"])
            else:
                self.z = 0

            if "w" in kwargs:
                self.w = float(kwargs["w"])
            else:
                self.w = 1.0

    def __str__(self):
        """Convert vector to string
        """
        return "Vec4(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w) + ")"

    def __add__(self, other):
        """add two vectors
        other: vector to add"""
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        """subtract two vectors
        other: vector to subtract"""
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, s):
        if type(s) == Vec4:
            return Vec4(self.x * s.x, self.y * s.y, self.z * s.z, self.w * s.w)
        elif type(s) == float or type(s) == int:
            return Vec4(self.x * s, self.y * s, self.z * s, self.w * s)
        else:
            raise ValueError("Vec4: Multiplicaton with wrong type: " + str(type(s)))

    def __eq__(self, other):
        if type(other) == list or type(other) == tuple:  # not checking type within tuple/list
            if len(other) == 4:
                return (abs(self.x - other[0]) < G_EPSILON) and \
                       (abs(self.y - other[1]) < G_EPSILON) and \
                       (abs(self.z - other[2]) < G_EPSILON) and \
                       (abs(self.w - other[3]) < G_EPSILON)
            else:
                raise ValueError("Can't compare vector with list or tuple of length != 4")
        elif type(other) == Vec4:
            return (abs(self.x - other.x) < G_EPSILON) and \
                   (abs(self.y - other.y) < G_EPSILON) and \
                   (abs(self.z - other.z) < G_EPSILON) and \
                   (abs(self.w - other.w) < G_EPSILON)
        else:
            raise ValueError("Can't compare this type")

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        elif key == 3:
            return self.w
        else:
            raise IndexError("Vec4 has 4 components: [0] [1] [2] and [3]")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = float(value)
        elif key == 1:
            self.y = float(value)
        elif key == 2:
            self.z = float(value)
        elif key == 3:
            self.w = float(value)
        else:
            raise IndexError("Vec4 has 4 components: [0] [1] [2] and [3]")

    def copy(self):
        """
        :return: copy of current vector
        """
        return Vec4(self.x, self.y, self.z, self.w)

    def isZero(self):
        """
        :return: True if this is a zero-vector
        """
        return math.fabs(self.x) < G_EPSILON and \
               math.fabs(self.y) < G_EPSILON and \
               math.fabs(self.z) < G_EPSILON and \
               math.fabs(self.w) < G_EPSILON

    def length(self):
        """
        :return: return length of vector
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def normalize(self):
        """
        normalize this vector
        """
        l = self.length()
        if l != 0:
            self.x /= l
            self.y /= l
            self.z /= l
            self.w /= l
