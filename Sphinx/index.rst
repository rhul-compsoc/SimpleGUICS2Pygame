SimpleGUICS2Pygame package's documentation
==========================================

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
(You can also use the online `SimpleGUI documentation on CodeSkulptor`_.)
Read Compatibility_ and Tips_ sections.


| **Sources** and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on **PyPI**: https://pypi.python.org/pypi/SimpleGUICS2Pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _Compatibility: Tips.html#compatibility
.. _`Online HTML documentation`: https://readthedocs.org/docs/simpleguics2pygame/en/latest/
.. _Python: http://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor`: http://www.codeskulptor.org/docs.html
.. _Tips: Tips.html

.. |SimpleGUICS2Pygame| image:: _static/img/SimpleGUICS2Pygame_64x64_t.png

|


Installation
------------
If pip_ is installed on your platform you can do:

>>> pip install SimpleGUICS2Pygame

(If several Python implementations are installed,
maybe you must use something like `pip2` or `pip3` instead `pip` command.)


Without pip, download the archive ``SimpleGUICS2Pygame-?.tar.gz``, unzip it ``somewhere``.
Next in the ``somewhere/SimpleGUICS2Pygame-?/`` subdirectory run:

>>> python setup.py install

In both cases, you must use **admin access**. So with Linux you will probably do:

>>> sudo [your command]


Module ``simpleplot`` require matplotlib_
(and must be installed separately).

Modules ``simplegui_lib`` (and its submodules) and ``simpleguics2pygame`` (except for the Timer class)
require Pygame_
(and must be installed separately).

You can run the little script_ ``SimpleGUICS2Pygame_check.py``
to check if required modules are installed.

.. _matplotlib: http://matplotlib.org/
.. _pip: https://pypi.python.org/pypi/pip
.. _Pygame: http://www.pygame.org/
.. _script: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/script/


Update
~~~~~~
With pip_ installed on your plaftorm you can update SimpleGUICS2Pygame:

>>> pip install SimpleGUICS2Pygame --upgrade


Complete installation on Window$ in few steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download and run the good `Pygame` installation file: `Unofficial Windows Binaries Pygame`_.  (Only require for ``simplegui_lib``, its submodules and ``simpleguics2pygame``.)

2. Download and run the good `matplotlib` installation file (**and** all its requirements): `Unofficial Windows Binaries matplotlib`_. (Only require for ``simpleplot``.)

3. Download and run the good `setuptools` installation file: `Unofficial Windows Binaries setuptools`_.

4. Download and run the good `pip` installation file: `Unofficial Windows Binaries pip`_.

5. Run in the *Command Prompt* (maybe with *Administrator* rights): ``pip install SimpleGUICS2Pygame`` . (Probably the ``pip`` command aren't in your ``PATH``, so add it or move in the subdirectory of ``pip`` with the ``CD`` command. This subdirectory is something like ``C:\Python?\Scripts\`` .)

.. _`Unofficial Windows Binaries matplotlib`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
.. _`Unofficial Windows Binaries pip`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip
.. _`Unofficial Windows Binaries Pygame`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
.. _`Unofficial Windows Binaries setuptools`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools


Examples of CodeSkulptor and SimpleGUICS2Pygame use
---------------------------------------------------
You can see examples in ``SimpleGUICS2Pygame/example/`` subdirectory from the sources archives.

Or online:
`Python programs running in CodeSkulptor`_ .

.. _`Python programs running in CodeSkulptor`: _static/links/prog_links.htm


Author |OPi|
------------
| Olivier Pirson OPi --- http://www.opimedia.be/
| olivier_pirson_opi@yahoo.fr
|

.. |OPi| image:: _static/img/OPi_t.png

| If you are happy with this **free and free** project you can **support** me financially by donating **on my PayPal account** or with **Flattr**.
| Go to the link |Donate|_
|

.. _Donate: http://www.opimedia.be/donate/index.htm

.. |Donate| image:: _static/img/Paypal_Donate_92x26_t.png


Note that
---------

* SimpleGUITk_ is an *other implementation*, using Tkinter and some others packages. It is really less complete and not updated. However it works for some programs.

* simplegui_ is a Python package which has the same name as SimpleGUI of CodeSkulptor, but it is *totally something else*.

.. _SimpleGUITk: https://pypi.python.org/pypi/SimpleGUITk/1.1.3

.. _simplegui: https://pypi.python.org/pypi/simplegui/0.1.1



Summary
=======

.. toctree::
   :maxdepth: 3

   package_init

   modules

   Tips

   License

   Bugs

   ChangeLog



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
