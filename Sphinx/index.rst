SimpleGUICS2Pygame package's documentation
==========================================
.. |SimpleGUICS2Pygame| image:: _static/img/SimpleGUICS2Pygame_32x32_t.png

.. toctree::
   :maxdepth: 2

   package_init
   codeskulptor
   codeskulptor_lib
   simplegui_lib
   simpleguics2pygame
   simpleguics2pygame_private



SimpleGUICS2Pygame
------------------
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
------------
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
--------
You can see examples in ``SimpleGUICS2Pygame/example/`` subdirectory from the sources archives.

Or online in CodeSkulptor:
http://www.opimedia.be/DS/SimpleGUICS2Pygame/doc_html/_static/links/prog_links.htm .


Author |OPi|
------------
| Olivier Pirson OPi --- http://www.opimedia.be/
| olivier_pirson_opi@yahoo.fr

.. |OPi| image:: _static/img/OPi_t.png



License: GPLv3_ |GPLv3|
-----------------------
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
.. |GPLv3| image:: _static/img/gplv3-88x31.png



Tips
----

CodeSkulptor
~~~~~~~~~~~~
CodeSkulptor_ is an interpreter running in a browser.

It is the environment used in the course
`An Introduction to Interactive Programming in Python`_
(Coursera 2013).

.. _`An Introduction to Interactive Programming in Python`: https://www.coursera.org/course/interactivepython


To use a program from CodeSkulptor in *standard Python* (with this package),
you need to change
``import simplegui``
by
``import SimpleGUICS2Pygame.simpleguics2pygame as simplegui``.

You can write this

.. code-block:: python

    try:
        import simplegui
    except:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

and your program run both in CodeSkulptor and *standard Python*.


| In this package a little script ``cs2both.py`` can help to quickly make this changement on program downloaded from CodeSkulptor.
| Run ``python cs2both.py yourprogram.py``.
| The file ``yourprogram.py`` is copied to ``yourprogram.py.bak`` before changing.


You can write this

.. code-block:: python

    try:
        import codeskulptor
        import simplegui

        import user16_DmDJwXW1dy0Sw1u as codeskulptor_lib
        import user16_v0hIgQGF5JqtOUQ as simplegui_lib
    except:
        import SimpleGUICS2Pygame.codeskulptor as codeskulptor
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

        import SimpleGUICS2Pygame.codeskulptor_lib as codeskulptor_lib
        import SimpleGUICS2Pygame.simplegui_lib as simplegui_lib

to use also the other modules. But specify only those you use.


Colors
~~~~~~
The color parameter used by drawing functions must be in the following formats:

* ``'#rrggbb'`` with rr, gg, bb hexadecimal numbers on 2 figures
* ``'#rgb'`` with r, g, b  hexadecimal numbers on 1 figure
* ``'rbg(red,blue,green)'`` with red, blue, green 0 <= integer <= 255
* ``'rgba(red,blue,green,alpha)'`` with red, blue, green 0 <= integer <= 255 and alpha between 0 and 1
* a constant name in this list http://www.w3schools.com/html/html_colornames.asp .

See the official HTML colors:
http://www.opimedia.be/DS/mementos/colors.htm .


Compatibility
~~~~~~~~~~~~~
Be careful

* CodeSkulptor don't distinguish int and float.

  The division ``/`` don't have the same behavior in Python 2 and Python 3:
  http://docs.python.org/3/whatsnew/3.0.html#integers .

  Rounded behavior is also different:
  http://docs.python.org/3/whatsnew/3.0.html#builtins .

  (You can add
  ``from __future__ import division``
  *on the top* of your program, and Python 2 mimic Python 3 division.
  But then *CodeSkulptor failed*!)

* ``Frame.start()`` is blocking until ``Frame.stop()`` execution or closing window.
  So timers must be started *before*, and states must be initialized *before*.
  (Or maybe after by a handler function.)

* ``math.abs()`` doesn't exist in In Python, instead use ``abs()``.

* ``print`` is a function in Python 3:
  http://docs.python.org/3/whatsnew/3.0.html#print-is-a-function .

  (You can add
  ``from __future__ import print_function``
  *on the top* of your program, and Python 2 mimic Python 3 print function.
  But then *CodeSkulptor failed*!)


English
~~~~~~~
I don't really speak English, I'm speak French.
So this documentation and comments in the source code are likely horrible. ;-)


Options
~~~~~~~
When you run a program you can use following options:
``python yourprogram.py [SimpleGUICS2Pygame options] [application options]``

* ``--default-font``: Use Pygame default font instead serif, monospace...
* ``--display-fps``: Display FPS average on the canvas.
* ``--fullscreen``: Fullscreen mode.
* ``--keep-timers``: Keep running timers when close frame without ask.
* ``--no-border``: Window without border.
* ``--no-controlpanel``: Hide the control panel (and status boxes).
* ``--no-load-sound``: Don't load any sound.
* ``--no-status``: Hide two status boxes.
* ``--print-load-medias``: Print URLs or local filenames loaded.
* ``--stop-timers``: Stop all timers when close frame.

If an argument not in this list then next arguments are ignored.

Example: ``python yourprogram.py --no-controlpanel --stop-timers --foo --fullscreen``
run ``yourprogram.py`` with the control panel hidden and timers will stoped.
But SimpleGUICS2Pygame ignore ``--foo`` and ``--fullscreen``.

SimpleGUICS2Pygame options are read when the module ``simpleguics2pygame`` is imported.


Run
``python yourprogram.py``
then asserts is active and this package is (intentionnaly) very strict. So maybe "correct" program in CodeSkulptor failed!
It is a good point to develop and write correct programs.
But if you want just run a program,
``python -O yourprogram.py``
then all asserts is *inactive*.


Ressources
~~~~~~~~~~
`Online images & sounds links`_

.. _`Online images & sounds links`: _static/links/img_snd_links.htm

`Python programs running in CodeSkulptor`_

.. _`Python programs running in CodeSkulptor`: _static/links/prog_links.htm


Sounds
~~~~~~
Supported formats are supported formats by Pygame: OGG and uncompressed WAV.
To convert your sounds, you can use Audacity_ and FFmpeg_.

.. _Audacity: http://audacity.sourceforge.net/
.. _FFmpeg: http://www.ffmpeg.org/
