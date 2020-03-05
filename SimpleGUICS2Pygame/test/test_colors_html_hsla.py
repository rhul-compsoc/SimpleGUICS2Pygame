#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test colors HTML in hsla() format. (March 4, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2014, 2020 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from user38_ZmhOVHGm2lhVRhk import hsla

    import simplegui
    import codeskulptor

    SIMPLEGUICS2PYGAME = False

    codeskulptor.set_timeout(10)
except ImportError:
    from SimpleGUICS2Pygame.codeskulptor_lib import hsla

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


TEST = 'test colors HTML hsla()'

WIDTH = 362
HEIGHT = 310

state_transparency = True


def draw(canvas):
    """
    Draw (with draw_line()) range of colors
    in hsla(hue, lightness, saturation, alpha) format.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    for i in range(180):  # Format hsla(hue, lightness, saturation, alpha)
        p = int(round(i * 100.0 / 180))

        for a in range(10):
            canvas.draw_line((i * 2, 10 + a * 10),
                             ((i + 1) * 2, 10 + a * 10), 10,
                             hsla(i, p, p, (a / 10.0 if state_transparency
                                            else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 110 + a * 10),
                             ((i + 1) * 2, 110 + a * 10), 10,
                             hsla(i, 50, 50, (a / 10.0 if state_transparency
                                              else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 210 + a * 10),
                             ((i + 1) * 2, 210 + a * 10), 10,
                             hsla(0, p, 50, (a / 10.0 if state_transparency
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
