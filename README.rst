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

|SimpleGUICS2Pygame|

`Online HTML documentation`_ on Read The Docs.

| Sources and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on PyPI: https://pypi.python.org/pypi/SimpleGUICS2Pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`Online HTML documentation`: https://readthedocs.org/docs/simpleguics2pygame/en/latest/
.. _Python: http://www.python.org/
.. |SimpleGUICS2Pygame| image:: https://simpleguics2pygame.readthedocs.org/en/latest/_images/SimpleGUICS2Pygame_64x64_t.png


Installation
============
If pip_ is installed on your platform you can do:

>>> pip install SimpleGUICS2Pygame


Else, download the archive ``SimpleGUICS2Pygame-?.tar.gz``, unzip it ``somewhere``.
Next in the ``somewhere/SimpleGUICS2Pygame-?/`` subdirectory run:

>>> python setup.py install


Modules ``simplegui_lib`` and ``simpleguics2pygame`` require
(except for the Timer class) Pygame_
(and must be installed separately).

On Window$:

* You can use the binary installer ``SimpleGUICS2Pygame-?.exe`` if it available to your machine.

* You can easily install pip and Pygame,
  see `Unofficial Windows Binaries pip`_ and `Unofficial Windows Binaries Pygame`_.

* You can use 7-Zip_ to unzip archive.

See `Complete installation on Window$ in few steps`_.

.. _7-Zip: http://www.7-zip.org/
.. _`Complete installation on Window$ in few steps`: https://simpleguics2pygame.readthedocs.org/en/latest/index.html#complete-installation-on-window-in-few-steps
.. _pip: https://pypi.python.org/pypi/pip
.. _Pygame: http://www.pygame.org/
.. _`Unofficial Windows Binaries pip`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip
.. _`Unofficial Windows Binaries Pygame`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame


Examples
========
You can see examples in ``SimpleGUICS2Pygame/example/`` subdirectory from the sources archives.

Or online:
`Python programs running in CodeSkulptor`_ .

.. _`Python programs running in CodeSkulptor`: https://simpleguics2pygame.readthedocs.org/en/latest/_static/links/prog_links.htm


Author |OPi|
============
| Olivier Pirson OPi --- http://www.opimedia.be/
| olivier_pirson_opi@yahoo.fr

.. |OPi| image:: http://www.opimedia.be/_png/OPi.png



License: GPLv3_ |GPLv3|
=======================
Copyright (C) 2013, 2014 Olivier Pirson

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
* May 27, 2014

  - Updated media and CodeSkulptor programs links.

* 01.05.00 --- May 25, 2014

  - Added cache for colors and option ``--print-stats-cache``.
  - First public version of ``.hgignore`` and ``Makefile``.
  - Off the mixer if no sound is loaded.
  - Updated ``example/RiceRocks_Asteroids.py``.
  - Updated documentation.

  - Updated ``example/Spaceship_prototype.py``.

  - Updated ``example/Blackjack.py``.

  - Updated ``example/Memory.py``.

  - Updated ``example/Pong.py``.

  - Cosmetic changes in some example programs.

  - Updated ``test/test_all.py``.

  - Better order Pygame initalization.
  - Updated ``script/cs2both.py`` and ``script/SimpleGUICS2Pygame_check.py``.

  - Updated ``simplegui_lib_keys.py`` and ``example/keys.py``.
  - Updated ``example/Stopwatch.py``.

  - Changed filename used by ``_load_media()`` (use now the query part of URLs).

  - Added precision to Window$ installation.
  - Updated media and CodeSkulptor programs links.

* 01.04.00 --- December 16, 2013

...

`Complete changelog`_

.. _`Complete changelog`: https://simpleguics2pygame.readthedocs.org/en/latest/ChangeLog.html
