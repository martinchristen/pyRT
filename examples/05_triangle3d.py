# Example 6: **Matrix, Camera, Triangle**
# In this example you learn how 3D transformation works
# In addition to example 5, an animated gif is created using Pillow

import sys

from pyrt.renderer import RGBImage
from pyrt.math import Vec2, Vec3
from pyrt.camera import PerspectiveCamera
from pyrt.geometry import Triangle, Vertex
from PIL import Image

sys.path.append("../")


w = 320
h = 240
image = RGBImage(w, h)

# Create a camere with width, height and field of view:
camera = PerspectiveCamera(w,h,60)

# Set View matrix of camera: define where to look at
camera.setView(Vec3(0,-10,0), Vec3(0,0,0), Vec3(0,0,1))

#  Create view-projection matrix (right to left)
vp =  camera.projection * camera.view

# Create a triangle
t = Triangle(Vertex(position=(-5, 1, 0)),
             Vertex(position=(0, 1, 5)),
             Vertex(position=(5, 1, 0)))

# Triangle in normalized device coordinates:
at = vp * t.a.position
bt = vp * t.b.position
ct = vp * t.c.position

# Triangle in Screen coordinates:
a_screenpos = Vec2(int(w * 0.5*(at.x + 1.) / at.z), int(h * 0.5*(at.y + 1.)/ at.z))
b_screenpos = Vec2(int(w * 0.5*(bt.x + 1.) / bt.z), int(h * 0.5*(bt.y + 1.)/ at.z))
c_screenpos = Vec2(int(w * 0.5*(ct.x + 1.) / ct.z), int(h * 0.5*(ct.y + 1.)/ at.z))

# Draw the Triangle (wireframe) in image:
color = Vec3(1,1,1)
image.drawLine(a_screenpos, c_screenpos, color)
image.drawLine(c_screenpos, b_screenpos, color)
image.drawLine(b_screenpos, a_screenpos, color)

print(a_screenpos)
print(b_screenpos)
print(c_screenpos)


im = Image.new("RGB", (w, h))
im.putdata(image.data)
im.save("05.png")
