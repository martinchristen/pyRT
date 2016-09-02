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

width = 640
height = 480
camera = PerspectiveCamera(width, height)
scene = Scene()
scene.add(Triangle(Vertex(position=(0, 0, 0), color=(1, 0, 0)),
                   Vertex(position=(0, 0, 5), color=(0, 1, 0)),
                   Vertex(position=(5, 5, 0), color=(0, 0, 1))))

scene.setCamera(camera)

engine = SimpleRT()

imgdata = engine.render(scene)


# save image using pillow
im = Image.new("RGBA", (width,height))
im.putdata(imgdata)
im.save("sample.png")
