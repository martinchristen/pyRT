# Example 17: Textured raytracing
#
# This time we render a triangle and scene with mipmaps
# Used textures contain funny digits
# Digit corresponds to level of detalization

from pyrt.light import PointLight
from pyrt.scene import *
from pyrt.material.texturematerial import TextureMaterial
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT

from pyrt.renderer import RGBImage
from pyrt.math import Vec3
from pyrt.geometry import Triangle, Vertex
import moviepy.editor as mpy


def make_frame(t):
    w = 320
    h = 240

    # Create a camera with width, height and field of view:
    camera = PerspectiveCamera(w, h, 60)

    # Set View matrix of camera: define where to look at
    camera.setView(Vec3(0, -t - 10, 0), Vec3(0, 0, 0), Vec3(0, 0, 1))

    #  Create view-projection matrix (right to left)
    vp =  camera.projection * camera.view

    # Create a scene
    scene = Scene()

    # Add a light to the scene
    scene.addLight(PointLight(Vec3(0, -2, 0)))

    # Create a triangle
    t1 = Triangle(Vertex(position=(-5, -4, 5), texcoord=(0, 0)),
                 Vertex(position=(5, -4, 5), texcoord=(1, 0)),
                 Vertex(position=(5, -4, -5), texcoord=(1, 1)),
                 material=
                 TextureMaterial(texturepath=['tex17-1.png', 'tex17-2.png']))

    t2 = Triangle(Vertex(position=(-5, -4, 5), texcoord=(0, 0)),
                 Vertex(position=(5, -4, -5), texcoord=(1, 1)),
                 Vertex(position=(-5,-4, -5), texcoord=(0, 1)),
                 material=
                 TextureMaterial(texturepath=['tex17-1.png', 'tex17-2.png']))

    # Add triangle and sphere to the scene:
    scene.add(t1)
    scene.add(t2)

    # Now tell the scene which camera we use
    scene.setCamera(camera)

    # Create a raytracer using "SimpleRT"
    engine = SimpleRT()

    # Render the scene:
    image = engine.render(scene)
    return image.data


clip = mpy.VideoClip(make_frame, duration=10)
clip.write_gif("17.gif",fps=20)
