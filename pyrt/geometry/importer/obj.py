"""
Simple Wavefront OBJ Importer


There are some restrictions:
- obj must be triangulated
- every group returns a TriangleMesh
- only single file obj are supported
- material file and obj file must be in same directory
- filenames of textures must be relative to the material/obj file


"""

from ..vertex import *
from ..triangle import *
from ..trianglemesh import *

import os.path


#-----------------------------------------------------------------------------------------------------------------------
def _mat_parse(materialfile, state):
    matfile = open(materialfile, "r")


    curmtl = ""
    materials = state["materials"]

    for line in matfile:
        line = line.strip()

        if line[0:1] == "#":
            pass # ignore comment...
        elif line[0:6] == "newmtl":
            newmtl = line.split(" ")
            if len(newmtl) == 2:
                curmtl = newmtl[1]
                materials[curmtl] = {}
                print("found material: " + curmtl)
        elif line[0:2] == "Ns":
            m = line.split(" ")
            materials[curmtl]["Ns"] = m[1]
        elif line[0:2] == "Ni":
            m = line.split(" ")
            materials[curmtl]["Ni"] = m[1]
        elif line[0:2] == "Tr":
            m = line.split(" ")
            materials[curmtl]["Tr"] = m[1]
        elif line[0:2] == "Ka":
            m = line.split(" ")
            materials[curmtl]["Ka"] = m[1]
        elif line[0:2] == "Kd":
            m = line.split(" ")
            materials[curmtl]["Kd"] = m[1]
        elif line[0:2] == "Ks":
            m = line.split(" ")
            materials[curmtl]["Ks"] = m[1]
        elif line[0:2] == "Ke":
            m = line.split(" ")
            materials[curmtl]["Ke"] = m[1]
        elif line[0:6] == "map_Kd":
            m = line.split(" ")
            materials[curmtl]["map_Kd"] = state["file"][1] + m[1]
        elif line[0:5] == "illum":
            m = line.split(" ")
            materials[curmtl]["illum"] = m[1]



    matfile.close()


#-----------------------------------------------------------------------------------------------------------------------
def _obj_parse(line, state):
    if line[0:6] == "mtllib":
        materialfile = line.split(" ")
        if len(materialfile) == 2:
            materialfile = materialfile[1]
            materialfile = state["file"][1] + materialfile
            _mat_parse(materialfile, state)

    elif line[0:2] == "v ":
        v = line.split(" ")
        state["raw_vertices"].append([float(v[1]), float(v[2]), float(v[3])])

    elif line[0:2] == "vt":
        vt = line.split(" ")
        state["raw_texcoords"].append([float(vt[1]), float(vt[2])])

    elif line[0:2] == "vn":
        vn = line.split(" ")
        state["raw_normals"].append([float(vn[1]), float(vn[2]), float(vn[3])])


    #-----------------------------------------------------------------------------------------------------------------------
def loadObj(filename: str) -> TriangleMesh:
    parsestate = {}

    path, name = os.path.split(filename)
    path = os.path.join(path, '')

    parsestate["materials"] = {}
    parsestate["raw_vertices"] = []
    parsestate["raw_normals"] = []
    parsestate["raw_texcoords"] = []
    parsestate["file"] = [name, path]


    print("processing: " + name + " in directory " + path)

    file = open(filename, "r")
    for line in file:
        line = line.rstrip()


        if line[0:1] != '#':  # not a comment
            _obj_parse(line, parsestate)

    file.close()


    # remove temporary info which was required for parsing:
    # del parsestate["file"]
    # del parsestate["raw_vertices"]
    # del parsestate["raw_normals"]
    # del parsestate["raw_texcoords"]


    import pprint
    print("PARSED OUTPUT:")

    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(parsestate)


#-----------------------------------------------------------------------------------------------------------------------