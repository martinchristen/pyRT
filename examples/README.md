# pyRT Examples

For the examples you need "pillow" installed. This can be done using pip

    pip install Pillow
    
or by running this Python code:

    import pip
    pip.main(['install', 'Pillow'])

## Using 'pyrt.image'

The first series of examples is just about images and drawing into them.
It is important to understand the concept of an "image generator". 
While most graphics applications draw something on the screen, in pyRT there is no interactive window displaying anything.
Images are for example generated as list of RGB tuples, which are then stored as an image in a common format like PNG. 

### Drawing Points

[00_drawpoints.py](00_drawpoints.py)

This example creates an image and draws 5000 random points using <span style="font-family:Monospace;">image.drawPoint(point,color)</span>

![Example 01](00.png)

The image is stored using pillow.

### Drawing Lines

[01_drawlines.py](01_drawlines.py)

This example draws 500 random lines using using <span style="font-family:Monospace;">image.drawLine(start, end, color)</span>. Drawing lines is done using the <a href="https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm" target="_blank">Bresenham line drawing algorithm</a>.

<cite>J. E. Bresenham. 1965. Algorithm for computer control of a digital plotter. IBM Syst. J. 4, 1 (March 1965), 25-30. DOI=http://dx.doi.org/10.1147/sj.41.0025</cite>

![Example 01](01.png)

### Drawing Koch curve

[02_snowflake.py](02_snowflake.py)

This example draws a Koch curve using recursion. It is just another example how line drawing can be used.

![Example 01](02.png)


### Drawing Circles

[03_circle.py](03_circle.py)

This example draws 100 random circles using  <span style="font-family:Monospace;">image.drawCircle(center, radius, color)</span>. Drawing lines is done using the <a href="https://en.wikipedia.org/wiki/Midpoint_circle_algorithm" target="_blank">Midpoint circle algorithm</a>.

![Example 01](03.png)

### Drawing Rectangles

[04_rectangle.py](04_rectangle.py)

This example draws 50 random rectangles using <span style="font-family:Monospace;">image.drawRectangle(bottomleft, width, height, color)</span>.

![Example 01](04.png)





