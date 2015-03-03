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

`Online HTML documentation`_ on **Read The Docs**.

| **Sources** and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on **PyPI**: https://pypi.python.org/pypi/SimpleGUICS2Pygame .

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
|

.. |OPi| image:: http://www.opimedia.be/_png/OPi.png

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



Changes
=======
* March 3, 2015

  - Updated documentation.

  - Updated media links.

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

* 01.06.03 --- July 24, 2014

  - Implemented ``width`` parameter in ``add_label()``.
  - Added ``test/test_button_label.py``.

* 01.06.02 --- July 18, 2014

  - Corrected stupid error in ``add_label()``.

* 01.06.01 --- July 17, 2014

  - Added (fake) width parameter in ``add_label()``.
  - Corrected gz archive of HTML offline documentation.

  - Added private members in all documentation.

* 01.06.00 --- June 16, 2014

...

`Complete changelog`_

.. _`Complete changelog`: https://simpleguics2pygame.readthedocs.org/en/latest/ChangeLog.html
