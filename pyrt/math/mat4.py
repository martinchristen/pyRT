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
        if key == 0:
            return (self.m[0], self.m[1], self.m[2], self.m[3])
        elif key == 1:
            return (self.m[4], self.m[5], self.m[6], self.m[7])
        elif key == 2:
            return (self.m[8], self.m[9], self.m[10], self.m[11])
        elif key == 3:
            return (self.m[12], self.m[13], self.m[14], self.m[15])
        else:
            raise IndexError("Wrong index for 4x4 matrix")

