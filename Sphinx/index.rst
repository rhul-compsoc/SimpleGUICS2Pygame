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
Obviously you need Python_. Then, open a terminal and do:

.. code-block:: sh

   $ python -m pip install -U pip --upgrade
   $ python -m pip install -U pygame --user --upgrade
   $ python -m pip install -U matplotlib --upgrade
   $ python -m pip install -U SimpleGUICS2Pygame --upgrade

See explanations of each part below.

If several Python implementations are installed,
maybe you must use something like ``python2`` or ``python3`` instead ``python`` command.

Note that ``$`` represents the prompt and do *not* be entered by you.

In some cases, maybe you must use **administrator rights**. With GNU/Linux do:

.. code-block:: sh

   $ sudo [your command]


First of all, install pip_, the installer of Python package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If ``pip`` is not yet installed on your system, install it with:

.. code-block:: sh

   $ python -m pip install -U pip --upgrade

If you have some problem,
see `installation documentation of pip`_.

.. _`installation documentation of pip`: https://pip.pypa.io/en/stable/installing/
.. _pip: https://pypi.org/project/pip


Install required package pygame_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Pygame is required to use module ``simplegui_lib`` (and its submodules)
and module ``simpleguics2pygame`` of SimpleGUICS2Pygame
(except for the Timer class).

.. code-block:: sh

   $ python -m pip install -U pygame --user --upgrade

If you have some problem,
see `installation documentation of pygame`_.

.. _`installation documentation of pygame`: https://www.pygame.org/wiki/GettingStarted
.. _Pygame: https://www.pygame.org/


Install required package matplotlib_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
matplotlib is required to use module ``simpleplot`` of SimpleGUICS2Pygame.

.. code-block:: sh

   $ python -m pip install -U matplotlib --upgrade

If you have some problem,
see `installation documentation of matplotlib`_.

.. _`installation documentation of matplotlib`: https://matplotlib.org/users/installing.html
.. _matplotlib: https://matplotlib.org/


Finally, install the package SimpleGUICS2Pygame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: sh

   $ python -m pip install -U SimpleGUICS2Pygame --upgrade

Alternatively you can install SimpleGUICS2Pygame manually.
The download_ directory contains
some archives of all sources.

.. _download: https://bitbucket.org/OPiMedia/simpleguics2pygame/downloads/


Test installation
~~~~~~~~~~~~~~~~~
You can run the little script_ ``SimpleGUICS2Pygame_check.py``
to check if all required modules are installed.

Examples of result with good installation:
`result in Python 2`_
and
`result in Python 3`_.

You can also test your Pygame installation alone with the other little script_ ``pygame_check.py``.

.. _script: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/script/
.. _`result in Python 2`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/test/results_py2/SimpleGUICS2Pygame_check.log
.. _`result in Python 3`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/test/results_py3/SimpleGUICS2Pygame_check.log


Update
~~~~~~
If SimpleGUICS2Pygame was installed with pip_ you can update it with:

.. code-block:: sh

   $ python -m pip install -U SimpleGUICS2Pygame --upgrade


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


Author: 🌳 Olivier Pirson — OPi |OPi| 🇧🇪🇫🇷🇬🇧 🐧 👨‍💻 👨‍🔬
-----------------------------------------------------------------
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
This program is a **free software** (GPL license).
It is **completely free** (like "free speech" *and* like "free beer").
However you can **support me** financially by donating.

Click to this link |Donate|
**Thank you!**

.. |Donate| image:: http://www.opimedia.be/donate/_png/Paypal_Donate_92x26_t.png
   :target: http://www.opimedia.be/donate/


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
