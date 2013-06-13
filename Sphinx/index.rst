SimpleGUICS2Pygame's documentation
==================================
.. |SimpleGUICS2Pygame| image:: _static/img/SimpleGUICS2Pygame_cartoon_32x32_t.png

.. toctree::
   :maxdepth: 2

   codeskulptor
   codeskulptor_lib
   simplegui_lib
   simpleguics2pygame
   simpleguics2pygame_private



SimpleGUICS2Pygame
------------------
It is a standard Python_ (2 **and** 3) module
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

Sources on Bitbucket:
https://bitbucket.org/OPiMedia/simpleguics2pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _Pygame: http://www.pygame.org/
.. _Python: http://www.python.org/
.. _`Unofficial Windows Binaries`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame



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

        import user16_9JI3lqVw8Bpq387 as codeskulptor_lib
        import user16_Qpss15rD1ETZL7l as simplegui_lib
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

* ``Frame.start()`` is blocking until ``Frame.stop()`` execution or closing window.
  So timers must be started *before*. (Or after by a handler function.)

* ``print`` is a function in Python 3:
  http://docs.python.org/3/whatsnew/3.0.html#print-is-a-function .


English
~~~~~~~
I don't really speak English, I'm speak French.
So this documentation and comments in the source code are likely horrible. ;-)


Installation
~~~~~~~~~~~~
Unzip the archive ``SimpleGUICS2Pygame-?.tar.gz``
and then in the ``SimpleGUICS2Pygame-?/`` directory
run ``python setup.py install``.

Or use the Window$ installer ``SimpleGUICS2Pygame-?.exe``.


To install easily the Pygame module on Window$, see `Unofficial Windows Binaries`_ .

.. _`Unofficial Windows Binaries`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame


Options
~~~~~~~
When you run a program you can use following options:
``python yourprogram.py [options]``

* ``--fullscreen```: Fullscreen mode.
* ``--keep-timers``: Keep running timers when close frame without ask.
* ``--no-border``: Window without border.
* ``--no-controlpanel``: Hide the control panel (and status boxes).
* ``--no-load-sound``: Don't load any sound.
* ``--no-status``: Hide two status boxes.
* ``--stop-timers``: Stop all timers when close frame.


Run
``python yourprogram.py``
then asserts is active and this module is (intentionnaly) very strict. So maybe "correct" program in CodeSkulptor failed!
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
