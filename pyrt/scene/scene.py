"""
This file contains the scene description

This is an early prototype, more to come soon...
"""


class Scene(object):
    def __init__(self):
        self.camera = None
        self.nodes = []
        self.lights = []

    def add(self, object):
        self.nodes.append(object)

    def addLight(self, light):
        self.lights.append(light)

    def setCamera(self, cam):
        self.camera = cam
