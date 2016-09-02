try:
    from PIL import Image

except:
    import pip
    pip.main(['install', 'Pillow'])    # install Pillow if you don't have it yet...
    from PIL import Image

from pyrt.math import *
from pyrt.scene import *
from pyrt.geometry import Triangle, Vertex
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT

camera = PerspectiveCamera(640, 480)
scene = Scene()
scene.Add(Triangle(Vertex(position=(0, 0, 0), color=(1, 0, 0)),
                   Vertex(position=(0, 5, 0), color=(0, 1, 0)),
                   Vertex(position=(1, 5, 0), color=(0, 0, 1))))

scene.SetCamera(camera)

engine = SimpleRT()

imgdata = engine.render(scene)
