Compatibility
=============

Compatibility between SimpleGUI of CodeSkulptor and SimpleGUICS2Pygame
----------------------------------------------------------------------
* With SimpleGUI of CodeSkulptor_, some things (like fonts, buttons…) are browser dependents.
  That is to say that there are some differences from one browser to another.
  Therefore it is normal that these elements are also slightly different with SimpleGUICS2Pygame.

* With SimpleGUI of CodeSkulptor_, supported sound formats are also browser dependents.

  .. warning::
    With SimpleGUICS2Pygame,
    MP3 is **not** supported. Only OGG and uncompressed WAV are supported.

  I recommend to always use the OGG format.
  See Tips_.

* .. warning::
    With SimpleGUICS2Pygame,
    ``Frame.start()`` is blocking
    until ``Frame.stop()`` execution or closing window.
    So timers must be started *before*, and states must be initialized *before*.
    (Or maybe after by a handler function.)

* .. warning::
    With SimpleGUICS2Pygame,
    if your program is terminated,
    then windows opened by
    ``plot_bars()``, ``plot_lines()`` and ``plot_scatter()``
    will be closed automatically.
    You can use the specific function ``_block()``
    to block the program until closing all windows.

* See Tips_ to run specific code.

.. _Tips: Tips.html


Compatibility between Python 2 and Python 3
-------------------------------------------

CodeSkulptor_ implements a subset of Python 2.

You can use SimpleGUICS2Pygame with Python 2 and Python 3.

* The division ``/`` don't have the same behavior in Python 2 and Python 3:
  http://docs.python.org/3/whatsnew/3.0.html#integers .

  * In Python 2 (and CodeSkulptor): ``3/2 == 1`` and ``3/2.0 == 1.5``
  * In Python 3: ``3/2 == 3/2.0 == 1.5``

  ``3//2 == 1`` and ``3//2.0 == 1.0`` everywehre.

  (You can add
  ``from __future__ import division``
  *on the top* of your program, and Python 2 mimic Python 3 division.
  But then *CodeSkulptor failed*!)

* Rounded behavior is also different:
  http://docs.python.org/3/whatsnew/3.0.html#builtins .

  * In Python 2 (and CodeSkulptor): ``round(1.5) == 2.0`` and ``round(2.5) == 3.0``
  * In Python 3: ``round(1.5) == round(2.5) == 2``

* ``print`` is a function in Python 3:
  http://docs.python.org/3/whatsnew/3.0.html#print-is-a-function .

  * In Python 2 (and CodeSkulptor): ``print 'Hello real world!', 42``
  * In Python 3: ``print('Hello real world!', 42)``

  With only one argument, ``print('Hello real world! ' + str(42))`` run everywhere.

  (You can add
  ``from __future__ import print_function``
  *on the top* of your program, and Python 2 mimic Python 3 print function.
  But then *CodeSkulptor failed*!)

.. _CodeSkulptor: http://www.codeskulptor.org/
