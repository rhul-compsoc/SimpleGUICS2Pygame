#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw lines. (June 19, 2013)

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



TEST = 'test line'

WIDTH = 400
HEIGHT = 200



state_colors = True
state_direction = True



def draw(canvas):
    """
    Draw several lines.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    canvas.draw_line((0, 0), (WIDTH - 1, HEIGHT - 1), 1, 'Blue')
    canvas.draw_line((0, HEIGHT - 1), (WIDTH, 0), 1, 'Blue')

    if state_direction:
        for i in range(0, HEIGHT + 1, 20):
            canvas.draw_line((i, i), (WIDTH - i/2, i), 9, ('White' if state_colors
                                                           else 'Red'))
            canvas.draw_line((i, i), (WIDTH - i/2, i), 3, ('Red' if state_colors
                                                           else 'White'))
    else:
        for i in range(0, WIDTH + 1, 20):
            canvas.draw_line((i, i), (i, HEIGHT - i/2), 9, ('White' if state_colors
                                                            else 'Red'))
            canvas.draw_line((i, i), (i, HEIGHT - i/2), 3, ('Red' if state_colors
                                                            else 'White'))


def switch_colors():
    """
    Switch red and white.
    """
    global state_colors

    state_colors = not state_colors


def switch_direction():
    """
    Switch horizontal and vertical.
    """
    global state_direction

    state_direction = not state_direction



# Main
frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)
frame.add_label('')
frame.add_button('Switch colors', switch_colors)
frame.add_button('Switch direction', switch_direction)
frame.add_label('')
frame.add_button('Quit', frame.stop)

frame.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        frame._save_canvas_and_stop(argv[1])


frame.start()
