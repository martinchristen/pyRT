import math
from .constants import *


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


