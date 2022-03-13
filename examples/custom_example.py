import math

from pyrt import PerspectiveCamera, Scene, Vertex, Triangle, SimpleRT, Sphere
from pyrt.material import PhongMaterial
from pyrt.math import Vec3
from pyrt.light import SpotLight
import moviepy.editor as mpy


def create_clip(t):
    width = 400
    height = 400

    camera = PerspectiveCamera(width, height)
    camera.setView(Vec3(0., -10., 10.), Vec3(0., 0., 0.), Vec3(0., 0., 1.))

    scene = Scene()

    radius = 2.0
    p = 2 * math.pi / 4
    x = radius * math.cos(t * p)
    y = radius * math.sin(t * p)

    scene.addLight(SpotLight(position=Vec3(0, 0, 10), direction=Vec3(x, y, -10), p=10))

    floormaterial = PhongMaterial(color=Vec3(0.5, 0.5, 0.5))
    sphere0material = PhongMaterial(color=Vec3(1., 0., 0.))
    sphere1material = PhongMaterial(color=Vec3(0., 1., 0.))
    sphere2material = PhongMaterial(color=Vec3(0., 0., 1.))
    sphere3material = PhongMaterial(color=Vec3(1., 1., 0.))

    A = Vertex(position=(-5.0, -5.0, 0.0))
    B = Vertex(position=(5.0, -5.0, 0.0))
    C = Vertex(position=(5.0, 5.0, 0.0))
    D = Vertex(position=(-5.0, 5.0, 0.0))

    scene.add(Triangle(A, B, C, material=floormaterial))
    scene.add(Triangle(A, C, D, material=floormaterial))

    scene.add(Sphere(center=Vec3(-2.5, -2.5, 1.75), radius=1.75, material=sphere0material))
    scene.add(Sphere(center=Vec3(2.5, -2.5, 1.75), radius=1.75, material=sphere1material))
    scene.add(Sphere(center=Vec3(2.5, 2.5, 1.75), radius=1.75, material=sphere2material))
    scene.add(Sphere(center=Vec3(-2.5, 2.5, 1.75), radius=1.75, material=sphere3material))

    scene.setCamera(camera)

    engine = SimpleRT(shadow=True)

    image = engine.render(scene)
    return image.data

clip = mpy.VideoClip(create_clip, duration=4) # duration 4 seconds
clip.write_gif("custom_example.gif", fps=15)
