"""
Phong Material

For phong shading
"""

from abc import abstractmethod
from .material import Material
from ..math import Vec3, Ray, HitRecord, dot3, reflect3, normalize3
from ..camera import Camera


class PhongMaterial(Material):

    """Base Material Class"""

    def __init__(self, color: Vec3 = Vec3(0.,0.,0.), shininess: float = 0.0, reflectivity: float = 0.5, refraction: float = 1.0):
        Material.__init__(self, color, shininess, reflectivity, refraction)

    def shade(self, camera: Camera, ray: Ray, hitrecord: HitRecord,  lights: list) -> Vec3:
        """
        Shade method: Phong

        phong shader
        """
        N = hitrecord.normal_g
        L = normalize3(hitrecord.point - lights[0].position)
        E = normalize3(camera.position - hitrecord.point)
        R = normalize3(-reflect3(L, N))
        diffuse = max(1. - dot3(N, L), 0.0)
        specular = pow(max(dot3(R, E), 0.0), 0.3 * self.shininess)
        color = self.color * 0.5 * (diffuse + specular)

        return color

