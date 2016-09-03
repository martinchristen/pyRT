from ..math import Vec2, Vec3


class RGBImage(object):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.type = "RGB"

        if self.type == "RGB":
            self.data = [(0, 0, 0) for i in range(0, self.width*self.height)]
        else:   # in future there will be RGBA, FLOAT images
            raise ValueError("unknown/unsupported image type")

    #-------------------------------------------------------------------------------------------------------------------

    def drawPoint(self, pos: Vec2, color: Vec3) -> None:
        # This code is really slow if you write many pixels - it even contains a bounds check.
        # If you draw many points, please use self.data directly.
        # This draw point assumes (0,0) to be bottom left
        x = pos.x
        y = self.height-pos.y-1
        if x>=0 and x<self.width and y>=0 and y<self.height:
            self.data[y*self.width+x] = (int(color[0]*255.), int(color[1]*255.), int(color[2]*255.))

    #-------------------------------------------------------------------------------------------------------------------

    def drawLine(self, start: Vec2, end: Vec2, color: Vec3 = Vec3(1.,1.,1.)) -> None:
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
                self.drawPoint(Vec2(x, y), color)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != end.y:
                self.drawPoint(Vec2(x, y), color)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        self.drawPoint(Vec2(x, y), color)

    #-------------------------------------------------------------------------------------------------------------------

    def drawCircle(self, center: Vec2, radius: int, color: Vec3):
        switch = 3 - (2 * radius)
        x = 0
        y = radius
        while x <= y:
            self.drawPoint(Vec2(x + center.x, -y + center.y), color)
            self.drawPoint(Vec2(y + center.x, -x + center.y), color)
            self.drawPoint(Vec2(y + center.x, x + center.y), color)
            self.drawPoint(Vec2(x + center.x, y + center.y), color)
            self.drawPoint(Vec2(-x + center.x, y + center.y), color)
            self.drawPoint(Vec2(-y + center.x, x + center.y), color)
            self.drawPoint(Vec2(-y + center.x, -x + center.y), color)
            self.drawPoint(Vec2(-x + center.x, -y + center.y), color)
            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1

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




