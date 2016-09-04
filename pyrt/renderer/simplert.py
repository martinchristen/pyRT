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
        hr = HitRecord()

        w = scene.camera.width
        h = scene.camera.height

        haslight = len(scene.lights) > 0

        shininess = 10.  # temp... -> material defintion follows later...

        image = []
        for y in range(0, h):
            for x in range(0, w):
                ray = scene.camera.primaryRay(x, y)
                num_rays += 1

                r = g = b = 0  # background color
                # TODO: handle multiple objects correctly
                for element in scene.nodes:
                    if element.hit(ray, hr):
                        if haslight:
                            # a material definition is still missing, so I do some odd things...
                            N = hr.normal_g
                            L = normalize3(hr.point - scene.lights[0].position)
                            E = normalize3(scene.camera.origin - hr.point)
                            R = normalize3(-reflect3(L, N))
                            diffuse = max(1. - dot3(N, L), 0.0)
                            specular = pow(max(dot3(R,E),0.0),0.3*shininess)
                            color = hr.color * 0.5 * (diffuse + specular)
                            r = int(color.x * 255)
                            g = int(color.y * 255)
                            b = int(color.z * 255)
                        else:
                            r = int(hr.color.x*255)
                            g = int(hr.color.y*255)
                            b = int(hr.color.z*255)

                image.append((r, g, b))

        time_end = time.time()
        print("# RENDER STATISTICS" + 31 * "#")
        time_total = time_end - time_start
        print("TIME FOR RENDERING: " + str(time_total) + "s")
        print("NUMBER OF RAYS: " + str(num_rays))
        print("RAYS/s: " + str(num_rays / time_total))
        print(50 * "#")

        return image
