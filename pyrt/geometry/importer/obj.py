"""
Simple Wavefront OBJ Importer


There are some restrictions:
- obj must be triangulated
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
    geometry = state["geometry"]


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

    elif line[0:1] == "o": # object group
        o = line[1:len(line)].strip()
        state["curobject"] = o

    elif line[0:1] == "g": # polygon group
        g = line[1:len(line)].strip()
        state["curgroup"] = g

    elif line[0:6] == "usemtl":
        m = line[6:len(line)].strip()
        state["curmaterial"] = m

    elif line[0:1] == "f":

        curobject = state["curobject"]
        curgroup = state["curgroup"]

        if not curobject in geometry:
            geometry[curobject] = {}

        if not curgroup in geometry[curobject]:
            geometry[curobject][curgroup] = {"positions": [], "texcoords": [], "normals": []}

        f = line[1:len(line)].strip()
        f = f.split(" ")

        if len(f) != 3:
            raise ImportError("Currently only triangulated OBJ files are supported")

        indexlist = []
        for element in f:
            vec = element.split("/")
            n = []
            for i in vec:
                try:
                    n.append(int(i))
                except:
                    n.append(0)     # 0 means "NO DATA"
            while len(n) != 3:
                n.append(0)         # 0 means "NO DATA"

            indexlist.append(n)

        for index in indexlist:
            position = index[0]
            texcoord = index[1]
            normal = index[2]

            if position == 0:
                raise ImportError("position not defined in face list")
            elif position>0:
                position -= 1

            vertices = state["raw_vertices"]

            vertex = vertices[position]
            for coord in vertex:
                geometry[curobject][curgroup]["positions"].append(coord)

            tc = True
            if texcoord == 0:
                tc = False
            elif texcoord>0:
                texcoord -= 1


            texcoords = state["raw_texcoords"]
            if tc:
                txcoord = texcoords[texcoord]
                for coord in txcoord:
                    geometry[curobject][curgroup]["texcoords"].append(coord)


            norm = True
            if normal == 0:
                norm = False
            elif normal>0:
                normal -= 1

            normals = state["raw_normals"]
            if norm:
                ncoord = normals[normal]
                for coord in ncoord:
                    geometry[curobject][curgroup]["normals"].append(coord)






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
    parsestate["geometry"] = {}

    parsestate["curobject"] = str(uuid.uuid4())[0:8]
    parsestate["curgroup"] = str(uuid.uuid4())[0:8]
    parsestate["curmaterial"] = ""


    if debug:
        print("processing: " + name + " in directory " + path)


    file = open(filename, "r")
    for line in file:
        line = line.rstrip()

        if line[0:1] != '#':  # only parse line if it is not a comment
            _obj_parse(line, parsestate)

    file.close()


    # remove temporary info which was required for parsing:
    del parsestate["file"]
    del parsestate["raw_vertices"]
    del parsestate["raw_normals"]
    del parsestate["raw_texcoords"]
    del parsestate["curobject"]
    del parsestate["curgroup"]
    del parsestate["curmaterial"]


    if debug:
        import pprint
        print("PARSED OUTPUT:")

        #pp = pprint.PrettyPrinter(depth=4)
        pp = pprint.PrettyPrinter(depth=10)
        pp.pprint(parsestate)


#-----------------------------------------------------------------------------------------------------------------------