from pyrt.geometry.sphere import Sphere
from typing import List
from pyrt.math import *
from pyrt.light import *
from pyrt.geometry import Triangle, Vertex, Sphere
from pyrt.material import PhongMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT 
from pyrt.scene import Scene

floormaterial = PhongMaterial(color=Vec3(0.5,0.5,0.5))
sphere0material = PhongMaterial(color=Vec3(1.,0.,0.), transparency=0.5)
sphere1material = PhongMaterial(color=Vec3(0.,0.,1.), transparency=0.7)

camera = PerspectiveCamera(640, 480, 45)
camera.setView(Vec3(0.,-10.,10.), Vec3(0.,0.,0.), Vec3(0.,0.,1.))

scene = Scene()
scene.add(Triangle(Vertex(position=(0, 0, 0)),
                   Vertex(position=(0, 5, 0)),
                   Vertex(position=(1, 5, 0)), material=PhongMaterial()))
scene.setCamera(camera)
scene.addLight(PointLight(Vec3(0,0,15)))

# Add "floor"
A = Vertex(position=(-5.0, -5.0, 0.0))
B = Vertex(position=( 5.0, -5.0, 0.0))
C = Vertex(position=( 5.0,  5.0, 0.0))
D = Vertex(position=(-5.0,  5.0, 0.0))
scene.add(Triangle(A,B,C, material=floormaterial))

# Add spheres
scene.add(Sphere(center=Vec3(2,-3.5,1.75), radius=1, material=sphere0material))
scene.add(Sphere(center=Vec3(2,-1.5,1.75), radius=1, material=sphere1material))

imgdata = SimpleRT(shadow=True, iterations=3).render(scene)
imgdata.save('a.png')
