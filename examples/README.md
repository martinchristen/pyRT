# pyRT Examples

For the examples you need "pillow" installed.

## Using 'pyrt.image'

The first series of examples is just about images and drawing into them. It is not about raytracing yet.
It is important to understand the concept of an "image generator". 
While most graphics applications draw something on the screen, in pyRT there is no interactive window displaying anything.
Images are for example generated as list of RGB tuples, which are then stored as an image in a common format like PNG. 

### Drawing Points

This example creates an image and draws 5000 random points using <span style="font-family:Monospace;">image.drawPoint(point,color)</span>

![Example 01](00.png)

The image is stored using pillow.

### Drawing Lines

This example draws 500 random lines using using <span style="font-family:Monospace;">image.drawLine(start, end, color)</span>

![Example 01](01.png)

### Drawing Koch curve

This example draws a Koch curve using recursion. It is just another example how line drawing can be used.

![Example 01](02.png)


