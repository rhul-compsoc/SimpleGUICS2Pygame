Tips
====

CodeSkulptor
------------
CodeSkulptor_ is a Python implementation (in JavaScript) running in a browser.
It implements a subset of Python 2.

It is the environment used in the MOOC
`An Introduction to Interactive Programming in Python`_
(Rice University, Coursera).

.. _`An Introduction to Interactive Programming in Python`: https://www.coursera.org/learn/interactive-python-1
.. _CodeSkulptor: http://www.codeskulptor.org/


To use a program from CodeSkulptor in *standard Python* (with this package),
you need to change
``import simplegui``
by
``import SimpleGUICS2Pygame.simpleguics2pygame as simplegui``.

**The right way to do** is to write this

.. code-block:: python

    try:
        import simplegui
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

and your program **runs both** in CodeSkulptor and *standard Python*.

So, if your program runs in CodeSkulptor, it imports ``simplegui``.
Else, an ``ImportError`` exception will be raised,
and then it will imports ``SimpleGUICS2Pygame.simpleguics2pygame``
and it renamed to ``simplegui``.


| In this package a little script_ ``cs2both.py`` can help to quickly make this changement on program downloaded from CodeSkulptor.
| Run ``python cs2both.py yourprogram.py``.
| The file ``yourprogram.py`` is copied to ``yourprogram.py.bak`` before changing.

.. _script: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/script/

|
|

To use also the **other modules**,
you can write this.
But specify only those you use.

.. code-block:: python

    try:
        import simplegui

        import codeskulptor
        import numeric
        import simpleplot

        import user38_ZmhOVHGm2lhVRhk as codeskulptor_lib
        import user40_Jax5K1pl4O1JMFp as simplegui_lib
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

        import SimpleGUICS2Pygame.codeskulptor as codeskulptor
        import SimpleGUICS2Pygame.numeric as numeric
        import SimpleGUICS2Pygame.simpleplot as simpleplot

        import SimpleGUICS2Pygame.codeskulptor_lib as codeskulptor_lib
        import SimpleGUICS2Pygame.simplegui_lib as simplegui_lib

To run **specific code** on CodeSkulptor_ or with SimpleGUICS2Pygame,
you can write this

.. code-block:: python

    try:
        import simplegui

        SIMPLEGUICS2PYGAME = False
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

        SIMPLEGUICS2PYGAME = True

And then you can run specific code simply by testing ``SIMPLEGUICS2PYGAME``.


Colors
------
The color parameter used by drawing functions must be in the following formats:

* ``'#rrggbb'`` with rr, gg, bb hexadecimal numbers on 2 figures
* ``'#rgb'`` with r, g, b  hexadecimal numbers on 1 figure
* ``'rbg(red,blue,green)'`` with red, blue, green 0 <= integer <= 255
* ``'rgba(red,blue,green,alpha)'`` with red, blue, green 0 <= integer <= 255 and alpha between 0 and 1
* a constant name in this list https://www.w3schools.com/colors/colors_names.asp .

See the official HTML colors:
http://www.opimedia.be/DS/mementos/colors.htm .


Command line options
--------------------
When you run a program you can use following options:
``python yourprogram.py [SimpleGUICS2Pygame options] [application options]``

* ``--default-font``: Use Pygame default font instead serif, monospace… (this is faster if you display a lot of text).
* ``--display-fps``: Display FPS average on the canvas.
* ``--fps n``: Set Frame Per Second (default is 60 FPS).
* ``--frame-padding n``: Set the padding in pixels found around the canvas
* ``--fullscreen``: Fullscreen mode.
* ``--keep-timers``: Keep running timers when close frame without ask.
* ``--last``: Mark this argument as the last  SimpleGUICS2Pygame's argument. (Do nothing else.)
* ``--no-border``: Window without border.
* ``--no-controlpanel``: Hide the control panel (and status boxes).
* ``--no-load-sound``: Don't load any sound.
* ``--no-status``: Hide two status boxes.
* ``--overwrite-downloaded-medias``: Download all images and sounds from Web and save in local directory even if they already exist.
* ``--print-load-medias``: Print URLs or local filenames loaded.
* ``--print-stats-cache``: After frame stopped, print some statistics of caches.
* ``--save-downloaded-medias``: Save images and sounds downloaded from Web that don't already exist in local directory.
* ``--stop-timers``: Stop all timers when close frame without ask.

If an argument is not in this list then it is ignored and all next arguments are ignored.

Arguments used by SimpleGUICS2Pygame is deleted to ``sys.argv``.

SimpleGUICS2Pygame options are read when the module ``simpleguics2pygame`` is imported.

Examples:
  * | ``python yourprogram.py --no-controlpanel --stop-timers --foo --fullscreen``
    | run ``yourprogram.py`` with the control panel hidden and timers will stoped. But SimpleGUICS2Pygame ignore ``--foo`` and ``--fullscreen``.
    | ``yourprogram.py`` application receive ``--foo --fullscreen`` options.

  * | ``python yourprogram.py --no-controlpanel --last --stop-timers --foo --fullscreen``
    | run ``yourprogram.py`` with the control panel hidden. But SimpleGUICS2Pygame ignore ``--stop-timers``, ``--foo`` and ``--fullscreen``.
    | ``yourprogram.py`` application receive ``--stop-timers --foo --fullscreen`` options.


Download medias
---------------
Run ``python yourprogram.py --save-downloaded-medias --print-load-medias`` once.
Images and sounds used (from URLs) will be saved in local directory (``_img/`` et ``_snd/`` by default).
Next simply run ``python yourprogram.py`` and the medias will be loaded from these local directories.

For example,
``load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png')``
save image to
``_img/commondatastorage.googleapis.com/codeskulptor_assets/lathrop/double_ship.png``.


Helper functions
----------------
This package contains 5 modules with several helper functions that you can also import online in CodeSkulptor:

  * `codeskulptor_lib`_ — some miscellaneous functions
  * `simplegui_lib_draw`_ — draw functions
  * `simplegui_lib_fps`_ — class to calculate and display Frames Per Second
  * `simplegui_lib_keys`_ — class to manage keyboard handling
  * `simplegui_lib_loader`_ — class to load images and sounds

.. _`codeskulptor_lib`: codeskulptor_lib.html
.. _`simplegui_lib_draw`: simplegui_lib_draw.html
.. _`simplegui_lib_fps`: simplegui_lib_fps.html
.. _`simplegui_lib_keys`: simplegui_lib_keys.html
.. _`simplegui_lib_loader`: simplegui_lib_loader.html

For example, to draw multiline text you can use `draw_text_multi()`_ from the `simplegui_lib_draw`_ module by:

.. _`draw_text_multi()`: simplegui_lib_draw.html#SimpleGUICS2Pygame.simplegui_lib_draw.draw_text_multi

.. code-block:: python

    try:
        import simplegui

        import user40_AeChfAkzlcqs3wG as simplegui_lib_draw
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

        import SimpleGUICS2Pygame.simplegui_lib as simplegui_lib_draw

    def draw(canvas):
        …
        draw_text_multi(canvas,
                        """line 1
    line 2
    line 3""", (x, y), size, 'white', 'serif')
        …


Python assertions option
------------------------
Run
``python yourprogram.py``
then asserts is active and this package is (intentionnaly) very strict. So maybe "correct" program in CodeSkulptor failed!
It is a good point to develop and write *correct programs*.
But if you want just run a program (or run faster),
``python -O yourprogram.py``
then all asserts is *inactive*.


Ressources: images, sounds and example programs
-----------------------------------------------
Online images_ & sounds_ links

.. _images: _static/links/img_links.html
.. _sounds: _static/links/snd_links.html

`Python programs running in CodeSkulptor`_

.. _`Python programs running in CodeSkulptor`: _static/links/prog_links.html


Sounds
------
Supported formats are supported formats by Pygame: OGG and uncompressed WAV.
To convert your sounds, you can use Audacity_ and FFmpeg_.

.. _Audacity: http://audacity.sourceforge.net/
.. _FFmpeg: http://www.ffmpeg.org/
