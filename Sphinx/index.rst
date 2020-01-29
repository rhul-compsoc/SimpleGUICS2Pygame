SimpleGUICS2Pygame package's documentation
==========================================

It is primarily a standard Python_ (**2 and 3**) module
reimplementing the SimpleGUI particular module of CodeSkulptor_
(a browser Python interpreter).
This is in fact a package also with other modules adapted from CodeSkulptor.

Simply change

.. code-block:: python

   import simplegui

by

.. code-block:: python

    try:
        import simplegui
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

in your CodeSkulptor program
and your program **run both** in CodeSkulptor
and *standard Python* with this module (and Pygame).

|SimpleGUICS2Pygame|

`Online HTML documentation`_ on **Read The Docs**.
(You can also see the online `SimpleGUI documentation on CodeSkulptor`_.)

**This is the online HTML documentation of the working version 2.**


| **Sources** and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on **PyPI**: https://pypi.org/project/SimpleGUICS2Pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`Online HTML documentation`: https://simpleguics2pygame.readthedocs.io/
.. _Python: https://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor`: http://www.codeskulptor.org/docs.html

.. |SimpleGUICS2Pygame| image:: _static/img/SimpleGUICS2Pygame_64x64_t.png

|


If you have some problem
------------------------
First, read this short main documentation page,
this Compatibility_ page
and this Tips_ page.

If you have problem with some command,
you can see its documentation in the `modules page`_
or by the :ref:`genindex` page .

Next, you can search in Stack Overflow.
If you don't find answer, you can ask question like this_.

Finally you can email me.
I will try to help you with pleasure.
(You can write me in French.)

.. _Compatibility: Compatibility.html
.. _`modules page`: modules.html
.. _this: https://stackoverflow.com/questions/16387770/how-to-integrate-simplegui-with-python-2-7-and-3-0-shell
.. _Tips: Tips.html


Installation
------------
If pip_ is installed on your platform you can do:

>>> pip install SimpleGUICS2Pygame

(If several Python implementations are installed,
maybe you must use something like `pip2` or `pip3` instead `pip` command.)


Without pip, download the archive ``SimpleGUICS2Pygame-?.tar.gz``, unzip it ``somewhere``.
Next in the ``somewhere/SimpleGUICS2Pygame-?/`` subdirectory run:

>>> python setup.py install

In both cases, you must use **admin access**. So with GNU/Linux you will probably do:

>>> sudo [your command]


Module ``simpleplot`` require matplotlib_
(and must be installed separately).

Modules ``simplegui_lib`` (and its submodules) and ``simpleguics2pygame`` (except for the Timer class)
require Pygame_
(and must be installed separately).

.. _matplotlib: https://matplotlib.org/
.. _pip: https://pypi.org/project/pip
.. _Pygame: https://www.pygame.org/


Test installation
~~~~~~~~~~~~~~~~~
You can run the little script_ ``SimpleGUICS2Pygame_check.py``
to check if all required modules are installed.

Examples of good installation:
`result in Python 2`_
and
`result in Python 3`_.

You can also test your Pygame installation alone with the other little script_ ``pygame_check.py``.

.. _script: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/script/
.. _`result in Python 2`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/test/results_py2/SimpleGUICS2Pygame_check.log
.. _`result in Python 3`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/test/results_py3/SimpleGUICS2Pygame_check.log


Update
~~~~~~
With pip_ installed on your plaftorm you can update SimpleGUICS2Pygame:

>>> pip install SimpleGUICS2Pygame --upgrade


Complete installation on Window$ in few steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download and run the good `Pygame` installation file: `Unofficial Windows Binaries Pygame`_.  (Only require for ``simplegui_lib``, its submodules and ``simpleguics2pygame``.)

2. Download and run the good `matplotlib` installation file (**and** all its requirements): `Unofficial Windows Binaries matplotlib`_. (Only require for ``simpleplot``.)

3. Download and run the good `setuptools` installation file: `Unofficial Windows Binaries setuptools`_.

4. Download and run the good `pip` installation file: `Unofficial Windows Binaries pip`_.

5. Run in the *Command Prompt* (maybe with *Administrator* rights): ``pip install SimpleGUICS2Pygame`` . (Probably the ``pip`` command aren't in your ``PATH``, so add it or move in the subdirectory of ``pip`` with the ``CD`` command. This subdirectory is something like ``C:\Python?\Scripts\`` .)

.. _`Unofficial Windows Binaries matplotlib`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
.. _`Unofficial Windows Binaries pip`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip
.. _`Unofficial Windows Binaries Pygame`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
.. _`Unofficial Windows Binaries setuptools`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools


Examples of CodeSkulptor and SimpleGUICS2Pygame use
---------------------------------------------------
You can see examples in `SimpleGUICS2Pygame/example/`_ subdirectory from the sources archives.

.. _`SimpleGUICS2Pygame/example/`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/example/

Or online:
`Python programs running in CodeSkulptor`_ .

Two simple online examples:
  * `Frame_example.py`_: very simple canvas example
  * `presentation.py`_: little draw images and texts

.. _`Frame_example.py`: http://www.codeskulptor.org/#user30_w7FYxBIKJKzEkTu.py
.. _`presentation.py`: http://www.codeskulptor.org/#user47_vA52sTrGMElpRNd.py
.. _`Python programs running in CodeSkulptor`: _static/links/prog_links.html


Message to developers
---------------------
This is a **free software**, so you can download it, **modify it** and **submit your modifications**.
You can also **redistribute** your own version (keeping the `GPL license`_).

Complete **sources** on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame

See developers_'page.

.. _developers: Developers.html
.. _`GPL license`: License.html


Author: 🌳  Olivier Pirson — OPi |OPi| 🇧🇪🇫🇷🇬🇧 🐧 👨‍💻 👨‍🔬
------------------------------------------------------------------
🌐 Website: http://www.opimedia.be/

💾 Bitbucket: https://bitbucket.org/OPiMedia/

* 📧 olivier.pirson.opi@gmail.com
* Mastodon: https://mamot.fr/@OPiMedia — Twitter: https://twitter.com/OPirson
* diaspora* (Framasphere*): https://framasphere.org/u/opimedia
* 👨‍💻 LinkedIn: https://www.linkedin.com/in/olivierpirson/ — CV: http://www.opimedia.be/CV/English.html
* other profiles: http://www.opimedia.be/about/

.. |OPi| image:: http://www.opimedia.be/_png/OPi.png


Support me
----------
This package is a completely **free software**, see `GPL license`_.
So it is **completely free** (like "free speech" and like "free beer").
However you can **support me** financially by donating.

Go to the link |Donate|_. **Thank you!**

.. _Donate: http://www.opimedia.be/donate/

.. |Donate| image:: _static/img/Paypal_Donate_92x26_t.png


Note that
---------
* `SimpleGUI of CodeSkulptor`_ (Scott Rixner) is a specific module of CodeSkulptor_, written in JavaScript.

  CodeSkulptor is a Python implementation running **in a browser**.
  It implements a subset of Python **2**.
  It is the environment used in the course
  `An Introduction to Interactive Programming in Python`_
  (Rice University, Coursera).

* **SimpleGUICS2Pygame** (Olivier Pirson) is **this package**.
  It is fully compatible with Python **2 and 3**.

  It contains
  ``codeskulptor``, ``numeric``, ``simpleguics2pygame`` and ``simpleplot`` modules
  that reimplement
  ``codeskulptor``, ``numeric``, ``simplegui`` and ``simpleplot`` modules of CodeSkulptor.

  .. warning::
     SimpleGUICS2Pygame was **designed to mimic behavior of CodeSkulptor**.
     So `load_image()`_ and `load_sound()`_ methods can load medias only from URL, not local files.
     However SimpleGUICS2Pygame can save these medias to a specific local directory.
     See the `Download medias`_ tips.

     You can also use *specific* `_load_local_image()`_ and `_load_local_sound()`_ methods
     to load local files. But be careful, each specific method doesn't exist in CodeSkulptor.

     There exist some **little differences between SimpleGUICS2Pygame and SimpleGUI** of CodeSkulptor.
     See Compatibility_ notes.

     .. _`Download medias`: Tips.html#download-medias
     .. _`load_image()`: simpleguics2pygame/image.html#SimpleGUICS2Pygame.simpleguics2pygame.image.load_image
     .. _`_load_local_image()`: simpleguics2pygame/image.html#SimpleGUICS2Pygame.simpleguics2pygame.image._load_local_image
     .. _`_load_local_sound()`: simpleguics2pygame/sound.html#SimpleGUICS2Pygame.simpleguics2pygame.sound._load_local_sound
     .. _`load_sound()`: simpleguics2pygame/sound.html#SimpleGUICS2Pygame.simpleguics2pygame.sound.load_sound

* SimpleGUITk_ (David Holm) is *another implementation* of SimpleGUI of CodeSkulptor, using Tkinter and some others packages. It is really less complete and not updated. However it works for some programs.

.. warning::
   * simplegui_ (Florian Berger) is a Python package which has the same name as SimpleGUI of CodeSkulptor, but it is *totally something else*.

   .. _`An Introduction to Interactive Programming in Python`: https://www.coursera.org/learn/interactive-python-1
   .. _simplegui: https://pypi.org/project/simplegui
   .. _`SimpleGUI of CodeSkulptor`: http://www.codeskulptor.org/docs.html#Frames
   .. _SimpleGUITk: https://pypi.org/project/SimpleGUITk



Table of contents
=================

.. toctree::
   :maxdepth: 3

   package_init

   modules

   Compatibility

   Tips

   License

   Bugs

   Developers

   ChangeLog

   List of online programs <https://simpleguics2pygame.readthedocs.io/en/latest/_static/links/prog_links.html>
   List of online images <https://simpleguics2pygame.readthedocs.io/en/latest/_static/links/img_links.html>
   List of online sounds <https://simpleguics2pygame.readthedocs.io/en/latest/_static/links/snd_links.html>

   Index <https://simpleguics2pygame.readthedocs.io/en/latest/genindex.html>



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
