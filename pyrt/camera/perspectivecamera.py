from ..math import *
from math import pi, tan

class PerspectiveCamera:
    def __init__(self, width : float = 640, height : float = 480, hfov : float = 45, lookfrom: Vec3 = Vec3(0,0,10), lookat: Vec3 = Vec3(0,0,0), up : Vec3 = Vec3(0,1,0)) -> None:
        """
        :param width: horizontal resolution of the output image
        :param height: vertical resolution of the output image
        :param hfov: vertical field of view (in degrees)
        :param lookfrom: vector looking from
        :param lookat: vector looking at
        :param up: up vector
        """
        pass

    def primaryRay(self, x: Vec3, y: Vec3) -> Ray:
        pass

    def __str__(self):
        s = "********************************************\n"
        s += "** Camera Info                            **\n"
        s += "********************************************\n"
        s += "Half Height = " + str(self.hh) + "\n"
        s += "Half Width = " + str(self.hw) + "\n"
        s += "Pixelsize = " + str(self.pixelsize) + "\n"
        s += "aspect = " + str(self.aspect) + "\n"
        s += "Center Vector: " + str(self.center) + "\n"
        s += "TopLeft Vector: " + str(self.tl) + "\n"
        s += "Pos: " + str(self.position) + "\n"
        s += "View Direction: " + str(self.viewdirection) + "\n"
        s += "UpVec vec: " + str(self.upvec) + "\n"
        s += "Up: " + str(self.up) + "\n"
        s += "Right Vec: " + str(self.right) + "\n"
        s += "********************************************\n"
        return s
