# Example 12: small scene
#
# This time we render a small scene with shadow

from pyrt.math import Vec3
from pyrt.scene import Scene
from pyrt.light import PointLight
from pyrt.geometry import Triangle, Sphere, Vertex
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT
from PIL import Image
import moviepy.editor as mpy    # pip install moviepy
import numpy as np
from math import *

def make_frame(t):
    # Specify width/height as in example 5
    width = 320
    height = 240

    # now create a camera and a view like in example 5:
    camera = PerspectiveCamera(width, height, 45)
    camera.setView(Vec3(0.,-10.,10.), Vec3(0.,0.,0.), Vec3(0.,0.,1.))

    # Create a scene
    scene = Scene()

    # Add a light to the scene
    radius = 3.0
    p = 2*pi/4
    x = radius * cos(t*p)
    y = radius * sin(t*p)

    scene.addLight(PointLight(Vec3(x, y, 10)))


    # create some materials:
    floormaterial = PhongMaterial(color=Vec3(0.5,0.5,0.5))
    sphere0material = PhongMaterial(color=Vec3(1.,0.,0.))
    sphere1material = PhongMaterial(color=Vec3(0.,1.,0.))
    sphere2material = PhongMaterial(color=Vec3(0.,0.,1.))
    sphere3material = PhongMaterial(color=Vec3(1.,1.,0.))

    # Add "floor"

    A = Vertex(position=(-5.0, -5.0, 0.0))
    B = Vertex(position=( 5.0, -5.0, 0.0))
    C = Vertex(position=( 5.0,  5.0, 0.0))
    D = Vertex(position=(-5.0,  5.0, 0.0))

    scene.add(Triangle(A,B,C, material=floormaterial))
    scene.add(Triangle(A,C,D, material=floormaterial))

    # Add some spheres

    scene.add(Sphere(center=Vec3(-2.5,-2.5,1.75), radius=1.75, material=sphere0material))
    scene.add(Sphere(center=Vec3( 2.5,-2.5,1.75), radius=1.75, material=sphere1material))
    scene.add(Sphere(center=Vec3( 2.5, 2.5,1.75), radius=1.75, material=sphere2material))
    scene.add(Sphere(center=Vec3(-2.5, 2.5,1.75), radius=1.75, material=sphere3material))

    # Now tell the scene which camera we use
    scene.setCamera(camera)

    # Create a raytracer using "SimpleRT"
    engine = SimpleRT(shadow=True)

    # Render the scene:
    imgdata = engine.render(scene)

    im = Image.new("RGB", (width, height))
    im.putdata(imgdata)
    return np.asarray(im)


clip = mpy.VideoClip(make_frame, duration=4) # duration 4 seconds
clip.write_gif("12b.gif",fps=15)
