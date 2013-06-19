#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test colors HTML in rgba() format. (June 19, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from user16_WPKkkxSR6z6xQh1 import rgba

    import simplegui

    SIMPLEGUICS2PYGAME = False
except:
    from SimpleGUICS2Pygame.codeskulptor_lib import rgba

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True


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



def draw(canvas):
    """
    Draw (with draw_line()) range of colors in rbga(red, blue, green, alpha) format.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    for i in range(256):  # Format rbga(red, blue, green, alpha)
        for a in range(10):
            canvas.draw_line((i*2, 10 + a*10), ((i + 1)*2, 10 + a*10), 10, rgba(i, i, i, a/9.0))

        for a in range(10):
            canvas.draw_line((i*2, 110 + a*10), ((i + 1)*2, 110 + a*10), 10, rgba(i, 0, 0, a/9.0))

        for a in range(10):
            canvas.draw_line((i*2, 210 + a*10), ((i + 1)*2, 210 + a*10), 10, rgba(0, i, 0, a/9.0))

        for a in range(10):
            canvas.draw_line((i*2, 310 + a*10), ((i + 1)*2, 310 + a*10), 10, rgba(0, 0, i, a/9.0))



# Main
frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)
frame.add_label('')
frame.add_button('Quit', frame.stop)

frame.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        frame._save_canvas_and_stop(argv[1])


frame.start()
