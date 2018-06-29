from pyrt.math import Vec3
from pyrt.scene import Scene
from pyrt.light import PointLight
from pyrt.geometry import Triangle, Sphere, Vertex, TriangleMesh
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT

# Specify width/height as in example 5
width = 320
height = 240

# now create a camera and a view like in example 5:
camera = PerspectiveCamera(width, height, 45)
camera.setView(Vec3(0.,-10.,10.), Vec3(0.,0.,0.), Vec3(0.,0.,1.))

# Create a scene
scene = Scene()

trimesh = TriangleMesh()
trimesh.load("../data/teapot_simple/teapot.obj")

print(trimesh.stats())

center = trimesh.getCentroid()
print(center)

bbox = trimesh.getBBox()
print(bbox)