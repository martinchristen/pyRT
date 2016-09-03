# Example 1: **Introduction to the image class**
# This example draws 5000 points and stores the image using PIL

import sys
sys.path.append("../")


from pyrt.renderer import RGBImage
from pyrt.math import Vec2, Vec3
import random
from PIL import Image

w = 320
h = 240
image = RGBImage(w,h)

for i in range(5000):
    image.drawPoint(Vec2(random.randint(0,w-1), random.randint(0,h-1)), Vec3(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))

im = Image.new("RGB", (w,h))
im.putdata(image.data)
im.save("00.png")


