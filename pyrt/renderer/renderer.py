from abc import abstractmethod
from ..scene import *


class Renderer(object):
    def __init__(self, name="UNKNOWN RENDERER"):
        self.name = name
        print("# Creating Renderer: " + self.name)

    @abstractmethod
    def render(self, scene):
        pass
