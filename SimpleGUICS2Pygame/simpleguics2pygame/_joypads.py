# -*- coding: latin-1 -*-

"""
simpleguics2pygame/_joypads

Dealing of joypads.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 29, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = []


from SimpleGUICS2Pygame.simpleguics2pygame._pygame_init import _PYGAME_AVAILABLE  # noqa  # pylint: disable=no-name-in-module
if _PYGAME_AVAILABLE:
    import pygame
    import pygame.joystick

    pygame.joystick.init()


#
# Private global constants
##########################
if _PYGAME_AVAILABLE:
    __PYGAME_JOYPADS = tuple(pygame.joystick.Joystick(i)
                             for i in range(pygame.joystick.get_count()))
    """
    Tuple of all Pygame joypads found.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """
else:
    __PYGAME_JOYPADS = tuple()

tuple(joypad.init() for joypad in __PYGAME_JOYPADS)


_joypad_nb = len(__PYGAME_JOYPADS)  # pylint: disable=invalid-name
"""
Number of available joypads.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""
