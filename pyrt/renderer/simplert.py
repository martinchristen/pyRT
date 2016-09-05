"""
A simple ray tracer

Reference implementation...
"""

from .renderer import Renderer
from ..scene import Scene
from ..math import *
import time


class SimpleRT(Renderer):
    def __init__(self):
        Renderer.__init__(self, "Simple Raytracer")

    def render(self, scene: Scene) -> list:
        if not scene.camera:
            print("Warning: Can't render: there is no (active) camera in the scene!")
            return None

        time_start = time.time()
        num_rays = 0
        hitrecord = HitRecord()

        w = scene.camera.width
        h = scene.camera.height

        haslight = len(scene.lights) > 0

        image = []
        for y in range(0, h):
            for x in range(0, w):
                ray = scene.camera.primaryRay(x, y)
                hitrecord.reset()
                num_rays += 1

                r = g = b = 0  # background color

                for element in scene.nodes:
                    if element.hit(ray, hitrecord):
                        hitrecord.obj = element # set hit object

                        # element hit -> call shader:
                        color = element.material.shade(scene.camera, ray, hitrecord, scene.lights)
                        r = int(color[0] * 255)
                        g = int(color[1] * 255)
                        b = int(color[2] * 255)

                image.append((r, g, b))

        time_end = time.time()
        print("# RENDER STATISTICS" + 31 * "#")
        time_total = time_end - time_start
        print("TIME FOR RENDERING: " + str(time_total) + "s")
        print("NUMBER OF RAYS: " + str(num_rays))
        print("RAYS/s: " + str(num_rays / time_total))
        print(50 * "#")

        return image
