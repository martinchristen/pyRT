"""
A simple ray tracer

Reference implementation...
"""

from .renderer import Renderer
from ..scene import Scene
from ..math import *
import time


class SimpleRT(Renderer):
    def __init__(self, shadow=False, iterations=1):
        Renderer.__init__(self, "Simple Raytracer")
        self.shadow = shadow
        self.iterations = iterations
        if self.shadow:
            print("# Shadow Enabled")
        if self.iterations>1:
            print("# Iterations: " + str(self.iterations))

    def _shade(self, scene: Scene, ray: Ray, hitrecord: HitRecord) -> tuple:
        r = g = b = 0  # background color
        hit = False
        for element in scene.nodes:
            if element.hit(ray, hitrecord):
                hit = True
                hitrecord.obj = element  # set hit object

                # element hit -> call shader:
                color = element.material.shade(scene.camera, ray, hitrecord, scene.lights)
                r = int(color[0] * 255)
                g = int(color[1] * 255)
                b = int(color[2] * 255)

                # Calculate shadow
                if self.shadow:
                    # is hitpoint in shadow ?
                    f, n = self._shadow(scene, hitrecord)
                    self.num_shadow_rays += n
                    r = int(r * f)
                    g = int(g * f)
                    b = int(b * f)


        return hit, r, g, b

    def _shadow(self, scene: Scene, hitrecord: HitRecord) -> tuple:
        # is hitpoint in shadow ?
        fs = 1.0
        local_num_shadow_rays = 0
        numshadow = 0
        for light in scene.lights:
            shadowray = Ray(hitrecord.point, light.position - hitrecord.point)
            local_num_shadow_rays += 1
            for testelement in scene.nodes:
                if testelement != hitrecord.obj:  # avoid self-intersection
                    if testelement.hitShadow(shadowray):
                        numshadow += 1
                        break
        for i in range(numshadow):
            fs /= 4.

        return fs,local_num_shadow_rays

    def _reflect(self, r: int, g: int, b: int, scene: Scene, ray: Ray, hitrecord: HitRecord) -> tuple:
        reflect_ray = Ray(hitrecord.point, reflect3(hitrecord.normal_g, ray.direction))
        reflect_hitrecord = HitRecord()

        hit, rnew, gnew, bnew = self._shade(scene, reflect_ray, reflect_hitrecord)

        if hit:
            ref1 = hitrecord.material.reflectivity
            ref2 = 1.-ref1
            rnew = int ( ref1 * rnew + ref2 * r)
            gnew = int ( ref1 * gnew + ref2 * g)
            bnew = int ( ref1 * bnew + ref2 * b)
            return rnew, gnew, bnew, reflect_ray, reflect_hitrecord
        else:
            return r,g,b,None,None

    def render(self, scene: Scene) -> list:
        if not scene.camera:
            print("Warning: Can't render: there is no (active) camera in the scene!")
            return None

        time_start = time.time()
        self.num_rays = 0
        self.num_shadow_rays  = 0
        self.num_secondary_rays = 0
        hitrecord = HitRecord()

        w = scene.camera.width
        h = scene.camera.height

        image = []
        for y in range(0, h):
            for x in range(0, w):
                ray = scene.camera.primaryRay(x, y)
                hitrecord.reset()
                self.num_rays += 1

                # Primary Ray:
                hit, r, g, b = self._shade(scene, ray, hitrecord)

                if hit and hitrecord.material.reflectivity != 0.0:
                    refhit = hitrecord.copy()
                    refray = ray.copy()
                    for i in range(self.iterations - 1):
                        r, g, b, refray, refhit = self._reflect(r,g,b, scene, refray, refhit)
                        self.num_secondary_rays += 1
                        if refray is None:
                            break

                image.append((r, g, b))

        time_end = time.time()
        print("# RENDER STATISTICS" + 31 * "#")
        time_total = time_end - time_start
        print("TIME FOR RENDERING: " + str(time_total) + "s")
        print("NUMBER OF PRIMARY RAYS: " + str(self.num_rays))
        print("NUMBER OF SECONDARY RAYS: " + str(self.num_secondary_rays))
        print("NUMBER OF SHADOW RAYS: " + str(self.num_shadow_rays))
        print("RAYS/s: " + str((self.num_rays + self.num_secondary_rays + self.num_shadow_rays) / time_total))
        print(50 * "#")

        return image
