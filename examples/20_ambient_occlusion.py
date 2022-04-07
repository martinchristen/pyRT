from pyrt.math import Vec3
from pyrt.scene import Scene
from pyrt.light import PointLight
from pyrt.geometry import Triangle, Sphere, Vertex
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT, AOSimpleRT

width = 320
height = 240

camera = PerspectiveCamera(width, height, 45)
camera.setView(Vec3(0., -10., 10.), Vec3(0., 0., 0.), Vec3(0., 0., 1.))

scene = Scene()

# Add a light to the scene
scene.addLight(PointLight(Vec3(0, -9, 20)))

# create material:
floor_material = PhongMaterial(color=Vec3(0.9, 0.9, 0.9))
sphere_material = PhongMaterial(color=Vec3(0.9, 0.9, 0.9))


# Add "floor"
A = Vertex(position=(-5.0, -5.0, 0.0))
B = Vertex(position=( 5.0, -5.0, 0.0))
C = Vertex(position=( 5.0,  5.0, 0.0))
D = Vertex(position=(-5.0,  5.0, 0.0))

scene.add(Triangle(A,B,C, material=floor_material))
scene.add(Triangle(A,C,D, material=floor_material))

# Add spheres

scene.add(Sphere(center=Vec3(0, 1, 1), radius=1, material=sphere_material))
scene.add(Sphere(center=Vec3(2, 1, 1), radius=1, material=sphere_material))
scene.add(Sphere(center=Vec3(-2, 1, 1), radius=1, material=sphere_material))

scene.add(Sphere(center=Vec3(-1, -1, 1), radius=1, material=sphere_material))
scene.add(Sphere(center=Vec3(1, -1, 1), radius=1, material=sphere_material))

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
simple_engine = SimpleRT(shadow=True, iterations=3)
ao_engine = AOSimpleRT(shadow=True, iterations=3, n_aorays=100)

# Render the scene:
image_simple = simple_engine.render(scene)
image_ao = ao_engine.render(scene)

# Save the resulting image using pillow
image_simple.save("20_0.png")
image_ao.save("20_1.png")
