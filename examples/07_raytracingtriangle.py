# Example 7: Raytracing a single triangle
#
# This example generates a scene equivalent to the experiment of Example 5 (and 6)

from pyrt.math import *
from pyrt.scene import *
from pyrt.geometry import Triangle, Vertex
from pyrt.camera import OrthographicCamera, PerspectiveCamera
from pyrt.renderer import SimpleRT
from PIL import Image


# Specify width/height as in example 5
width = 320
height = 240

# now create a camera and a view like in example 5:
camera = PerspectiveCamera(width, height, 60)
camera.setView(Vec3(0,-10,0), Vec3(0,0,0), Vec3(0,0,1))

# Create a scene
scene = Scene()

# Add a triangle (same as example 5) to the scene:
scene.add(Triangle(Vertex(position=(-5, 1, 0)),
                   Vertex(position=(0, 1, 5)),
                   Vertex(position=(5, 1, 0))))

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
engine = SimpleRT()

# Render the scene:
image = engine.render(scene)

image.save("07.png")
