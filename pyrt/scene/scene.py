

class Scene(object):
    def __init__(self):
        self.camera = None
        self.nodes = []

    def add(self, object):
        self.nodes.append(object)

    def setCamera(self, cam):
        self.camera = cam
