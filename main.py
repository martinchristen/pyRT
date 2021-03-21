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

width = 1000
height = 800

camera = PerspectiveCamera(width, height, 60)
camera.setView(Vec3(0,-10,0), Vec3(0,0,0), Vec3(0,0,1))

scene = Scene()
scene.addLight(PointLight(Vec3(-1,-8,1)))

scene.add(
    Triangle(
        Vertex(position=(-1.5,10,0)),
        Vertex(position=(3.5,10,0)),
        Vertex(position=(1,10,5.)),
        material=PhongMaterial(color=Vec3(1,1,1))
    )
)

#scene.add(
#    Sphere(
#        center=Vec3(1, 10, 0),
#        radius = 1.5,
#        material=PhongMaterial(color=Vec3(1, 1, 0))
#    )
#)

scene.add(
    Sphere(
        center=Vec3(0, 0, 0),
        radius=1.5,
        material=PhongMaterial(color=Vec3(.9, .9, .9), transparency=0.4, refraction=1.33)
    )
)

scene.setCamera(camera)
engine = SimpleRT(iterations=10)
image = engine.render(scene)
image.save("a.png")
