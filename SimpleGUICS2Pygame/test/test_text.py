#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw text. (June 19, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from user16_5OTl5W5yQFVDqqv import draw_rect, draw_text_side

    import simplegui

    SIMPLEGUICS2PYGAME = False
except:
    from SimpleGUICS2Pygame.simplegui_lib import draw_rect, draw_text_side

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



TEST = 'test text'

WIDTH = 800
HEIGHT = 300



def draw(canvas):
    """
    Draw handler.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    for x in range(0, WIDTH, 20):
        canvas.draw_line((x, 0), (x, HEIGHT - 1), 1, 'Silver')

    for y in range(0, HEIGHT, 20):
        canvas.draw_line((0, y), (WIDTH - 1, y), 1, 'Silver')

    size = 80

    text = 'Text'
    y = 120

    canvas.draw_text(text, (  0, y), size, 'rgba(255,255,255,.5)')
    canvas.draw_text(text, (200, y), size, 'White', 'serif')
    canvas.draw_text(text, (400, y), size, 'White', 'sans-serif')
    canvas.draw_text(text, (600, y), size, 'White', 'monospace')

    text = 'Text'
    y = 240

    canvas.draw_text(text, (  0, y), size, 'rgba(255,255,255,.5)')
    canvas.draw_text(text, (200, y), size, 'White', 'serif')
    canvas.draw_text(text, (400, y), size, 'White', 'sans-serif')
    canvas.draw_text(text, (600, y), size, 'White', 'monospace')

    size = 40

    draw_text_side(frame, canvas,
                   'Left top', (0, 0), size, 'Red',
                   rectangle_color = 'Orange',
                   side_x = -1, side_y = -1)

    draw_text_side(frame, canvas,
                   'Left bottom', (0, HEIGHT - 1), size, 'Red',
                   rectangle_color = 'Orange',
                   side_x = -1, side_y = 1)

    draw_text_side(frame, canvas,
                   'Right top', (WIDTH - 1, 0), size, 'Red',
                   rectangle_color = 'Orange',
                   side_x = 1, side_y = -1)

    draw_text_side(frame, canvas,
                   'Right bottom', (WIDTH - 1, HEIGHT - 1), size, 'Red',
                   rectangle_color = 'Orange',
                   side_x = 1, side_y = 1)

    draw_text_side(frame, canvas,
                   'Center', (WIDTH/2, HEIGHT/2), size, 'Red',
                   rectangle_color = 'Orange', rectangle_fill_color = 'Yellow',
                   side_x = 0, side_y = 0)



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
