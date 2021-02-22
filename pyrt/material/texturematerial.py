"""
Texture Material

For texture shading
"""
from .texture import Texture
from .material import Material
from ..math import Vec3, Ray, HitRecord, dot3, reflect3, normalize3, clamp3
from ..camera import Camera
from math import log2, floor


class TextureMaterial(Material):

    """Texture Material Class"""

    def __init__(self, color: Vec3 = Vec3(1.,1.,1.), shininess: float = 10.0, reflectivity: float = 0.0, refraction: float = 1.0,
                 texturepath: list = None):
        Material.__init__(self, color, shininess, reflectivity, refraction)
        self.texture = None \
            if texturepath is None \
            else {i: Texture(texturepath[i]) for i in range(len(texturepath))}

    def addTexture(self, lod: int, texture: Texture):
        self.texture.update({lod: texture})

    def shade(self, camera: Camera, ray: Ray, hitrecord: HitRecord,  lights: list) -> Vec3:
        """
        Shade method: Texture

        texture shader
        """
        colorsum = Vec3(0.,0.,0.)

        if self.texture is None or len(self.texture) == 0:
            texcolor = self.color
        else:
            size = camera.getSize();
            resolution = size[0] * size[1];
            lod = floor(log2((hitrecord.point - camera.position).length() / resolution) + 14)
            texcolor = self.texture[max(0, min(lod, len(self.texture) - 1))].color(hitrecord.texcoord)

        if len(lights) > 0:
            for light in lights:
                N = normalize3(hitrecord.normal_g)
                L = normalize3(hitrecord.point - light.position)
                E = normalize3(camera.position - hitrecord.point)
                R = normalize3(-reflect3(L, N))
                diffuse = max(1. - dot3(N, L), 0.0)
                specular = pow(max(dot3(R, E), 0.0), 0.3 * self.shininess)

                color = texcolor * (diffuse + specular) * hitrecord.color
                colorsum += color
            colorsum /= len(lights)
            colorsum = clamp3(colorsum, Vec3(0.,0.,0.), Vec3(1.,1.,1.))
        else:
            # no light in scene, use material color
            colorsum = texcolor * hitrecord.color

        return colorsum

