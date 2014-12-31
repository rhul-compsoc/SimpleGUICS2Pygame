SimpleGUICS2Pygame package's documentation
==========================================

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
(You can also use the online `SimpleGUI documentation on CodeSkulptor`_.)

| **Sources** and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on **PyPI**: https://pypi.python.org/pypi/SimpleGUICS2Pygame .

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`Online HTML documentation`: https://readthedocs.org/docs/simpleguics2pygame/en/latest/
.. _Python: http://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor`: http://www.codeskulptor.org/docs.html#simplegui-create_frame
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


Module ``simpleplot`` require matplotlib_
(and must be installed separately).

Modules ``simplegui_lib`` (and its submodules) and ``simpleguics2pygame`` require
(except for the Timer class) Pygame_
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
| Go to the links: |Donate|_
|

.. _Donate: http://www.opimedia.be/donate/index.htm
.. |Donate| image:: _static/img/Paypal_Donate_92x26_t.png



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
