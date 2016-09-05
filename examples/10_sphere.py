# Example 10: Raytracing a sphere
#
# This time we render a sphere

from pyrt.math import *
from pyrt.scene import *
from pyrt.geometry import Sphere
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
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

# Add a sphere to the scene:
scene.add(Sphere(center=Vec3(0.,0.,0.), radius=3., material=PhongMaterial(color=Vec3(1.,0.,0.))))

# Now tell the scene which camera we use
scene.setCamera(camera)

# Create a raytracer using "SimpleRT"
engine = SimpleRT()

# Render the scene:
imgdata = engine.render(scene)

# Save the resulting image using pillow
im = Image.new("RGBA", (width, height))
im.putdata(imgdata)
im.save("10.png")
