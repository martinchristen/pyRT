"""
This is the geometric object trianglemesh

(renderable object).
"""

from ..geometry import Shape, Vertex, BBox
from ..material import PhongMaterial
from ..math import *


class TriangleMesh(Shape):
    def __init__(self):
        Shape.__init__(self, "TriangleMesh")

        self.vertices = []
        self.faces = []



    def stats(self):
        """
        Return a status string about the triangle mesh

        :return:
        """
        return "vertices: {}, faces: {}".format(len(self.vertices), len(self.faces))

    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        """
        :param ray: the ray to check hit
        :param tmin: tmin to test intersection
        :param tmax: tmax to test intersection
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        """
        pass

    def hitShadow(self, ray: Ray) -> bool:
        """
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        """
        pass


    def getBBox(self):
        """
        Retrieve axis aligned bounding box of the triangle mesh

        :return: bounding box
        """

        bbmin = Vec3(1e20, 1e20, 1e20)
        bbmax = Vec3(-1e20, -1e20, -1e20)

        for xyz in self.vertices:
            if xyz[0] <= bbmin[0]:
                bbmin[0] = xyz[0]
            if xyz[0] >= bbmax[0]:
                bbmax[0] = xyz[0]

            if xyz[1] <= bbmin[1]:
                bbmin[1] = xyz[1]
            if xyz[1] >= bbmax[1]:
                bbmax[1] = xyz[1]

            if xyz[2] <= bbmin[2]:
                bbmin[2] = xyz[2]
            if xyz[2] >= bbmax[2]:
                bbmax[2] = xyz[2]

        return BBox(bbmin, bbmax)

    def getCentroid(self) -> Vec3:
        """
        Retrieve centroid of triangle mesh
        :return:
        """

        oon = 1.0/float(len(self.vertices))
        center = Vec3(0,0,0)
        for xyz in self.vertices:
            center[0] += xyz[0] * oon
            center[1] += xyz[1] * oon
            center[2] += xyz[2] * oon

        return center

    def getSurfaceArea(self) -> float:
        """
        Retrieve Surface area of the triangle mesh (area of all triangles)

        :return: surface area
        """
        return 0

    def load(self, filename):
        """
        Load 3d object from file (obj format).
        (Please note that a triangle mesh is not a scene! Only single material, single meshes are imported.)
        (also, the importer is really simple. Meshes must be triangulated before!!)

        :param filename: filename of the 3d object
        :return: nothing
        """

        file3d = open(filename, "r")
        for line in file3d:
            data = line.split(" ")
            if len(data)>2:
                if data[0] == "v" and len(data) == 4:
                    self.vertices.append([float(data[1]), float(data[2]), float(data[3])])
                if data[0] == "f" and len(data) == 4:   # data must be triangulated, no tex/normals
                    self.faces.append([int(data[1]), int(data[2]), int(data[3])])

