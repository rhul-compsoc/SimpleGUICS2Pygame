#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test input dealing in control panel. (August 18, 2015)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015 Olivier Pirson
http://www.opimedia.be/
"""


try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version
    from pygame.version import ver as pygame_version
    from SimpleGUICS2Pygame import _VERSION as GUI_VERSION

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    PYGAME_VERSION = 'Pygame ' + pygame_version
    GUI_VERSION = 'SimpleGUICS2Pygame ' + GUI_VERSION
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/
    PYGAME_VERSION = ''
    GUI_VERSION = 'simplegui'


TEST = 'test input'


input_1 = ''
input_2 = ''


def input_1_handler(text):
    """
    Simple input handler function.
    """
    global input_1

    input_1 = text
    print('|' + input_1 + '|')
    print('.' + input_2 + '.')


def input_2_handler(text):
    """
    Simple input handler function.
    """
    global input_2

    input_2 = text
    print('|' + input_1 + '|')
    print('.' + input_2 + '.')


# Main
frame = simplegui.create_frame(TEST, 0, 400, 400)

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)
frame.add_label('')
frame.add_button('Quit', frame.stop)
frame.add_label('')


# Buttons
frame.add_input('Input 1:', input_1_handler, 400)
frame.add_input('Input 2:', input_2_handler, 400)


frame.start()
