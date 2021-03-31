from pyrt.geometry.vertex import Vertex
from pyrt import material
from pyrt.math import Vec3
from pyrt.scene import Scene
from pyrt.light import PointLight
from pyrt.geometry import Sphere, Triangle
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT
from PIL import Image

width = 400
height = 300

camera = PerspectiveCamera(width, height, 60)
camera.setView(Vec3(0,-10,0), Vec3(0,0,0), Vec3(0,0,1))

scene = Scene()
scene.addLight(PointLight(Vec3(-1,-8,1)))

# Triangle behind lens
A = Vertex(position=(-1.5, 6, 0))
B = Vertex(position=(3.5, 6, 0))
C = Vertex(position=(1, 6, 5.))
scene.add(Triangle(A, B, C, material=PhongMaterial(color=Vec3(1,1,1))))

# Floor
A = Vertex(position=(-5.0, -5.0, -2.0))
B = Vertex(position=( 5.0, -5.0, -2.0))
C = Vertex(position=( 5.0,  5.0, -2.0))
D = Vertex(position=(-5.0,  5.0, -2.0))

floormaterial = PhongMaterial(color=Vec3(.2,.2,.2)  )
scene.add(Triangle(A,B,C, material=floormaterial))
scene.add(Triangle(A,C,D, material=floormaterial))

# Two lenses
scene.add(Sphere(Vec3(-1, 5.7, -1), 2.5, PhongMaterial(color=Vec3(.9, .9, .9),
    transparency=.8, refraction=1.5)))
scene.add(Sphere(Vec3(2.8, 5, .5), 1.8, PhongMaterial(color=Vec3(.9, .9, .9),
    transparency=.8, refraction=1.5)))

scene.setCamera(camera)
engine = SimpleRT(iterations=4, shadow=True)
image = engine.render(scene)
image.save("16.png")
