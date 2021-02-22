from .texture import Texture
from .texturematerial import TextureMaterial
from ..math import Vec3, Ray, HitRecord, dot3, reflect3, normalize3, clamp3
from ..camera import Camera


class NormalMappedMaterial(TextureMaterial):
    """Texture Material Class"""

    def __init__(self, color: Vec3 = Vec3(1., 1., 1.), shininess: float = 10.0, reflectivity: float = 0.0,
                 refraction: float = 1.0, texturepath: str = '', normalmappath: str = ''):
        TextureMaterial.__init__(self, color, shininess, reflectivity, refraction, texturepath)
        self.normalmap = None if len(normalmappath) == 0 else Texture(normalmappath)

    def shade(self, camera: Camera, ray: Ray, hitrecord: HitRecord, lights: list) -> Vec3:
        """
        Shade method: Texture

        texture shader
        """
        diff = 2 * (self.normalmap.color(hitrecord.texcoord) - Vec3(0.5, 0.5, 0.5))
        hitrecord.normal_g = normalize3(diff)
        return super().shade(camera, ray, hitrecord, lights)