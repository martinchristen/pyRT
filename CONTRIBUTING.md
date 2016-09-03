# Contributing to pyRT

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/martinchristen/pyrt/issues) [![Gitter](https://badges.gitter.im/pyRT/pyRT-dev.svg)](https://gitter.im/pyRT/pyRT-dev?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

We'd love for you to contribute to our source code and to make pyRT even better than it is
today! 

There are several ways to support this project, constribute, test, document, ...

Some contribution examples:

* Implement new renderers
* Support new geometry types 
* Implement new lighting models
* Create some cool rendering examples (2D/3D or whatever)
* Help to increase the project health score!
 
## Got a Question or Problem?

If you have questions about how to use pyRT - we are also available on [Gitter][gitter].

## Found an Issue?

If you find a bug in the source code or a mistake in the documentation, you can help us by
submitting an issue to our [GitHub Repository][github]. Even better you can submit a Pull Request
with a fix.
 
## Want a Feature?

You can request a new feature by submitting an issue to our [GitHub Repository][github].  If you
would like to implement a new feature then consider what kind of change it is:

* **Major Changes** that you wish to contribute to the project should be discussed first on 
  [Gitter][gitter] so that we can better coordinate our efforts,
  prevent duplication of work, and help you to craft the change so that it is successfully accepted
  into the project.
* **Small Changes** can be crafted and submitted to the [GitHub Repository][github] as a Pull
  Request.

## Coding Guideline
   
**Keep pure Python for now!**

_I know there can be many speed improvements done by just using numpy or whatever cool external module you think of.
As soon as the Pure-Python code is stable we can do that, but for now I really want no external dependencies._
  
For examples (in the example directory) Pillow, moviepy or other dependencies is acceptable if they are documented.
  
## Rendering Examples
  
If you created a cool scene, submit it as a Pull Request (use the "examples" directory). If possible include a screenshot.

  
  
[gitter]: https://gitter.im/pyRT/pyRT-dev
[github]: https://github.com/martinchristen/pyRT
  
 