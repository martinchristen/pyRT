from ..math import *


class PerspectiveCamera:
    def __init__(self, width=640, height=480, fov=45):
        """
        :param width: horizontal resolution of the output image
        :param height: vertical resolution of the output image
        :param fov: horizontal field of view (in degrees)
        """
        print("[init] Perspective Camera")

        self.width = width  # image width in pixels
        self.height = height  # image height in pixels
        self.position = Vec3(15., 0., 1.)  # camera position
        self.viewdirection = Vec3(-1., 0., 0.)  # view direction
        self.viewdirection.normalize()
        self.upvec = Vec3(0., 0., 1.)  #up-vector
        self.movedirection = Vec3()  # move direction
        self.right = Vec3(1., 0., 0.)  # right vector
        self.up = Vec3(0., 0., 1.)  # up-vector

        self.near = 0.1  # near plane
        self.far = 1000.0  # far plane
        self.fov = deg2rad(fov)   # field of view (stored in rad)

        self.update()

    def update(self):
        self.up = self.upvec

        self.aspect = self.width / self.height
        self.hh = math.tan(self.fov / 2) * self.near
        self.hw = self.hh * self.aspect
        self.pixelsize = self.hw * 2.0 / self.width
        self.center = self.viewdirection * self.near
        self.tl = self.center - self.right * self.hw + self.up * self.hh
        self.movedirection = self.viewdirection

    def primaryRay(self, x, y):
        direction = self.tl + self.right * (self.pixelsize / 2.0) - self.upvec * (self.pixelsize / 2.0)
        direction = direction + self.right * (x * self.pixelsize) - self.up * (y * self.pixelsize)

        r = Ray(self.position, direction)
        return r

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
