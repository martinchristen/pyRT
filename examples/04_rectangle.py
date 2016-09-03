# Example 3: **Introduction to the image class**
# This example draws 20 rectangles and stores the image using PIL

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
    image.drawRectangle(Vec2(random.randint(0, w - 1), random.randint(0, h - 1)),
                        random.randint(1, w / 2), random.randint(1, h / 2),
                        Vec3(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))

im = Image.new("RGB", (w, h))
im.putdata(image.data)
im.save("04.png")
