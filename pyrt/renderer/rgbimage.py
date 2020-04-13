from ..math import Vec2, Vec3
import random
from time import time
from time import sleep

#-----------------------------------------------------------------------------------------------------------------------
# options:
RBGImage_use_numpy = True       # set to False if you don't want to use numpy
RGBImage_use_pillow = True      # set to False if you don't want to use pillow (store images manually)
RGBImage_use_ipython = True     # set to False if you don't want ipython/jupyter support
RGBImage_develop = True         # set to True for debug output
#-----------------------------------------------------------------------------------------------------------------------
RGBImage_use_numpy_array = False  # not a setting. 
                                  # If True: store rgb data i numpy, if False: store rgb data in Python list
                                  # [This is set to True automatically if numpy is available]
#-----------------------------------------------------------------------------------------------------------------------

if RBGImage_use_numpy:
    try:
        import numpy as np
        RGBImage_use_numpy_array = True
    except ImportError:
        RGBImage_use_numpy_array = False

RBGImage_has_pillow = False
if RGBImage_use_pillow:
    try:
        from PIL import Image
        RBGImage_has_pillow = True
    except ImportError:
        RBGImage_has_pillow = False

RGBImage_has_ipython = False
if RGBImage_use_ipython:
    try:
        __IPYTHON__
        from IPython.display import clear_output, display, HTML, Javascript 
        from io import BytesIO
        import base64
        RGBImage_has_ipython = True
    except NameError:
        RGBImage_has_ipython = False
#-----------------------------------------------------------------------------------------------------------------------


class RGBImage(object):
    def __init__(self, width: int, height: int, init_memory=True) -> None:
        self.width = width
        self.height = height
        self.type = "RGB"

        if init_memory:
            if RGBImage_use_numpy_array:
                self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            else:
                self.data = [[0, 0, 0] for i in range(0, self.width*self.height)]
        else:
            self.data = None


    #-------------------------------------------------------------------------------------------------------------------

    def save(self, filename: str) -> None:
        if RBGImage_has_pillow:
            if RBGImage_use_numpy:
                im = Image.fromarray(self.data)
                im.save(filename)
            else:
                im = Image.new("RGB", (self.width, self.height))
                im.putdata(self.data)
                im.save(filename)
        else:
            print("WARNING: Pillow module is required to export images!")
            print("         not saved anything!")

    # -------------------------------------------------------------------------------------------------------------------
    
    def _repr_html_(self):
        if RGBImage_has_ipython and RBGImage_has_pillow:
            if RGBImage_use_numpy_array:
                im = Image.fromarray(self.data)
            else:
                im = Image.new("RGB", (self.width, self.height))
                im.putdata(self.data)
            
            buffer = BytesIO()
            im.save(buffer, format="PNG")
            img_str = str(base64.b64encode(buffer.getvalue()), encoding="ascii")
            return '<img src="data:image/png;base64,' + img_str + '"></img>'
        else:
            return ''
        
    # -------------------------------------------------------------------------------------------------------------------
    
    def framebuffer(self, myid="pyrtfb"):
        t0 = time()
        if RGBImage_has_ipython and RBGImage_has_pillow:
            if RGBImage_use_numpy_array:
                im = Image.fromarray(self.data)
            else:
                im = Image.new("RGB", (self.width, self.height))
                im.putdata(self.data)
            
            buffer = BytesIO()
            im.save(buffer, format="PNG")
            img_str = str(base64.b64encode(buffer.getvalue()), encoding="ascii")

            display(HTML('<img src="data:image/png;base64,' + img_str + '"></img>'), display_id=myid, update=False)
            t1 = time()
            if RGBImage_develop:
                print("Time to display: " + str(round(t1-t0,2)) + "s")
            
        else:
            return ''
    # -------------------------------------------------------------------------------------------------------------------
    
    def update(self, myid="pyrtfb", fps=0):
        t0 = time()
        if RGBImage_has_ipython and RBGImage_has_pillow:
            if RGBImage_use_numpy_array:
                im = Image.fromarray(self.data)
            else:
                im = Image.new("RGB", (self.width, self.height))
                im.putdata(self.data)
            
            buffer = BytesIO()
            im.save(buffer, format="PNG")
            img_str = str(base64.b64encode(buffer.getvalue()), encoding="ascii")
                  
            display(HTML('<img src="data:image/png;base64,' + img_str + '"></img>'), display_id=myid, update=True)
            
            #adapt to fps:
            t1 = time()
            dt = t1-t0
                
            if fps != 0:
                wait = 1/fps - dt
                if wait>0:
                    sleep(wait)
            
            if RGBImage_develop:
                if fps == 0:
                    print("\rTime to display: " + str(round(dt,2)) + "s" + " [FPS: " + str(round(1./(dt),1)) + "]     ", end='')
                else:
                    dt = time()-t0
                    print("\rTime to display: " + str(round(dt,2)) + "s" + " [FPS: " + str(round(1./(dt),1)) + "]     ", end='')    
        else:
            return ''
        
    # -------------------------------------------------------------------------------------------------------------------            
    def display(self):
        print("**warning, display() is deprecated and will be removed**: Use the object directly in Jupyter")
        print("           also check out the new methods framebuffer() and update() for animations in Jupyter")
        if RGBImage_has_ipython and RBGImage_has_pillow:
            return HTML(data=self._repr_html_())
        else:
            print("ERROR: RGBImage.display() only works from IPython/Jupyter Notebook and also requires PIL")
            return None

    #-------------------------------------------------------------------------------------------------------------------
    
    def clear(self, color: Vec3) -> None:
        """
        Clear Image with specified color
        """
        r = int(color[0]*255.)
        g = int(color[1]*255.)
        b = int(color[2]*255.)
        if RGBImage_use_numpy_array:
            self.data[:,:] = [r,g,b]
        else:
            for y in range(self.height):
                for x in range(self.width):
                    self.data[y * self.width + x] = (r,g,b)
    
    #-------------------------------------------------------------------------------------------------------------------
    
    def drawPixelFast8(self, x: int, y: int, r: int, g: int, b: int) -> None:
        """
        Set 8-bit RGB pixel without boundary check and without float to int conversion.

        :param x: x-Pos
        :param y: y-Pos
        :param r: red
        :param g: green
        :param b: blue
        :return:
        """
        if RGBImage_use_numpy_array:
            self.data[y][x][0] = r
            self.data[y][x][1] = g
            self.data[y][x][2] = b
        else:
            self.data[y * self.width + x] = (r, g, b )
    # -------------------------------------------------------------------------------------------------------------------

    def drawPixel(self, pos: Vec2, color: Vec3) -> None:
        """
        This code is really slow if you write many pixels - it even contains a bounds check.
        If you draw many points, consider using self.data directly.


        :param pos: position of the point, with (0,0) being bottom left
        :param color: RGB Color (8 bit per channel)
        """
        x = pos.x
        y = self.height-pos.y-1
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            if RGBImage_use_numpy_array:
                self.data[y][x][0] = int(color[0]*255.)
                self.data[y][x][1] = int(color[1]*255.)
                self.data[y][x][2] = int(color[2]*255.)
            else:
                self.data[y*self.width+x] = (int(color[0]*255.), int(color[1]*255.), int(color[2]*255.))

    # -------------------------------------------------------------------------------------------------------------------
    
    def drawPoint(self, pos: Vec2, color: Vec3, size : int = 1) -> None:
        """
        Draws a point


        :param pos: position of the point, with (0,0) being bottom left
        :param color: RGB Color (8 bit per channel)
        :param size: size of the point
        :return:
        """

        # TODO: use arbitrary size, currently only size 1,2 and 3 are supported...

        if size == 1:
            self.drawPixel(pos,color)
        if size == 2:
            self.drawPixel(Vec2(pos.x, pos.y), color)
            self.drawPixel(Vec2(pos.x, pos.y+1), color)
            self.drawPixel(Vec2(pos.x+1, pos.y), color)
            self.drawPixel(Vec2(pos.x+1, pos.y+1), color)
        elif size == 3:
            self.drawPixel(Vec2(pos.x-1, pos.y-1), color)
            self.drawPixel(Vec2(pos.x, pos.y-1), color)
            self.drawPixel(Vec2(pos.x+1, pos.y-1), color)
            self.drawPixel(Vec2(pos.x-1, pos.y), color)
            self.drawPixel(Vec2(pos.x, pos.y), color)
            self.drawPixel(Vec2(pos.x+1, pos.y), color)
            self.drawPixel(Vec2(pos.x-1, pos.y+1), color)
            self.drawPixel(Vec2(pos.x, pos.y+1), color)
            self.drawPixel(Vec2(pos.x+1, pos.y+1), color)


    #-------------------------------------------------------------------------------------------------------------------

    def drawLine(self, start: Vec2, end: Vec2, color: Vec3 = Vec3(1.,1.,1.), size : int = 1) -> None:
        """Bresenham's line algorithm
           modified from: https://rosettacode.org/wiki/Bitmap/Bresenham%27s_line_algorithm#Python
        """
        dx = abs(end.x - start.x)
        dy = abs(end.y - start.y)
        x, y = start.x, start.y
        sx = -1 if start.x > end.x else 1
        sy = -1 if start.y > end.y else 1
        if dx > dy:
            err = dx / 2.0
            while x != end.x:
                self.drawPoint(Vec2(x, y), color, size)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != end.y:
                self.drawPoint(Vec2(x, y), color, size)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.drawPoint(Vec2(x, y), color, size)

    #-------------------------------------------------------------------------------------------------------------------

    def drawCircle(self, center: Vec2, radius: int, color: Vec3, size : int = 1):
        switch = 3 - (2 * radius)
        x = 0
        y = radius
        while x <= y:
            self.drawPoint(Vec2(x + center.x, -y + center.y), color, size)
            self.drawPoint(Vec2(y + center.x, -x + center.y), color, size)
            self.drawPoint(Vec2(y + center.x, x + center.y), color, size)
            self.drawPoint(Vec2(x + center.x, y + center.y), color, size)
            self.drawPoint(Vec2(-x + center.x, y + center.y), color, size)
            self.drawPoint(Vec2(-y + center.x, x + center.y), color, size)
            self.drawPoint(Vec2(-y + center.x, -x + center.y), color, size)
            self.drawPoint(Vec2(-x + center.x, -y + center.y), color, size)
            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1
            
    #-------------------------------------------------------------------------------------------------------------------
    
    def drawCircleFilled(self, center: Vec2, radius: int, color: Vec3, fillcolor: Vec3, size : int = 1):
        switch = 3 - (2 * radius)
        x = 0
        y = radius
        while x <= y:
            self.drawLine(Vec2(x + center.x, -y + center.y), Vec2(-x + center.x, -y + center.y), fillcolor)
            self.drawLine(Vec2(y + center.x, -x + center.y), Vec2(-y + center.x, -x + center.y), fillcolor)
            self.drawLine(Vec2(y + center.x, x + center.y), Vec2(-y + center.x, x + center.y), fillcolor)
            self.drawLine(Vec2(x + center.x, y + center.y), Vec2(-x + center.x, y + center.y), fillcolor)
            
            
            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1
                          
        self.drawCircle(center, radius, color, size)

    #-------------------------------------------------------------------------------------------------------------------

    def drawRectangle(self, bl : Vec2, width: int, height: int, color: Vec3) -> None:
        """
        Draws a rectangle.
        This is quite slow and would be much faster using direct image buffer filling instead of using bresenham lines.

        :param bl: bottom left coordinate of center
        :param width: width of rectangle
        :param height: height of rectangle
        :param color: color of rectangle
        :return:
        """
        for y in range(height):
            start = Vec2(bl.x, bl.y + y)
            end = Vec2(bl.x + width, bl.y + y)
            self.drawLine(start, end, color)


def loadimage(filename: str) -> RGBImage:
    """
    Load a RGBImage. This requires pillow and numpy
    """

    if not RGBImage_use_pillow or not RGBImage_use_ipython:
        raise NotImplementedError("Load only works if numpy and pillow is installed")
    
    im = Image.open(filename)
    if im.mode != 'RGB':
        im = im.convert('RGB')

    data = np.array(im.getdata(), dtype=np.uint8).reshape(im.size[1], im.size[0], 3)
    result = RGBImage(im.size[0], im.size[1], False)
    result.data = data
    
    return result
    