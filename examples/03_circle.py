# Example 3: **Introduction to the image class**
# This example draws 100 circles and stores the image using PIL

import sys
from pyrt.renderer import RGBImage
from pyrt.math import Vec2, Vec3
import random
from PIL import Image

sys.path.append("../")

w = 320
h = 240
image = RGBImage(w, h)

for i in range(100):
    image.drawCircle(Vec2(random.randint(0, w - 1), random.randint(0, h - 1)),
                     random.randint(3, 100),
                     Vec3(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))

image.drawCircle(Vec2(159, 119), 100, Vec3(1, 0, 0))

im = Image.new("RGB", (w, h))
im.putdata(image.data)
im.save("03.png")
