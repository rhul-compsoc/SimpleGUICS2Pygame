#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw circles. (June 19, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except:
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



TEST = 'test circle'

WIDTH = 400
HEIGHT = 200



def draw(canvas):
    """
    Draw concentric circles.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    x = WIDTH//3
    y = HEIGHT//2

    line_width = 11

    for radius in range(1, WIDTH, 30):
        canvas.draw_circle((WIDTH - 1 - x, y), radius, line_width, 'rgba(0,255,0,.5)')
        canvas.draw_circle((WIDTH - 1 - x, y), radius, 1, 'Lime')

    for radius in range(1, WIDTH, 30):
        canvas.draw_circle((x, y), radius, line_width, 'rgba(255,0,0,.5)')
        canvas.draw_circle((x, y), radius, 1, 'Red')



# Main
frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)
frame.add_label('')
frame.add_button('Quit', lambda: frame.stop())

frame.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        frame._save_canvas_and_stop(argv[1])


frame.start()
