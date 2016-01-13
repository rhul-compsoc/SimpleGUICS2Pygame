#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/__init__ (January 13, 2016)

Standard Python_ (**2 and 3**) module
reimplementing the SimpleGUI particular module of CodeSkulptor_
(a browser Python interpreter).

Require Pygame_
(except for the Timer class)
(`Unofficial Windows Binaries`_)
(and must be installed separately).

`Online HTML documentation`_ on Read The Docs.
(You can also see the online `SimpleGUI documentation on CodeSkulptor`_.)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2015, 2016 Olivier Pirson
http://www.opimedia.be/

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _`Online HTML documentation`: http://simpleguics2pygame.readthedocs.org/
.. _Pygame: http://www.pygame.org/
.. _Python: http://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor`: http://www.codeskulptor.org/docs.html#simplegui-create_frame
.. _`Unofficial Windows Binaries`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
"""


#
# Set options
#############
from SimpleGUICS2Pygame.simpleguics2pygame._options \
    import _set_option_from_argv

try:
    del _options
except NameError:
    pass

try:
    _set_option_from_argv()

    del _set_option_from_argv
except NameError:
    pass


#
# Init Pygame
#############
from SimpleGUICS2Pygame.simpleguics2pygame._pygame_lib import *

try:
    del _pygame_lib
except NameError:
    pass


#
# Import all
############
from SimpleGUICS2Pygame.simpleguics2pygame.canvas import *

from SimpleGUICS2Pygame.simpleguics2pygame.control import *

from SimpleGUICS2Pygame.simpleguics2pygame.frame import *

from SimpleGUICS2Pygame.simpleguics2pygame.image import *

from SimpleGUICS2Pygame.simpleguics2pygame.keys import *

from SimpleGUICS2Pygame.simpleguics2pygame.sound import *

from SimpleGUICS2Pygame.simpleguics2pygame.timer import *

try:
    del canvas
except NameError:
    pass

try:
    del control
except NameError:
    pass

try:
    del frame
except NameError:
    pass

try:
    del image
except NameError:
    pass

try:
    del keys
except NameError:
    pass

try:
    del sound
except NameError:
    pass

try:
    del timer
except NameError:
    pass


try:
    del _colors
except NameError:
    pass

try:
    del _fonts
except NameError:
    pass

try:
    del _media
except NameError:
    pass
