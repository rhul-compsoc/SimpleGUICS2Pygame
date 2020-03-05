#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw images. (March 5, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2015, 2016, 2020 Olivier Pirson
http://www.opimedia.be/
"""

import math

try:
    from user33_Bhc7VzXKbXGVQV1 import FPS
    from user40_nMs7JxzimyImAv2 import Loader

    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False


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


TEST = 'test image'

WIDTH = 360
HEIGHT = 270


def draw(canvas):
    """
    Draw a ship image several times.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    canvas.draw_line((0, 0), (WIDTH - 1, HEIGHT - 1), 1, 'Blue')
    canvas.draw_line((0, HEIGHT - 1), (WIDTH, 0), 1, 'Blue')

    img = loader.get_image('double_ship')

    # The complete image with ship twice
    canvas.draw_image(img,
                      (img.get_width() / 2, img.get_height() / 2),
                      (img.get_width(), img.get_height()),
                      (img.get_width() / 2, img.get_height() / 2),
                      (img.get_width(), img.get_height()))

    # The ship without thrust
    canvas.draw_image(img,
                      (img.get_width() / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() / 4, img.get_height() * 3 / 2),
                      (img.get_width() / 2, img.get_height()))
    # The ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 3 / 4, img.get_height() * 3 / 2),
                      (img.get_width() / 2, img.get_height()))

    # The rotated ship without thrust
    canvas.draw_image(img,
                      (img.get_width() / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() / 4, img.get_height() * 5 / 2),
                      (img.get_width() / 2, img.get_height()),
                      -math.pi / 2)
    # The rotated ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 3 / 4, img.get_height() * 5 / 2),
                      (img.get_width() / 2, img.get_height()),
                      -math.pi / 2)

    # The big ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 6 / 4, img.get_height() * 3 / 2),
                      (img.get_width(), img.get_height() * 4))

    # The little ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 15 / 8, img.get_height() / 2),
                      (img.get_width() / 4, img.get_height()))

    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 7 / 4, img.get_height() * 11 / 4),
                      (img.get_width() / 2, img.get_height() / 2))

    canvas.draw_image(logo,
                      (32, 32), (64, 64),
                      (WIDTH / 2, HEIGHT / 2), (64, 64))

    # Update and draw FPS (if started)
    fps.draw_fct(canvas)


def fps_on_off():
    """
    Active or inactive the calculation and drawing of FPS.
    """
    if fps.is_started():
        fps.stop()
        button_fps.set_text('FPS on')
    else:
        fps.start()
        button_fps.set_text('FPS off')


# Main
frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

fps = FPS()

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)
frame.add_label('')
button_fps = frame.add_button('FPS on', fps_on_off)
frame.add_label('')
frame.add_button('Quit', frame.stop)


def init():
    """
    Init after image loaded.
    """
    if not SIMPLEGUICS2PYGAME:
        global logo

        logo = loader.get_image('logo')

    frame.set_draw_handler(draw)

    if SIMPLEGUICS2PYGAME:
        from sys import argv

        if len(argv) == 2:
            frame._save_canvas_and_stop(argv[1])

loader = Loader(frame, WIDTH, init)
loader.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png',  # noqa
                 'double_ship')
if not SIMPLEGUICS2PYGAME:
    loader.add_image('https://simpleguics2pygame.readthedocs.io/en/latest/_images/SimpleGUICS2Pygame_64x64_t.png',  # noqa
                     'logo')
loader.load()

loader.wait_loaded()

if SIMPLEGUICS2PYGAME:
    logo = simplegui._load_local_image(
        '../_img/SimpleGUICS2Pygame_64x64_t.png')

frame.start()
if SIMPLEGUICS2PYGAME and frame._print_stats_cache:
    loader.print_stats_cache()
