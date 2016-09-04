# Example 2: **Introduction to the image class**
# This example draws 500 lines and stores the image using PIL

from pyrt.renderer import RGBImage
from pyrt.math import Vec2, Vec3
import random

from pyrt.utils import CreatePPM

w = 320
h = 240
image = RGBImage(w, h)

for i in range(500):
    image.drawLine(Vec2(random.randint(0, w - 1), random.randint(0, h - 1)),
                   Vec2(random.randint(0, w - 1), random.randint(0, h - 1)),
                   Vec3(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))



CreatePPM("01.ppm",(w,h),image.data)