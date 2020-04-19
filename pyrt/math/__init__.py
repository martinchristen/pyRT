"""
Math for pyRT

This contains vector, matrix operations and other mathematical utils like planes, rays, ...
"""

from .constants import G_EPSILON
from .mat4 import Mat4
from .matops import *
from .ray import Ray, HitRecord
from .vec3 import Vec3
from .vec4 import Vec4
from .vecops import *
from .perlin import *
from .ops import *
