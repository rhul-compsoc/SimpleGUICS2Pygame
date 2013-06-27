.. -*- restructuredtext -*-

==================
SimpleGUICS2Pygame
==================

It is primarily a standard Python_ (2 **and** 3) module
reimplementing the SimpleGUI particular module of CodeSkulptor_
(a browser Python interpreter).

| Simply change
|   ``import simplegui``
| by
|   ``import SimpleGUICS2Pygame.simpleguics2pygame as simplegui``
| in your CodeSkulptor program and run it in *standard Python* with this module (and Pygame).

`Online HTML documentation`_ on `DragonSoft DS`_ website.

| Sources and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on PyPI: https://pypi.python.org/pypi/SimpleGUICS2Pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`DragonSoft DS`: http://www.opimedia.be/DS/SimpleGUICS2Pygame/
.. _`Online HTML documentation`: http://www.opimedia.be/DS/SimpleGUICS2Pygame/doc_html/index.htm
.. _Python: http://www.python.org/


Installation
============
If pip_ is installed on your platform you can do:

>>> pip install SimpleGUICS2Pygame


Else, download the archive ``SimpleGUICS2Pygame-?.tar.gz``, unzip it ``somewhere``.
Next in the ``somewhere/SimpleGUICS2Pygame-?/SimpleGUICS2Pygame`` subdirectory run:

>>> python setup.py install


Modules ``simplegui_lib`` and ``simpleguics2pygame`` require
(except for the Timer class) Pygame_ .

On Window$:

* You can use the binary installer ``SimpleGUICS2Pygame-?.exe`` if it available to your machine.

* You can easily install pip and Pygame,
  see `Unofficial Windows Binaries pip`_ and `Unofficial Windows Binaries Pygame`_.

* You can use 7-Zip_ to unzip archive.

.. _7-Zip: http://www.7-zip.org/
.. _pip: https://pypi.python.org/pypi/pip
.. _Pygame: http://www.pygame.org/
.. _`Unofficial Windows Binaries pip`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip
.. _`Unofficial Windows Binaries Pygame`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame


Examples
========
You can see examples in ``SimpleGUICS2Pygame/example/`` subdirectory from the sources archives.

Or online in CodeSkulptor:
http://www.opimedia.be/DS/SimpleGUICS2Pygame/doc_html/_static/links/prog_links.htm .


Author |OPi|
============
| Olivier Pirson OPi --- http://www.opimedia.be/
| olivier_pirson_opi@yahoo.fr

.. |OPi| image:: http://www.opimedia.be/_png/OPi.png



License: GPLv3_ |GPLv3|
=======================
Copyright (C) 2013 Olivier Pirson

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



Changes
=======
*

  - Added ``Frame._set_canvas_background_image()`` function.

  - Memoization of downloaded images and sounds.
  - Changed save in local directory to avoid conflict.

  - Added test/test_image.py.

  - Added ``--overwrite-downloaded-medias`` and ``--save-downloaded-medias`` options.

  - Display versions in ``script/SimpleGUICS2Pygame_check.py``.

* 00.91.00 --- June 23, 2013

  - Changed installation program to build distributions (now ``setuptools`` is used).
  - Added ``--print-load-medias`` option.
  - Added ``script/SimpleGUICS2Pygame_check.py`` and moved and updated ``cs2both.py``.

  - Now, ``_set_option_from_argv()`` deleted SimpleGUICS2Pygame options after use.

  - Memoization of Pygame fonts.
  - Added ``--default-font`` option.

  - Many cosmetic changes to respect PEP 8.
  - Updated media and CodeSkulptor programs links.

  - Some precisions and English corrections in the documentation.
  - Added some CodeSkulptor programs links.

  - example/Memory.py: moved image locations.
  - example/Nostalgic_Basic_Blitz.py : added spacebar information.

* 00.90.10 --- June 19, 2013

  - Adapted button, label and input to display multine text.
  - Simplified handler functions transmitted to ``add_button()`` in some programs.
  - Added example/Nostalgic_Basic_Blitz.py.

  - Changed ``default_pygame_color`` param of ``_simpleguicolor_to_pygamecolor()`` function (now installation is ok even if Pygame not installed).

  - Moved ``_VERSION`` and ``_WEBSITE`` constants from ``simpleguics2pygame.py`` to ``__init__.py``.
  - Removed ``enumerate()`` function from ``codeskulptor_lib`` (now implemented natively by CodeSkulptor).
  - Added ``--display-fps`` option.
  - Added example/RiceRocks_Asteroids.py.
  - Updated some CodeSkulptor programs links.
  - Added some new media links.
  - Added some details in documentations.
  - Some cosmetic changes.

* 00.90.00 --- June 13, 2013

  - First public version.
