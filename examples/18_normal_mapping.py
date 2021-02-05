# Example 18: Normal mappings
#
# Two spheres are rendered, one with normal map and the other without it

from pyrt.math import Vec3
from pyrt.scene import Scene
from pyrt.light import PointLight
from pyrt.geometry import Triangle, Sphere, Vertex
from pyrt.material import NormalMappedMaterial, TextureMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT
from PIL import Image

# Specify width/height
width = 400
height = 300

# now create a camera and a view like in example 5:
camera = PerspectiveCamera(width, height, 60)
camera.setView(Vec3(0,-10,0), Vec3(0,0,0), Vec3(0,0,1))

# Create a scene
scene = Scene()

# Add a light to the scene
scene.addLight(PointLight(Vec3(0,0,0)))

# Create material with normal mappings
material0 = NormalMappedMaterial(texturepath='tex16.png', normalmappath='normalmap.png')
material1 = TextureMaterial(texturepath='tex16.png')

# Add spheres to the scene:
scene.add(Sphere(center=Vec3(-3.5,0.,0.), radius=2.8, material=material0))
scene.add(Sphere(center=Vec3(3.5,0.,0.), radius=2.8, material=material1))

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
engine = SimpleRT()

# Render the scene:
image = engine.render(scene)

# Save the resulting image using pillow
image.save("18.png")
