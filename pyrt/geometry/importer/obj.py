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
import uuid



#-----------------------------------------------------------------------------------------------------------------------
# Parse Material file
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
            materials[curmtl]["Ns"] = float(m[1])
        elif line[0:2] == "Ni":
            m = line.split(" ")
            materials[curmtl]["Ni"] = float(m[1])
        elif line[0:2] == "Tr":
            m = line.split(" ")
            materials[curmtl]["Tr"] = float(m[1])
        elif line[0:2] == "d":
            m = line.split(" ")
            materials[curmtl]["Tr"] = 1. - float(m[1])
        elif line[0:2] == "Ka":
            m = line.split(" ")
            materials[curmtl]["Ka"] = float(m[1])
        elif line[0:2] == "Kd":
            m = line.split(" ")
            materials[curmtl]["Kd"] = float(m[1])
        elif line[0:2] == "Ks":
            m = line.split(" ")
            materials[curmtl]["Ks"] = float(m[1])
        elif line[0:2] == "Ke":
            m = line.split(" ")
            materials[curmtl]["Ke"] = float(m[1])
        elif line[0:6] == "map_Ka":
            m = line.split(" ")
            materials[curmtl]["map_Ka"] = state["file"][1] + m[1]
        elif line[0:6] == "map_Kd":
            m = line.split(" ")
            materials[curmtl]["map_Kd"] = state["file"][1] + m[1]
        elif line[0:6] == "map_Ks":
            m = line.split(" ")
            materials[curmtl]["map_Ks"] = state["file"][1] + m[1]
        elif line[0:8] == "map_bump" or line[0:4] == "bump":
            m = line.split(" ")
            materials[curmtl]["map_bump"] = state["file"][1] + m[1]
        elif line[0:4] == "disp":
            m = line.split(" ")
            materials[curmtl]["map_disp"] = state["file"][1] + m[1]
        elif line[0:5] == "illum":
            m = line.split(" ")
            materials[curmtl]["illum"] = int(m[1])
            # Illum:
            #  0: Color on and Ambient off
            #  1: Color on and Ambient on
            #  2: Highlight on
            #  3: Reflection on and Ray trace on
            #  4: Transparency: Glass on, Reflection: Ray trace on
            #  5: Reflection: Fresnel on and Ray trace on
            #  6: Transparency: Refraction on, Reflection: Fresnel off and Ray trace on
            #  7: Transparency: Refraction on, Reflection: Fresnel on and Ray trace on
            #  8: Reflection on and Ray trace off
            #  9: Transparency: Glass on, Reflection: Ray trace off
            # 10: Casts shadows onto invisible surfaces


    matfile.close()


#-----------------------------------------------------------------------------------------------------------------------
def _obj_parse(line, state):
    curgroup = str(uuid.uuid4())[0:8]
    if line[0:6] == "mtllib":
        materialfile = line.split(" ")
        if len(materialfile) == 2:
            materialfile = materialfile[1]
            materialfile = state["file"][1] + materialfile
            _mat_parse(materialfile, state)

    elif line[0:2] == "v ":
        v = line[1:len(line)].strip()
        v = v.split(" ")
        state["raw_vertices"].append([float(v[0]), float(v[1]), float(v[2])])

    elif line[0:2] == "vt":
        vt = line[2:len(line)].strip()
        vt = vt.split(" ")
        state["raw_texcoords"].append([float(vt[0]), float(vt[1])])

    elif line[0:2] == "vn":
        vn = line[2:len(line)].strip()
        vn = vn.split(" ")
        state["raw_normals"].append([float(vn[0]), float(vn[1]), float(vn[2])])

    elif line[0:1] == "g":
        g = line[1:len(line)].strip()
        curgroup = g

    elif line[0:1] == "f":
        f = line[1:len(line)].strip()
        f = f.split(" ")

        #if len(f) != 3:
        #    print("ERROR: Currently only triangulated objects are supported")


    #-----------------------------------------------------------------------------------------------------------------------
def loadObj(filename: str, debug: bool = False) -> TriangleMesh:
    parsestate = {}

    path, name = os.path.split(filename)
    path = os.path.join(path, '')

    parsestate["materials"] = {}
    parsestate["raw_vertices"] = []
    parsestate["raw_normals"] = []
    parsestate["raw_texcoords"] = []
    parsestate["file"] = [name, path]

    if debug:
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


    if debug:
        import pprint
        print("PARSED OUTPUT:")

        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(parsestate)


#-----------------------------------------------------------------------------------------------------------------------