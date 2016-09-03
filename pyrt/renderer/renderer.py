"""
This is the abstract Renderer.

If you override if you implement your own.
"""

from abc import abstractmethod
from ..scene import Scene


class Renderer(object):
    def __init__(self, name="UNKNOWN RENDERER"):
        self.name = name
        print("# Creating Renderer: " + self.name)

    @abstractmethod
    def render(self, scene : Scene) -> list:
        """
        Abstract rendering. This actually renmders the scene and returns the image data

        :param scene: the scene to render
        :return:
        """
        pass
