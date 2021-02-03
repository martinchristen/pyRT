# Example 16: Textured raytracing
#
# This time we render a triangle and scene

from pyrt.light import PointLight
from pyrt.scene import *
from pyrt.geometry import Sphere
from pyrt.material.texturematerial import TextureMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT

from pyrt.renderer import RGBImage
from pyrt.math import Vec3
from pyrt.geometry import Triangle, Vertex
from PIL import Image


w = 320
h = 240

# Create a camera with width, height and field of view:
camera = PerspectiveCamera(w, h, 60)

# Set View matrix of camera: define where to look at
camera.setView(Vec3(0, -10, 0), Vec3(0, 0, 0), Vec3(0, 0, 1))

#  Create view-projection matrix (right to left)
vp =  camera.projection * camera.view

# Create a scene
scene = Scene()

# Add a light to the scene
scene.addLight(PointLight(Vec3(0, -5, 0)))

# Create a triangle
t = Triangle(Vertex(position=(-5, 1, 0), texcoord=(0, 0)),
             Vertex(position=(0, 1, 5), texcoord=(1, 0)),
             Vertex(position=(5, 1, 0), texcoord=(1, 1)),
             material=
             TextureMaterial(texturepath='tex16.png'))

s = Sphere(center=Vec3(0, -3, 0), radius=1,
           material=
           TextureMaterial(texturepath='tex16.png'))

# Add triangle and sphere to the scene:
scene.add(t)
scene.add(s)

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
engine = SimpleRT()

# Render the scene:
image = engine.render(scene)


image.save("16.png")
