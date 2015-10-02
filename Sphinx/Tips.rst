Tips
====

CodeSkulptor
------------
CodeSkulptor_ is a Python implementation running in a browser.
It implements a subset of Python 2.

It is the environment used in the course
`An Introduction to Interactive Programming in Python`_
(Coursera).

.. _`An Introduction to Interactive Programming in Python`: https://www.coursera.org/course/interactivepython
.. _CodeSkulptor: http://www.codeskulptor.org/


To use a program from CodeSkulptor in *standard Python* (with this package),
you need to change
``import simplegui``
by
``import SimpleGUICS2Pygame.simpleguics2pygame as simplegui``.

**You can write** this

.. code-block:: python

    try:
        import simplegui
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

and your program **run both** in CodeSkulptor and *standard Python*.


| In this package a little script_ ``cs2both.py`` can help to quickly make this changement on program downloaded from CodeSkulptor.
| Run ``python cs2both.py yourprogram.py``.
| The file ``yourprogram.py`` is copied to ``yourprogram.py.bak`` before changing.

.. _script: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/script/

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
        import user40_sK3vMO7yQIMVwUr as simplegui_lib
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
* a constant name in this list http://www.w3schools.com/html/html_colornames.asp .

See the official HTML colors:
http://www.opimedia.be/DS/mementos/colors.htm .


Command line options
--------------------
When you run a program you can use following options:
``python yourprogram.py [SimpleGUICS2Pygame options] [application options]``

* ``--default-font``: Use Pygame default font instead serif, monospace... (this is faster if you display a lot of text).
* ``--display-fps``: Display FPS average on the canvas.
* ``--fps n``: Set Frame Per Second (default is 60 FPS).
* ``--fullscreen``: Fullscreen mode.
* ``--keep-timers``: Keep running timers when close frame without ask.
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

Example: ``python yourprogram.py --no-controlpanel --stop-timers --foo --fullscreen``
run ``yourprogram.py`` with the control panel hidden and timers will stoped.
But SimpleGUICS2Pygame ignore ``--foo`` and ``--fullscreen``.
``yourprogram.py`` application receive ``--foo --fullscreen`` options.


Download medias
---------------
Run ``python yourprogram.py --save-downloaded-medias --print-load-medias`` once.
Images and sounds used (from URLs) will be saved in local directory (``_img/`` et ``_snd/`` by default).
Next simply run ``python yourprogram.py`` and the medias will be loaded from these local directories.

For example,
``load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png')``
save image to
``_img/commondatastorage.googleapis.com/codeskulptor_assets/lathrop/double_ship.png``.


Python assertions option
------------------------
Run
``python yourprogram.py``
then asserts is active and this package is (intentionnaly) very strict. So maybe "correct" program in CodeSkulptor failed!
It is a good point to develop and write *correct programs*.
But if you want just run a program (or run faster),
``python -O yourprogram.py``
then all asserts is *inactive*.


Ressources: images, sounds, programs
------------------------------------
`Online images & sounds links`_

.. _`Online images & sounds links`: _static/links/img_snd_links.htm

`Python programs running in CodeSkulptor`_

.. _`Python programs running in CodeSkulptor`: _static/links/prog_links.htm


Sounds
------
Supported formats are supported formats by Pygame: OGG and uncompressed WAV.
To convert your sounds, you can use Audacity_ and FFmpeg_.

.. _Audacity: http://audacity.sourceforge.net/
.. _FFmpeg: http://www.ffmpeg.org/
