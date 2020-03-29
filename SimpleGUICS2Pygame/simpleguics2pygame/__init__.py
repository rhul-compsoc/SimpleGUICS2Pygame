# -*- coding: latin-1 -*-

"""
simpleguics2pygame/__init__

Standard Python_ (**2 and 3**) module
reimplementing the SimpleGUI particular module of CodeSkulptor_ and CodeSkulptor3_
(a Python browser environment).

Require Pygame_
(except for the Timer class).

`Online HTML documentation`_ on Read The Docs.
(You can also see the online `SimpleGUI documentation on CodeSkulptor`_
or `SimpleGUI documentation on CodeSkulptor3`_.)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _CodeSkulptor3: https://py3.codeskulptor.org/
.. _`Online HTML documentation`: https://simpleguics2pygame.readthedocs.io/
.. _Pygame: https://www.pygame.org/
.. _Python: https://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor`: http://www.codeskulptor.org/docs.html#simplegui-create_frame
.. _`SimpleGUI documentation on CodeSkulptor3`: https://py3.codeskulptor.org/docs.html#simplegui-create_frame

:license: GPLv3 --- Copyright (C) 2013-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 29, 2020
"""  # noqa

from __future__ import print_function

# print('IMPORT', __name__)


import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

if 'os' in dir():
    del os


#
# Set arguments
###############
import SimpleGUICS2Pygame.simpleguics2pygame._arguments  # noqa  # pylint: disable=wrong-import-position,no-name-in-module

if '_arguments' in dir():
    del _arguments  # pylint: disable=undefined-variable


#
# Import timer (Pygame is not required)
#######################################
from SimpleGUICS2Pygame.simpleguics2pygame.timer import *  # noqa  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module

if 'timer' in dir():
    del timer  # pylint: disable=undefined-variable


#
# Init Pygame
#############
from SimpleGUICS2Pygame.simpleguics2pygame._pygame_init import *  # noqa  # pylint: disable=no-name-in-module,wildcard-import,wrong-import-position

if '_pygame_init' in dir():
    del _pygame_init  # pylint: disable=undefined-variable


#
# Import all others (Pygame is required)
########################################
from SimpleGUICS2Pygame.simpleguics2pygame.keys import *  # noqa  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module

if 'keys' in dir():
    del keys  # pylint: disable=undefined-variable

from SimpleGUICS2Pygame.simpleguics2pygame.control import *  # noqa  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module

if 'control' in dir():
    del control  # pylint: disable=undefined-variable


from SimpleGUICS2Pygame.simpleguics2pygame.image import *  # noqa  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module

if 'image' in dir():
    del image  # pylint: disable=undefined-variable

from SimpleGUICS2Pygame.simpleguics2pygame.sound import *  # noqa  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module

if 'sound' in dir():
    del sound  # pylint: disable=undefined-variable


from SimpleGUICS2Pygame.simpleguics2pygame.canvas import *  # noqa  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module

if 'canvas' in dir():
    del canvas  # pylint: disable=undefined-variable

from SimpleGUICS2Pygame.simpleguics2pygame.frame import *  # noqa  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module

if 'frame' in dir():
    del frame  # pylint: disable=undefined-variable


#
# Clean
#######
if 'SimpleGUICS2Pygame' in dir():
    del SimpleGUICS2Pygame
