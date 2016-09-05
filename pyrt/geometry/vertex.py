"""
Here the vertex is defined

The following attributes are supported:
  * position
  * normal
  * color
  * texcoord
"""

from ..math import *


class Vertex(object):
    def __init__(self, **kwargs):
        self.position = Vec3(0, 0, 0)
        self.normal = None
        self.color = Vec3(1.,1.,1.)
        self.texcoord = None

        if len(kwargs) == 0:
            raise ValueError("Vertex must specify attributes, for example: position, normal, color, texcoord")
        else:

            if "position" in kwargs:
                if type(kwargs["position"]) == Vec3:
                    self.position = kwargs["position"].copy()
                elif type(kwargs["position"]) == tuple or type(kwargs["position"]) == list:
                    if len(kwargs["position"]) != 3:
                        raise ValueError("position must be specified as Vec3 or a list/tuple")
                    else:
                        self.position = Vec3(kwargs["position"][0], kwargs["position"][1], kwargs["position"][2])
                else:
                    raise ValueError("position must be specified as Vec3 or a list/tuple")

            if "normal" in kwargs:
                if type(kwargs["normal"]) == Vec3:  # TODO: a list/tuple of values is ok too...
                    self.normal = kwargs["normal"].copy()
                elif type(kwargs["normal"]) == tuple or type(kwargs["normal"]) == list:
                    if len(kwargs["normal"]) != 3:
                        raise ValueError("normal must be specified as Vec3 or a list/tuple with 3 floats")
                    else:
                        self.normal = Vec3(kwargs["position"][0], kwargs["position"][1], kwargs["position"][2])
                else:
                    raise ValueError("normal must be specified as Vec3 or a list/tuple")

            if "color" in kwargs:
                if type(kwargs["color"]) == Vec4:
                    raise ValueError("Color must be Vec3")
                elif type(kwargs["color"]) == Vec3:
                    color = kwargs["color"]
                    self.color = Vec3(color.x, color.y, color.z)
                elif type(kwargs["color"]) == tuple or type(kwargs["color"]) == list:
                    color = kwargs["color"]
                    if len(color) == 3:
                        self.color = Vec3(color[0], color[1], color[2])
                    else:
                        raise ValueError("Wrong number of components for color")
                else:
                    raise ValueError("color must be specified as Vec3 or list/tuple with 3 components")

            '''
            if "texcoord" in kwargs:
                if type(kwargs["texcoord"]) == Vec2:
                    pass
                elif type(kwargs["texcoord"]) == tuple or type(kwargs["texcoord"]) == list:
                else:
                    raise ValueError("position must be specified as Vec2 or list/tuple")
            '''
