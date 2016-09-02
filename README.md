# PyRT - The Python Raytracer #

[![CI](https://travis-ci.org/martinchristen/pyRT.svg?branch=master)](https://travis-ci.org/martinchristen/pyRT) [![Gitter](https://badges.gitter.im/pyRT/pyRT-dev.svg)](https://gitter.im/pyRT/pyRT-dev?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)  [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/martinchristen/pyrt/issues) [![Code Climate](https://codeclimate.com/github/martinchristen/pyRT/badges/gpa.svg)](https://codeclimate.com/github/martinchristen/pyRT) [![](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/martinchristen/pyRT/blob/master/LICENSE.md)

![Logo](docs/img/pyRT_256.png)


**PyRT** (pronounced _pirate_) is a raytracer written in Python 3.x. This project is mainly done with the following in mind:

  * Ray Tracing in the Jupyter Notebook
  * Teaching Ray Tracing
  * Exploring ray tracing concepts for geo data using Python.
  * Rendering geo data, including large point clouds.
  * Implementing new algorithms for large 3D City Model rendering.
  * Creating 3D-Maps from OpenStreetMap data
  * ...

PyRT just started in July 2016, it is still **work in progress** - API changes will be frequent.

## Dependencies ##

PyRT doesn't have any dependencies at the moment. Generated images are just RGB or RGBA Arrays. To create jpg or png or other images, many demos use Pillow (PIL). So it is highly recommended to install it.

## Creating Scenes ##

PyRT is *not* a 3D-Modelling package. It is all about rendering from code.

In PyRT you create a scene first. Scenes consist of atleast one camera and geometry. Creation of scenes is done in an object oriented way:

```python
from pyrt.math import *
from pyrt.geometry import Triangle, Vertex
from pyrt.camera import PerspectiveCamera
from pyrt.renderer import SimpleRT

camera = PerspectiveCamera(640,480)
scene = Scene()
scene.add(Triangle(Vertex(position=(0, 0, 0), color=(1,0,0)), 
                   Vertex(position=(0, 5, 0), color=(0,1,0)), 
                   Vertex(position=(1, 5, 0), color=(0,0,1))))
                   
scene.setCamera(camera)

engine = SimpleRT()

imgdata = engine.render(scene)
```

PyRT has an open rendering concept, you can create **your own renderer**. In the example above "SimpleRT" was used, which is a minimalistic raycaster.

## Python & RayTracing, isn't that too slow ? ##

No. Custom renderers can be written in C with Python bindings. This is planned in future, later versions will even support the GPU using OpenCL and/or other libraries, but at the moment the primary focus is to create a pythonic interface to scenegraph based ray tracing.

## License ##

PyRT is released under MIT. 
More information about this license can be found under: [https://opensource.org/licenses/MIT]()

## Author ##

PyRT is created and maintained by Martin Christen. You can contact me by e-mail: martin.christen@gmail.com

## Support this project! ##

There are several ways to support this project, constribute, test, document, ...

Some Contribution examples:

* Contribute: implement new renderers
* Contrubute: support new geometry types 
* Contribute: implement new lighting models
* Contribute: rendering examples


