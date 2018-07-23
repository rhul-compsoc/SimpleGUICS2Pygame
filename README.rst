.. -*- restructuredtext -*-

==================
SimpleGUICS2Pygame
==================

It is primarily a standard Python_ (**2 and 3**) module
reimplementing the SimpleGUI particular module of CodeSkulptor_
(a browser Python interpreter).

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

| **Sources** and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on **PyPI**: https://pypi.org/project/SimpleGUICS2Pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`Online HTML documentation`: https://simpleguics2pygame.readthedocs.io/
.. _Python: http://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor`: http://www.codeskulptor.org/docs.html

.. |SimpleGUICS2Pygame| image:: https://simpleguics2pygame.readthedocs.io/en/latest/_images/SimpleGUICS2Pygame_64x64_t.png



If you have some problem
========================
First, read this short main `documentation page`_,
this Compatibility_ page
and this Tips_ page.

If you have problem with some command,
you can see its documentation in the `modules page`_.

Next, you can search in Stack Overflow.
If you don't find answer, you can ask question like this_.

Finally you can email me.
I will try to help you with pleasure.

.. _`documentation page`: https://simpleguics2pygame.readthedocs.io/
.. _Compatibility: https://simpleguics2pygame.readthedocs.io/en/latest/Compatibility.html
.. _`modules page`: https://simpleguics2pygame.readthedocs.io/en/latest/modules.html
.. _this: https://stackoverflow.com/questions/16387770/how-to-integrate-simplegui-with-python-2-7-and-3-0-shell
.. _Tips: https://simpleguics2pygame.readthedocs.io/en/latest/Tips.html



Installation
============
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

.. _matplotlib: http://matplotlib.org/
.. _pip: https://pypi.org/project/pip
.. _Pygame: http://www.pygame.org/


Test installation
-----------------
You can run the little script_ ``SimpleGUICS2Pygame_check.py``
to check if all required modules are installed.

Examples of good installation:
`result in Python 2`_
and
`result in Python 3`_.

You can also test your Pygame installation alone with the other little script_ ``pygame_check.py``.

.. _script: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/script/
.. _`result in Python 2`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/test/results_py2/SimpleGUICS2Pygame_check.log
.. _`result in Python 3`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/test/results_py3/SimpleGUICS2Pygame_check.log


On Window$
----------

* You can easily install matplotlib, pip and Pygame;
  see `Unofficial Windows Binaries matplotlib`_,
  `Unofficial Windows Binaries pip`_
  and `Unofficial Windows Binaries Pygame`_.

* You can use 7-Zip_ to unzip archive.

See `Complete installation on Window$ in few steps`_.

.. _7-Zip: http://www.7-zip.org/
.. _`Complete installation on Window$ in few steps`: https://simpleguics2pygame.readthedocs.io/en/latest/index.html#complete-installation-on-window-in-few-steps
.. _`Unofficial Windows Binaries matplotlib`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
.. _`Unofficial Windows Binaries pip`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip
.. _`Unofficial Windows Binaries Pygame`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame



Examples of CodeSkulptor and SimpleGUICS2Pygame use
===================================================
You can see examples in `SimpleGUICS2Pygame/example/`_ subdirectory from the sources archives.

.. _`SimpleGUICS2Pygame/example/`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/example/

Or online:
`Python programs running in CodeSkulptor`_ .

Two simple online examples:
  * `Frame_example.py`_: very simple canvas example
  * `presentation.py`_: little draw images and texts

.. _`Frame_example.py`: http://www.codeskulptor.org/#user30_w7FYxBIKJKzEkTu.py
.. _`presentation.py`: http://www.codeskulptor.org/#user44_XaGVASfiYWdEymp.py
.. _`Python programs running in CodeSkulptor`: https://simpleguics2pygame.readthedocs.io/en/latest/_static/links/prog_links.html



Message to developers
=====================
This is a **free software**, so you can download it, **modify it** and **submit your modifications**.
You can also **redistribute** your own version (keeping the GPL license).

Complete **sources** on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame

See developers_'page.

.. _developers: https://simpleguics2pygame.readthedocs.io/en/latest/Developers.html



Author: 🌳  Olivier Pirson — OPi |OPi| 🇧🇪🇫🇷🇬🇧 🐧
=======================================================
🌐 Website: http://www.opimedia.be/

💾 Bitbucket: https://bitbucket.org/OPiMedia/

* 📧 olivier.pirson.opi@gmail.com
* Mastodon: https://mamot.fr/@OPiMedia — Twitter: https://twitter.com/OPirson
* diaspora* (Framasphere*): https://framasphere.org/u/opimedia
* other profiles: http://www.opimedia.be/about/

.. |OPi| image:: http://www.opimedia.be/_png/OPi.png



Support me
==========
This package is a completely **free software** (GPL license).
So it is **completely free** (like "free speech" and like "free beer").
However you can **support me** financially by donating.

Go to the link |Donate|_. **Thank you!**

.. _Donate: http://www.opimedia.be/donate/

.. |Donate| image:: http://www.opimedia.be/donate/_png/Paypal_Donate_92x26_t.png



License: GPLv3_ |GPLv3|
=======================
Copyright (C) 2013, 2014, 2015, 2016, 2018 Olivier Pirson

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

.. _GPLv3: http://www.gnu.org/licenses/gpl.html

.. |GPLv3| image:: http://www.gnu.org/graphics/gplv3-88x31.png



Note that
=========
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

     .. _`Download medias`: https://simpleguics2pygame.readthedocs.io/en/latest/Tips.html#download-medias
     .. _`load_image()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/image.html#SimpleGUICS2Pygame.simpleguics2pygame.image.load_image
     .. _`_load_local_image()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/image.html#SimpleGUICS2Pygame.simpleguics2pygame.image._load_local_image
     .. _`_load_local_sound()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/sound.html#SimpleGUICS2Pygame.simpleguics2pygame.sound._load_local_sound
     .. _`load_sound()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/sound.html#SimpleGUICS2Pygame.simpleguics2pygame.sound.load_sound

* SimpleGUITk_ (David Holm) is *another implementation* of SimpleGUI of CodeSkulptor, using Tkinter and some others packages. It is really less complete and not updated. However it works for some programs.

.. warning::
   * simplegui_ (Florian Berger) is a Python package which has the same name as SimpleGUI of CodeSkulptor, but it is *totally something else*.

   .. _`An Introduction to Interactive Programming in Python`: https://www.coursera.org/learn/interactive-python-1
   .. _simplegui: https://pypi.org/project/simplegui
   .. _`SimpleGUI of CodeSkulptor`: http://www.codeskulptor.org/docs.html#Frames
   .. _SimpleGUITk: https://pypi.org/project/SimpleGUITk



Changes
=======
* 02.00.00 WORKING VERSION — July 23, 2018

  - Added a developer's page in documentation.

  - Replaced links of *Read the Docs*.

  - Added ``--last`` command line option.
  - Added ``test/test_command_line_options.py``.
  - Replaced ``_WEBSITE`` value by documentation link.
  - Splitted media links to image links and sound links.

  - Added ``script/pygame_check.py`` to check Pygame installation alone.

  - Added ``ValueError`` exception if ``draw_text()`` try to draw a text containing unprintable whitespace character.
  - Added ``draw_text_multi()`` in ``simplegui_lib_draw``.
  - Updated ``test/test_text.py``.

  - Added alpha possibility on background color.
  - Added ``transparent`` "color" name.

  - Improved dealing of input box.
  - Added ``test/test_input.py``.

  - Updated ``simpleplot`` module, to "run" same if matplotlib is not installed.
  - Updated ``test/test_objects.py``.

  - Corrected "Read the Docs" subpackage problem.

  - Updated ``test/test_sound.py``.

  - Updated ``script/SimpleGUICS2Pygame_check.py``.

  - **Splitted the big file ``simpleguics2pygame.py``.**
  - Added ``example/presentation.py``.

  - Added ``example/stop_example.py``.

  - Corrected ``test/test_sound.py``.

  - Updated documentation. (Thanks to `John Gray` and `Tom Keller`.)

  - Updated media and CodeSkulptor programs links.

* 01.09.00 — January 1st, 2015

  - **Added ``_load_local_image()`` and ``_load_local_sound()`` functions.**
  - …

…

`Complete changelog`_

.. _`Complete changelog`: https://simpleguics2pygame.readthedocs.io/en/latest/ChangeLog.html
