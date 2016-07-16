# Matrix Operations

import math
from .vec2 import *
from .vec3 import *
from .vec4 import *
from .mat4 import *


def CreateIdentity4():
    return Mat4((1,0,0,0,
                 0,1,0,0,
                 0,0,1,0,
                 0,0,0,1))

