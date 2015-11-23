.. -*- restructuredtext -*-

==================
SimpleGUICS2Pygame
==================

It is primarily a standard Python_ (2 **and** 3) module
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
| and on **PyPI**: https://pypi.python.org/pypi/SimpleGUICS2Pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`Online HTML documentation`: http://simpleguics2pygame.readthedocs.org/
.. _Python: http://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor`: http://www.codeskulptor.org/docs.html

.. |SimpleGUICS2Pygame| image:: https://simpleguics2pygame.readthedocs.org/en/latest/_images/SimpleGUICS2Pygame_64x64_t.png


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

.. _`documentation page`: http://simpleguics2pygame.readthedocs.org/
.. _Compatibility: http://simpleguics2pygame.readthedocs.org/en/latest/Compatibility.html
.. _`modules page`: http://simpleguics2pygame.readthedocs.org/en/latest/modules.html
.. _this: https://stackoverflow.com/questions/16387770/how-to-integrate-simplegui-with-python-2-7-and-3-0-shell
.. _Tips: http://simpleguics2pygame.readthedocs.org/en/latest/Tips.html


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
.. _pip: https://pypi.python.org/pypi/pip
.. _Pygame: http://www.pygame.org/


Test installation
-----------------
You can run the little script_ ``SimpleGUICS2Pygame_check.py``
to check if all required modules are installed.

Examples of good installation:
`result in Python 2`_
and
`result in Python 3`_.

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
.. _`Complete installation on Window$ in few steps`: https://simpleguics2pygame.readthedocs.org/en/latest/index.html#complete-installation-on-window-in-few-steps
.. _`Unofficial Windows Binaries matplotlib`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
.. _`Unofficial Windows Binaries pip`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip
.. _`Unofficial Windows Binaries Pygame`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame


Examples of CodeSkulptor and SimpleGUICS2Pygame use
===================================================
You can see examples in `SimpleGUICS2Pygame/example/`_ subdirectory from the sources archives.

.. _`SimpleGUICS2Pygame/example/`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/example/

Or online:
`Python programs running in CodeSkulptor`_ .

.. _`Python programs running in CodeSkulptor`: https://simpleguics2pygame.readthedocs.org/en/latest/_static/links/prog_links.htm


Author |OPi|
============
| Olivier Pirson OPi --- http://www.opimedia.be/
| olivier_pirson_opi@yahoo.fr
|
| Other free softwares on my Bitbucket account: https://bitbucket.org/OPiMedia
|

.. |OPi| image:: http://www.opimedia.be/_png/OPi.png


Support me
==========
| If you are happy with this **free and free** project you can **support** me financially by donating **on my PayPal account** or with **Flattr**.
| Go to the link |Donate|_

.. _Donate: http://www.opimedia.be/donate/index.htm

.. |Donate| image:: http://www.opimedia.be/donate/_png/Paypal_Donate_92x26_t.png


License: GPLv3_ |GPLv3|
=======================
Copyright (C) 2013, 2014, 2015 Olivier Pirson

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

* SimpleGUITk_ is an *other implementation* of SimpleGUI of CodeSkulptor, using Tkinter and some others packages. It is really less complete and not updated. However it works for some programs.

* simplegui_ is a Python package which has the same name as SimpleGUI of CodeSkulptor, but it is *totally something else*.

.. _SimpleGUITk: https://pypi.python.org/pypi/SimpleGUITk

.. _simplegui: https://pypi.python.org/pypi/simplegui


Changes
=======
* 02.00.00 WORKING VERSION --- November 23, 2015

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

  - Splitted the big file ``simpleguics2pygame.py``.
  - Added ``example/presentation.py``.

  - Added ``example/stop_example.py``.

  - Corrected ``test/test_sound.py``.

  - Updated documentation. (Thanks to `John Gray`.)

  - Updated media and CodeSkulptor programs links.

* 01.09.00 --- January 1st, 2015

  - **Added ``_load_local_image()`` and ``_load_local_sound()`` functions.**
  - Added ``test/test_sound.py``.
  - Updated ``test/test_dir.py``.
  - Updated ``test/test_image.py``.

  - Added ``--fps n`` option.

  - Added Donate button in ``_draw_about()`` panel.

* 01.08.01 --- October 9, 2014

  - Added information when pygame is not installed.

  - Corrected local filename bug in ``_load_media()``. (Thanks to `Sergey Sorokin`_.)
  - Updated documentation.

.. _`Sergey Sorokin`: https://bitbucket.org/SergeyVlSorokin

* 01.08.00 --- October 4, 2014

  - Added alternative grey colors.
  - Added HSL and HSLA colors format.
  - Added ``test/test_colors_html_hsla.py``.
  - Updated CodeSkulptor programs links.
  - Updated ``codeskulptor_lib``.
  - Updated ``test/test_colors_html_rgba.py``.

  - Updated media links.

* 01.07.00 --- September 2, 2014

  - Added ``plot_scatter()`` function in ``simpleplot`` module.
  - Added ``test/test_simpleplot_scatter.py``.
  - Updated ``test/test_dir.py``.
  - Updated documentation.
  - Updated CodeSkulptor programs links.

...

`Complete changelog`_

.. _`Complete changelog`: https://simpleguics2pygame.readthedocs.org/en/latest/ChangeLog.html
