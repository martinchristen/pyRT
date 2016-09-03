"""
Mat4: 4x4 Matrix Class

This is the class for handling 4x4 Matrices
"""


import math
from .constants import *
from .vec3 import *
from .vec4 import *


class Mat4(object):

    """
    Class representing a 4x4 Matrix

    It contains all important methods for matrices. Some external operations are defined in "matops.py".
    """

    def __init__(self, elm=None):
        """
        elm:
            if None this will create a matrix initialized with 0

            if elm is a list or a tuple with 16 values, it will be initialized as 4x4 matrix
        """
        if isinstance(elm, type(None)):
            self.m = [0., 0., 0., 0.,
                      0., 0., 0., 0.,
                      0., 0., 0., 0.,
                      0., 0., 0., 0.]
        elif type(elm) == list or type(elm) == tuple:
            if len(elm) == 16:
                self.m = []
                for v in elm:
                    self.m.append(float(v))
            else:
                raise ValueError("Mat4 must be initialized in a list or tuple with 16 floats")

    def __str__(self):
        """Convert to string"""
        s = "[[" + str(self.m[0]) + ", " + str(self.m[1]) + ", " + str(self.m[2]) + ", " + str(self.m[3]) + "]\n"
        s += "[" + str(self.m[4]) + ", " + str(self.m[5]) + ", " + str(self.m[6]) + ", " + str(self.m[7]) + "]\n"
        s += "[" + str(self.m[8]) + ", " + str(self.m[9]) + ", " + str(self.m[10]) + ", " + str(self.m[11]) + "]\n"
        s += "[" + str(self.m[12]) + ", " + str(self.m[13]) + ", " + str(self.m[14]) + ", " + str(self.m[15]) + "]]"
        return s

    def __getitem__(self, key):
        if type(key) == tuple:
            if len(key) != 2:
                raise IndexError("Index must be 2-dimensional!")
            x, y = key

            if x < 0 or x > 4 or y < 0 or y > 4:
                raise IndexError("Index out of range!")

            return self.m[x + y * 4]
        else:
            raise IndexError("Matrix indices must be specified as tuple, for example:   s = m[1,2]")

    def __setitem__(self, key, value):
        if type(key) == tuple:
            if len(key) != 2:
                raise IndexError("Index must be 2-dimensional!")
            x, y = key

            if x < 0 or x > 4 or y < 0 or y > 4:
                raise IndexError("Index out of range!")

            self.m[x + y * 4] = value

        else:
            raise IndexError("Matrix indices must be access as tuple, for example:   m[1,2] = 5")

    def transpose(self):
        """Transpose matrix"""
        t = self.m.copy()
        for x in range(0, 4):
            for y in range(0, 4):
                index0 = x + y * 4
                index1 = y + x * 4
                self.m[index0] = t[index1]

    def __eq__(self, other):
        if type(other) == list or type(other) == tuple:  # not checking type within tuple/list
            if len(other) == 16:
                for i in range(0, 16):
                    if abs(self.m[i] - other[i]) > G_EPSILON:
                        return False
                return True
            else:
                raise ValueError("Can't compare 4x4 Matrix with list or tuple of length != 16")
        elif type(other) == Mat4:
            for i in range(0, 16):
                if (abs(self.m[i] - other.m[i]) > G_EPSILON):
                    return False
            return True
        else:
            raise ValueError("Can't compare matrix with " + str(type(other)))

    def __add__(self, other):
        """add two Mat4"""
        if type(other) == Mat4:
            return Mat4((self.m[0] + other.m[0], self.m[1] + other.m[1], self.m[2] + other.m[2], self.m[3] + other.m[3],
                         self.m[4] + other.m[4], self.m[5] + other.m[5], self.m[6] + other.m[6], self.m[7] + other.m[7],
                         self.m[8] + other.m[8], self.m[9] + other.m[9], self.m[10] + other.m[10],
                         self.m[11] + other.m[11],
                         self.m[12] + other.m[12], self.m[13] + other.m[13], self.m[14] + other.m[14],
                         self.m[15] + other.m[15]))
        else:
            raise ValueError("Wrong type for matrix addition: " + str(type(other)))

    def __sub__(self, other):
        """subtract two Mat4"""
        if type(other) == Mat4:
            return Mat4((self.m[0] - other.m[0], self.m[1] - other.m[1], self.m[2] - other.m[2], self.m[3] - other.m[3],
                         self.m[4] - other.m[4], self.m[5] - other.m[5], self.m[6] - other.m[6], self.m[7] - other.m[7],
                         self.m[8] - other.m[8], self.m[9] - other.m[9], self.m[10] - other.m[10],
                         self.m[11] - other.m[11],
                         self.m[12] - other.m[12], self.m[13] - other.m[13], self.m[14] - other.m[14],
                         self.m[15] - other.m[15]))
        else:
            raise ValueError("Wrong type for matrix subtraction: " + str(type(other)))

    def __mul__(self, other):
        """
        The following multiplications are supported:

        Matrix4 Matrix4 multiplication
        Matrix4 Vector3 multiplication
        Matrix4 Vector4 multiplication
        """
        if type(other) == Mat4:
            newmat = Mat4()
            newmat.m[0] = other.m[0] * self.m[0]\
                          + other.m[4] * self.m[1] \
                          + other.m[8] * self.m[2] \
                          + other.m[12] * self.m[3]
            newmat.m[4] = other.m[0] * self.m[4] \
                          + other.m[4] * self.m[5] \
                          + other.m[8] * self.m[6] \
                          + other.m[12] * self.m[7]
            newmat.m[8] = other.m[0] * self.m[8] \
                          + other.m[4] * self.m[9] \
                          + other.m[8] * self.m[10] \
                          + other.m[12] * self.m[11]
            newmat.m[12] = other.m[0] * self.m[12] \
                           + other.m[4] * self.m[13] \
                           + other.m[8] * self.m[14] \
                           + other.m[12] * self.m[15]
            newmat.m[1] = other.m[1] * self.m[0] \
                          + other.m[5] * self.m[1] \
                          + other.m[9] * self.m[2] \
                          + other.m[13] * self.m[3]
            newmat.m[5] = other.m[1] * self.m[4] \
                          + other.m[5] * self.m[5] \
                          + other.m[9] * self.m[6] \
                          + other.m[13] * self.m[7]
            newmat.m[9] = other.m[1] * self.m[8] \
                          + other.m[5] * self.m[9] \
                          + other.m[9] * self.m[10] \
                          + other.m[13] * self.m[11]
            newmat.m[13] = other.m[1] * self.m[12] \
                           + other.m[5] * self.m[13] \
                           + other.m[9] * self.m[14] \
                           + other.m[13] * self.m[15]
            newmat.m[2] = other.m[2] * self.m[0] \
                          + other.m[6] * self.m[1] \
                          + other.m[10] * self.m[2] \
                          + other.m[14] * self.m[3]
            newmat.m[6] = other.m[2] * self.m[4] \
                          + other.m[6] * self.m[5] \
                          + other.m[10] * self.m[6] \
                          + other.m[14] * self.m[7]
            newmat.m[10] = other.m[2] * self.m[8] \
                           + other.m[6] * self.m[9] \
                           + other.m[10] * self.m[10] \
                           + other.m[14] * self.m[11]
            newmat.m[14] = other.m[2] * self.m[12] \
                           + other.m[6] * self.m[13] \
                           + other.m[10] * self.m[14] \
                           + other.m[14] * self.m[15]
            newmat.m[3] = other.m[3] * self.m[0] \
                          + other.m[7] * self.m[1] \
                          + other.m[11] * self.m[2] \
                          + other.m[15] * self.m[3]
            newmat.m[7] = other.m[3] * self.m[4] \
                          + other.m[7] * self.m[5] \
                          + other.m[11] * self.m[6] \
                          + other.m[15] * self.m[7]
            newmat.m[11] = other.m[3] * self.m[8] \
                           + other.m[7] * self.m[9] \
                           + other.m[11] * self.m[10] \
                           + other.m[15] * self.m[11]
            newmat.m[15] = other.m[3] * self.m[12] \
                           + other.m[7] * self.m[13] \
                           + other.m[11] * self.m[14] \
                           + other.m[15] * self.m[15]
            return newmat

        if type(other) == Vec3:
            result = Vec3()
            result.x = self.m[0] * other.x + self.m[1] * other.y + self.m[2] * other.z + self.m[3]
            result.y = self.m[4] * other.x + self.m[5] * other.y + self.m[6] * other.z + self.m[7]
            result.z = self.m[8] * other.x + self.m[9] * other.y + self.m[10] * other.z + self.m[11]
            w = self.m[12] * other.x + self.m[13] * other.y + self.m[14] * other.z + self.m[15]

            result.x = result.x / w
            result.y = result.y / w
            result.z = result.z / w

            return result

        if type(other) == Vec4:
            result = Vec4()
            result.x = self.m[0] * other.x + self.m[1] * other.y + self.m[2] * other.z + self.m[3]
            result.y = self.m[4] * other.x + self.m[5] * other.y + self.m[6] * other.z + self.m[7]
            result.z = self.m[8] * other.x + self.m[9] * other.y + self.m[10] * other.z + self.m[11]
            result.w = self.m[12] * other.x + self.m[13] * other.y + self.m[14] * other.z + self.m[15]

            return result
        else:
            raise ValueError("Can't multiply matrix with specified type: " + str(type(other)))
