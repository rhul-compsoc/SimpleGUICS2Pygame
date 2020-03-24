#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test colors constants.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 24, 2020
"""

try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version
    from pygame.version import ver as pygame_version
    from SimpleGUICS2Pygame import _VERSION as GUI_VERSION  # noqa  # pylint: disable=ungrouped-imports

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    PYGAME_VERSION = 'Pygame ' + pygame_version
    GUI_VERSION = 'SimpleGUICS2Pygame ' + GUI_VERSION
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/ or https://py3.codeskulptor.org/  # noqa
    PYGAME_VERSION = ''
    GUI_VERSION = 'simplegui'


TEST = 'test colors constants'

WIDTH = 640
HEIGHT = 200


def draw(canvas):
    """
    Draw boxes in each color constant.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    width = WIDTH // 8
    height = HEIGHT // 3

    size = 30

    for j, line in enumerate((('Aqua', 'Black', 'Blue', 'Fuchsia',
                               'Gray', 'Green', 'Lime', 'Maroon'),
                              ('Navy', 'Olive', 'Purple', 'Red',
                               'Silver', 'Teal', 'White', 'Yellow'),
                              ('Orange', 'Cyan', 'Magenta'))):
        for i, color in enumerate(line):
            canvas.draw_line((i * width, height // 2 - 1 + j * height),
                             ((i + 1) * width, height // 2 - 1 + j * height),
                             height, color)

            length = FRAME.get_canvas_textwidth(color, size)
            canvas.draw_text(color,
                             (i * width + (width - length) // 2,
                              (j * height + (height - size) // 2 +
                               size * 3 // 4)),
                             size, 'White')


# Main
FRAME = simplegui.create_frame(TEST, WIDTH, HEIGHT)

FRAME.add_label(TEST)
FRAME.add_label('')
FRAME.add_label(PYTHON_VERSION)
FRAME.add_label(GUI_VERSION)
FRAME.add_label(PYGAME_VERSION)
FRAME.add_label('')
FRAME.add_button('Quit', FRAME.stop)

FRAME.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        FRAME._save_canvas_and_stop(argv[1])  # noqa  # pylint: disable=protected-access


FRAME.start()
