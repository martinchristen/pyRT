# Example 2: **Introduction to the image class**
# This example draws two Koch (snowflake) curves

import sys
sys.path.append("../")

from pyrt.renderer import RGBImage
from pyrt.math import Vec2, Vec3
import math
from PIL import Image

def snowflake(image: Image, lev: int, x1 : int, y1 : int, x5:int, y5: int, color : Vec3)  -> None:
    if lev == 0:
        image.drawLine(Vec2(x1, y1), Vec2(x5, y5), color)
    else:
        deltaX = x5-x1
        deltaY = y5-y1

        x2 = int(x1+deltaX/3.)
        y2 = int(y1+deltaY/3.)

        x3 = int(0.5*(x1+x5)+math.sqrt(3.)*(y1-y5)/6.)
        y3 = int(0.5*(y1+y5)+math.sqrt(3.)*(x5-x1)/6.)

        x4 = int(x1+2.*deltaX/3.)
        y4 = int(y1+2.*deltaY/3.)

        snowflake(image, lev - 1, x1, y1, x2, y2,color)
        snowflake(image, lev - 1, x2, y2, x3, y3,color)
        snowflake(image, lev - 1, x3, y3, x4, y4,color)
        snowflake(image, lev - 1, x4, y4, x5, y5,color)


w = 512
h = 512
image = RGBImage(w,h)

level = 5  # Change max recursion depth here

snowflake(image,level,0, 255, 511, 255, Vec3(1,0,0))

im = Image.new("RGB", (w,h))
im.putdata(image.data)
im.save("02.png")




