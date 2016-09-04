from pyrt.math import *
from pyrt.scene import *
from pyrt.geometry import Triangle, Vertex
from pyrt.camera import OrthographicCamera, PerspectiveCamera
from pyrt.renderer import SimpleRT
from pyrt.utils import CreatePPM
width = 512
height = 512
camera = OrthographicCamera(width, height)
scene = Scene()
scene.add(Triangle(Vertex(position=(0, 0, -1000), color=(1, 0, 0)),
                   Vertex(position=(0, 512, -1000), color=(0, 1, 0)),
                   Vertex(position=(512, 256, -1000), color=(0, 0, 1))))


'''
camera = PerspectiveCamera(width,height)
scene = Scene()
scene.add(Triangle(Vertex(position=(1, 0, 1), color=(1,0,0)),
                   Vertex(position=(1, 5, -1), color=(0,1,0)),
                   Vertex(position=(5, 1, 0), color=(0,0,1))))
'''


scene.setCamera(camera)

engine = SimpleRT()

imgdata = engine.render(scene)


CreatePPM("sample.ppm",(width,height),imgdata)