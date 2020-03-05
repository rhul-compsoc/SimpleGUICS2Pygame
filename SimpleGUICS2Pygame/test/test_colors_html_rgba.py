#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test colors HTML in rgba() format. (March 4, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2020 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from user38_ZmhOVHGm2lhVRhk import rgba

    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    from SimpleGUICS2Pygame.codeskulptor_lib import rgba

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


TEST = 'test colors HTML rgba()'

WIDTH = 512
HEIGHT = 410

state_transparency = True


def draw(canvas):
    """
    Draw (with draw_line()) range of colors
    in rgba(red, blue, green, alpha) format.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    for i in range(256):  # Format rgba(red, blue, green, alpha)
        for a in range(10):
            canvas.draw_line((i * 2, 10 + a * 10),
                             ((i + 1) * 2, 10 + a * 10), 10,
                             rgba(i, i, i, (a / 10.0 if state_transparency
                                            else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 110 + a * 10),
                             ((i + 1) * 2, 110 + a * 10), 10,
                             rgba(i, 0, 0, (a / 10.0 if state_transparency
                                            else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 210 + a * 10),
                             ((i + 1) * 2, 210 + a * 10), 10,
                             rgba(0, i, 0, (a / 10.0 if state_transparency
                                            else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 310 + a * 10),
                             ((i + 1) * 2, 310 + a * 10), 10,
                             rgba(0, 0, i, (a / 10.0 if state_transparency
                                            else 1)))


def switch_transparency():
    """
    Switch between transparency mode and opaque mode.
    """
    global state_transparency

    state_transparency = not state_transparency


# Main
frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)
frame.add_label('')
frame.add_button('Switch transparency', switch_transparency)
frame.add_label('')
frame.add_button('Quit', frame.stop)

frame.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        frame._save_canvas_and_stop(argv[1])


frame.start()
