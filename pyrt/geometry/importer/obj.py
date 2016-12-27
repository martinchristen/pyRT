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
            pass



    matfile.close()


#-----------------------------------------------------------------------------------------------------------------------
def _obj_parse(line, state):
    if line[0:6] == "mtllib":
        materialfile = line.split(" ")
        if len(materialfile) == 2:
            materialfile = materialfile[1]
            materialfile = state["file"][1] + materialfile
            _mat_parse(materialfile, state)



#-----------------------------------------------------------------------------------------------------------------------
def loadObj(filename: str) -> TriangleMesh:
    parsestate = {}

    path, name = os.path.split(filename)
    path = os.path.join(path, '')

    parsestate["materials"] = {}
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


    import pprint
    print("PARSED OUTPUT:")

    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(parsestate)


#-----------------------------------------------------------------------------------------------------------------------