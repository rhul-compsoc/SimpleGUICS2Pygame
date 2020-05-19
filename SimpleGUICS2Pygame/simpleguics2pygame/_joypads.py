# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/_joypads.

Dealing of joypads.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 19, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


import os.path
import sys


__all__ = tuple()  # type: tuple


from SimpleGUICS2Pygame.simpleguics2pygame._pygame_init import _PYGAME_AVAILABLE  # pylint: disable=no-name-in-module  # noqa
if _PYGAME_AVAILABLE:
    import pygame
    import pygame.joystick

    pygame.joystick.init()


#
# Private global constants
##########################
if not os.path.basename(sys.argv[0]).startswith('sphinx-build'):
    __PYGAME_JOYPADS = (tuple(pygame.joystick.Joystick(i)
                              for i in range(pygame.joystick.get_count()))
                        if _PYGAME_AVAILABLE
                        else tuple())
else:
    __PYGAME_JOYPADS = tuple()
    """
    Tuple of all Pygame joypads found.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """


# Initialize each joypad
tuple(joypad.init() for joypad in __PYGAME_JOYPADS)


_joypad_nb = len(__PYGAME_JOYPADS)  # pylint: disable=invalid-name
"""
Number of available joypads.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""
