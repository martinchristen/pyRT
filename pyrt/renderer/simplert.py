from .renderer import *


class SimpleRT(Renderer):
    def __init__(self):
        Renderer.__init__(self, "Simple Raytracer")


    def render(self, scene : Scene) -> None:
        pass

