# Example 11: Raytracing a sphere with light
#
# This time we render a sphere and add a light to the scene

from pyrt.math import Vec3
from pyrt.scene import Scene
from pyrt.light import PointLight
from pyrt.geometry import Triangle, Sphere, Vertex
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT
from PIL import Image

# Specify width/height as in example 5
width = 320
height = 240

# now create a camera and a view like in example 5:
camera = PerspectiveCamera(width, height, 45)
camera.setView(Vec3(0.,-10.,10.), Vec3(0.,0.,0.), Vec3(0.,0.,1.))

# Create a scene
scene = Scene()

# Add a light to the scene
scene.addLight(PointLight(Vec3(0,0,15)))

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

# Save the resulting image using pillow
im = Image.new("RGBA", (width, height))
im.putdata(imgdata)
im.save("12.png")
