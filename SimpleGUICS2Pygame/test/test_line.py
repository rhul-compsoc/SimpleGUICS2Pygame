#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw lines.

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


TEST = 'test line'

WIDTH = 400
HEIGHT = 200


STATE_COLORS = True
STATE_DIRECTION = True


def draw(canvas):
    """
    Draw several lines.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    canvas.draw_line((0, 0), (WIDTH - 1, HEIGHT - 1), 1, 'Blue')
    canvas.draw_line((0, HEIGHT - 1), (WIDTH, 0), 1, 'Blue')

    if STATE_DIRECTION:
        for i in range(0, HEIGHT + 1, 20):
            canvas.draw_line((i, i), (WIDTH - i / 2, i), 9,
                             ('White' if STATE_COLORS
                              else 'Red'))
            canvas.draw_line((i, i), (WIDTH - i / 2, i), 3,
                             ('Red' if STATE_COLORS
                              else 'White'))
    else:
        for i in range(0, WIDTH + 1, 20):
            canvas.draw_line((i, i), (i, HEIGHT - i / 2), 9,
                             ('White' if STATE_COLORS
                              else 'Red'))
            canvas.draw_line((i, i), (i, HEIGHT - i / 2), 3,
                             ('Red' if STATE_COLORS
                              else 'White'))


def switch_colors():
    """
    Switch red and white.
    """
    global STATE_COLORS  # pylint: disable=global-statement

    STATE_COLORS = not STATE_COLORS


def switch_direction():
    """
    Switch horizontal and vertical.
    """
    global STATE_DIRECTION  # pylint: disable=global-statement

    STATE_DIRECTION = not STATE_DIRECTION


#
# Main
######
def main():
    """Create and start frame."""
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
            frame._save_canvas_and_stop(argv[1])  # noqa  # pylint: disable=protected-access

    frame.start()

if __name__ == '__main__':
    main()
