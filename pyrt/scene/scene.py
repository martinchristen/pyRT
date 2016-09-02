


class Scene:
    def __init__(self):
        self.camera = None
        self.nodes = []

    def Add(self, object):
        self.nodes.append(object)

    def SetCamera(self, cam):
        self.camera = cam
