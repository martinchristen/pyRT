from .renderer import *
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
        hr = HitRecord()

        w = scene.camera.width
        h = scene.camera.height

        image = []
        for y in range(0, h):
            for x in range(0, w):
                ray = scene.camera.primaryRay(x, y)
                num_rays += 1

                r = g = b = 0  # background color
                for element in scene.nodes:
                    if element.hit(ray, hr):
                        r = 255
                        g = 0
                        b = 0

                image.append((r, g, b))

        time_end = time.time()
        print("# RENDER STATISTICS" + 31 * "#")
        time_total = time_end - time_start
        print("TIME FOR RENDERING: " + str(time_total) + "s")
        print("NUMBER OF RAYS: " + str(num_rays))
        print("RAYS/s: " + str(num_rays / time_total))
        print(50 * "#")

        return image
