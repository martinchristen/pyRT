# Example 16: Textured raytracing
#
# This time we render a triangle
# TODO render sphere in this scene
from pyrt.light import PointLight
from pyrt.material.texturematerial import TextureMaterial
from pyrt.math import *
from pyrt.scene import *
from pyrt.geometry import Sphere
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT

from pyrt.renderer import RGBImage
from pyrt.math import Vec2, Vec3
from pyrt.camera import PerspectiveCamera
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

# Add a sphere to the scene:
scene.add(t)

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
engine = SimpleRT()

# Render the scene:
image = engine.render(scene)


image.save("16.png")
