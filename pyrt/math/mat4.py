import math
from .constants import *
from .vec3 import *
from .vec4 import *

class Mat4:
    """
    Class representing a 4x4 Matrix
    """
    def __init__(self, elm=None):
        """
        elm:
            if None this will create a matrix initialized with 0

            if elm is a list or a tuple with 16 values, it will be initialized as 4x4 matrix
        """

        if type(elm) == type(None):
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
        """Convert to string
        """
        s = "[[" + str(self.m[0]) + ", " + str(self.m[1]) + ", " + str(self.m[2]) + ", " + str(self.m[3]) + "]\n"
        s += "[" + str(self.m[4]) + ", " + str(self.m[5]) + ", " + str(self.m[6]) + ", " + str(self.m[7]) + "]\n"
        s += "[" + str(self.m[8]) + ", " + str(self.m[9]) + ", " + str(self.m[10]) + ", " + str(self.m[11]) + "]\n"
        s += "[" + str(self.m[12]) + ", " + str(self.m[13]) + ", " + str(self.m[14]) + ", " + str(self.m[15]) + "]]"
        return s

    def __getitem__(self, key):
        if type(key) == tuple:
            if len(key) != 2:
                raise IndexError("Index must be 2-dimensional!")
            x,y = key

            if x<0 or x>4 or y<0 or y>4:
                raise IndexError("Index out of range!")

            return self.m[x + y*4]
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
        """
        Transpose matrix
        """
        t = self.m.copy()
        for x in range(0,4):
            for y in range(0,4):
                index0 = x+y*4
                index1 = y+x*4
                self.m[index0] = t[index1]


    def __mul__(self, other):
        """
        Matrix4 Matrix4 multiplication
        Matrix4 Vector3 multiplication
        Matrix4 Vector4 multiplication
        """
        if type(other) == Mat4:
            a00 = self.m[0]
            a10 = self.m[1]
            a20 = self.m[2]
            a30 = self.m[3]
            a01 = self.m[4]
            a11 = self.m[5]
            a21 = self.m[6]
            a31 = self.m[7]
            a02 = self.m[8]
            a12 = self.m[9]
            a22 = self.m[10]
            a32 = self.m[11]
            a03 = self.m[12]
            a13 = self.m[13]
            a23 = self.m[14]
            a33 = self.m[15]

            b00 = other.m[0]
            b10 = other.m[1]
            b20 = other.m[2]
            b30 = other.m[3]
            b01 = other.m[4]
            b11 = other.m[5]
            b21 = other.m[6]
            b31 = other.m[7]
            b02 = other.m[8]
            b12 = other.m[9]
            b22 = other.m[10]
            b32 = other.m[11]
            b03 = other.m[12]
            b13 = other.m[13]
            b23 = other.m[14]
            b33 = other.m[15]

            newmat = Mat4()

            newmat.m[0] = b00 * a00 + b01 * a10 + b02 * a20 + b03 * a30
            newmat.m[4] = b00 * a01 + b01 * a11 + b02 * a21 + b03 * a31
            newmat.m[8] = b00 * a02 + b01 * a12 + b02 * a22 + b03 * a32
            newmat.m[12] = b00 * a03 + b01 * a13 + b02 * a23 + b03 * a33

            newmat.m[1] = b10 * a00 + b11 * a10 + b12 * a20 + b13 * a30
            newmat.m[5] = b10 * a01 + b11 * a11 + b12 * a21 + b13 * a31
            newmat.m[9] = b10 * a02 + b11 * a12 + b12 * a22 + b13 * a32
            newmat.m[13] = b10 * a03 + b11 * a13 + b12 * a23 + b13 * a33

            newmat.m[2] = b20 * a00 + b21 * a10 + b22 * a20 + b23 * a30
            newmat.m[6] = b20 * a01 + b21 * a11 + b22 * a21 + b23 * a31
            newmat.m[10] = b20 * a02 + b21 * a12 + b22 * a22 + b23 * a32
            newmat.m[14] = b20 * a03 + b21 * a13 + b22 * a23 + b23 * a33

            newmat.m[3] = b30 * a00 + b31 * a10 + b32 * a20 + b33 * a30
            newmat.m[7] = b30 * a01 + b31 * a11 + b32 * a21 + b33 * a31
            newmat.m[11] = b30 * a02 + b31 * a12 + b32 * a22 + b33 * a32
            newmat.m[15] = b30 * a03 + b31 * a13 + b32 * a23 + b33 * a33

            return newmat
        if type(other) == Vec3:
            pass # TODO: implement

        if type(other) == Vec4:
            pass # TODO: implement
    
        else:
            raise ValueError("Can't multiply matrix with specified type: " + str(type(other)))
