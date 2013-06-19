.. -*- restructuredtext -*-

==================
SimpleGUICS2Pygame
==================

It is primarily a standard Python_ (2 **and** 3) module
reimplementing the SimpleGUI particular module of CodeSkulptor_
(a browser Python interpreter).

Require Pygame_
(except for the Timer class)
(`Unofficial Windows Binaries`_).

| Simply change
|   ``import simplegui``
| by
|   ``import SimpleGUICS2Pygame.simpleguics2pygame as simplegui``
| in your CodeSkulptor program and run it in *standard Python* with this module (and Pygame).

`Online HTML documentation`_ on `DragonSoft DS`_ website.

Sources on Bitbucket:
https://bitbucket.org/OPiMedia/simpleguics2pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`DragonSoft DS`: http://www.opimedia.be/DS/SimpleGUICS2Pygame/
.. _`Online HTML documentation`: http://www.opimedia.be/DS/SimpleGUICS2Pygame/doc_html/index.htm
.. _Pygame: http://www.pygame.org/
.. _Python: http://www.python.org/
.. _`Unofficial Windows Binaries`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame



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
