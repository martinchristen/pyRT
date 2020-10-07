"""
A multi processing ray tracer
"""

from .rgbimage import *
from .renderer import Renderer
from ..scene import Scene
from ..math import *

from .simplert import SimpleRT

from multiprocessing import Pool
import time


class MultiProcessRT(SimpleRT):

    def __init__(self, shadow=False, iterations=1):
        Renderer.__init__(self, "MP Raytracer")
        self.shadow = shadow
        self.iterations = iterations
        if self.shadow:
            print("# Shadow Enabled")
        if self.iterations>1:
            print("# Iterations: " + str(self.iterations))


    def trace_ray_multiprocess(engine, scene, x, y):
        ray = scene.camera.primaryRay(x, y)
        hitrecord = HitRecord()
        engine.num_rays += 1

        # Reset shadow rays for the process
        engine.num_shadow_rays = 0
      
        num_secondary_rays = 0

        # Primary Ray:
        hit, r, g, b = engine._shade(scene, ray, hitrecord)

        if hit and hitrecord.material.reflectivity != 0.0:
            refhit = hitrecord.copy()
            refray = ray.copy()
            for i in range(engine.iterations - 1):
                r, g, b, refray, refhit = engine._reflect(r,g,b, scene, refray, refhit)
                num_secondary_rays += 1
                if refray is None:
                    break

        return x, y, r, g, b, num_secondary_rays, engine.num_shadow_rays

    def render(self, scene: Scene) -> RGBImage:
        if not scene.camera:
            print("Warning: Can't render: there is no (active) camera in the scene!")
            return None

        time_start = time.time()
        self.num_shadow_rays = 0
        self.num_secondary_rays = 0

        w = scene.camera.width
        h = scene.camera.height

        self.num_rays = w * h

        image = RGBImage(w,h)
        
        args = []
        for y in range(0, h):
            for x in range(0, w):
                args.append([scene, x, y])

        with Pool() as p:
            for result in p.starmap(self.trace_ray_multiprocess, args):
                x, y, r, g, b, secondary_rays, shadow_rays = result
                image.drawPixelFast8(x, y, r, g, b)
                self.num_secondary_rays += secondary_rays
                self.num_shadow_rays += shadow_rays

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
