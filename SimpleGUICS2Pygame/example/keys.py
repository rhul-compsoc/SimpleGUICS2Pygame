#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Example of simplegui_lib_keys.Keys use.

Documentation:
https://simpleguics2pygame.readthedocs.io/en/latest/simplegui_lib_keys.html

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 28, 2020
"""

try:
    import simplegui

    from user305_CGRDFZgmaZOL2YB import Keys
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    from SimpleGUICS2Pygame.simplegui_lib_keys import Keys


def draw(canvas):
    """
    Draw pressed keys.

    :param canvas: simplegui.Canvas
    """
    for i, key_str in enumerate(('space', 'left', 'up', 'right', 'down')):
        canvas.draw_text(key_str,
                         (5 + 120 * i, 30),
                         30, ('White' if KEYS.is_pressed_key_map(key_str)
                              else 'Gray'))
    for i in range(10):  # 0..9
        key_str = chr(48 + i)
        canvas.draw_text(key_str,
                         (5 + 25 * i, 60),
                         30, ('White' if KEYS.is_pressed_key_map(key_str)
                              else 'Gray'))
    for i in range(26):  # a..z
        key_str = chr(97 + i)
        canvas.draw_text(key_str,
                         (5 + 25 * i, 90),
                         30, ('White' if KEYS.is_pressed_key_map(key_str)
                              else 'Gray'))

    pressed_keys = KEYS.pressed_keys()
    if pressed_keys:
        pressed_keys.sort()
        canvas.draw_text('Pressed keys code: ' +
                         ', '.join([str(key_code)
                                    for key_code in pressed_keys]),
                         (5, 140),
                         30, 'White')


# Functions to associate with specified key events.
def deal_down_space(key_code):
    """
    :param key_code: int
    """
    print('deal_down_space() function: %i' % key_code)


def deal_down_x(key_code):
    """
    :param key_code: int
    """
    print('deal_down_x() function: %i' % key_code)


def deal_up_space(key_code):
    """
    :param key_code: int
    """
    print('deal_up_space() function: %i' % key_code)


def deal_up_y(key_code):
    """
    :param key_code: int
    """
    print('deal_up_y() function: %i' % key_code)


FRAME = simplegui.create_frame('keys', 650, 160, 150)

FRAME.add_button('Quit', FRAME.stop)

# Init an empty keys handler
KEYS = Keys(FRAME)

# Associate funtions to key down event of specified keys
KEYS.set_keydown_fct(simplegui.KEY_MAP['x'], deal_down_x)
KEYS.set_keydown_fct_key_map('space', deal_down_space)

# Associate functions to key up event of specified keys
KEYS.set_keyup_fct(simplegui.KEY_MAP['y'], deal_up_y)
KEYS.set_keyup_fct_key_map('space', deal_up_space)

FRAME.set_draw_handler(draw)

# Active key down and key up handlers
KEYS.active_handlers()

FRAME.start()
