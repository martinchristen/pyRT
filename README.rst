PyRT - The Python Raytracer
===========================

|CI| |Gitter| |contributions welcome| |Code Climate| |Code Health|
|image5|

If you like this project, please support development: 
https://pages.donately.com/pybaselassociation/campaign/pyrt-version-1-0



.. figure:: docs/img/pyRT_256.png
   :alt: Logo

**PyRT** (pronounced *pirate*) is a raytracer/image generator for **Python 3.5** and higher.
This project is mainly done with the following in mind:

-  Ray Tracing in the Jupyter Notebook
-  Teaching ray tracing
-  Exploring ray tracing concepts for geo data using Python.
-  Rendering geo data, including large point clouds.
-  Implementing new algorithms for rendering large 3D city models.
-  Creating 3D-Maps from OpenStreetMap data
-  Server-side rendering / cloud based rendering
-  ...

PyRT is **work in progress**.

Installation
------------

Installation can be done with pip. Please note that pyrt is still under **heavy development** and not yet meant for production.
(API breaks are possible!)

.. code:: shell

    pip install pyrt


Currently it is recommended to pip directly from the repository:

.. code:: shell

    pip install https://github.com/martinchristen/pyRT/archive/master.zip --upgrade



Dependencies
------------

PyRT doesn't have any dependencies.
Generated images are just RGB or RGBA Arrays. To create jpg or png or other images, many
demos use Pillow (PIL). So it is highly recommended to install it.

Getting Started: Try the examples
---------------------------------

There are a lot of examples available how to use this module. This is
the recommended way to get started with pyRT.

|Example 01| |Example 12b| |Example 13| |Example 08|

`View all examples <examples/README.md>`__

Creating Scenes
---------------

PyRT is *not* a 3D-modelling package. It is all about rendering from
code.

In PyRT you create a scene first. Scenes consist of atleast one camera
and geometry. Creation of scenes is done in an object oriented way:

.. code:: python

    from pyrt.math import *
    from pyrt.geometry import Triangle, Vertex
    from pyrt.material import PhongMaterial
    from pyrt.camera import PerspectiveCamera
    from pyrt.renderer import SimpleRT
    from pyrt.scene import Scene

    camera = PerspectiveCamera(640,480)
    scene = Scene()
    scene.add(Triangle(Vertex(position=(0, 0, 0)), 
                       Vertex(position=(0, 5, 0)), 
                       Vertex(position=(1, 5, 0)), material=PhongMaterial()))
                       
    scene.setCamera(camera)

    engine = SimpleRT()

    imgdata = engine.render(scene)

PyRT has an open rendering concept, you can create **your own
renderer**. In the example above "SimpleRT" was used, which is a
minimalistic reference implementation.

Python & RayTracing, isn't that too slow ?
------------------------------------------

No. Custom renderers can be written in C with Python bindings. This is
planned in future, later versions will even support the GPU using OpenCL
and/or other libraries, but at the moment the primary focus is to create
a "pythonic" ray tracer.

License
-------

PyRT is released under MIT. More information about this license can be
found under: https://opensource.org/licenses/MIT

About the Author
----------------

PyRT is created and maintained by Martin Christen. You can contact me by
e-mail: martin.christen@fhnw.ch

Please note: This project is mostly developed in my spare time, there is no
official support or anything.

.. |CI| image:: https://travis-ci.org/martinchristen/pyRT.svg?branch=master
   :target: https://travis-ci.org/martinchristen/pyRT
.. |Gitter| image:: https://badges.gitter.im/pyRT/Lobby.svg
   :target: https://gitter.im/pyRT/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
.. |contributions welcome| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
   :target: https://github.com/martinchristen/pyrt/issues
.. |Code Climate| image:: https://codeclimate.com/github/martinchristen/pyRT/badges/gpa.svg
   :target: https://codeclimate.com/github/martinchristen/pyRT
.. |Code Health| image:: https://landscape.io/github/martinchristen/pyRT/master/landscape.svg?style=flat
   :target: https://landscape.io/github/martinchristen/pyRT/master
.. |image5| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/martinchristen/pyRT/blob/master/LICENSE.md
.. |Example 01| image:: examples/11.png
.. |Example 12b| image:: examples/12b.gif
.. |Example 13| image:: examples/13.png
.. |Example 08| image:: examples/08.png

