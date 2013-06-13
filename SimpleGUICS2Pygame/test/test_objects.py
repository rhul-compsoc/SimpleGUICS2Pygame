#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test __repr__() et __str__() methods of objects. (June 11, 2013)

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

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    PYGAME_VERSION = 'Pygame ' + pygame_version
    GUI_VERSION = 'SimpleGUICS2Pygame ' + simplegui._VERSION
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/
    PYGAME_VERSION = ''
    GUI_VERSION = 'simplegui'



TEST = 'test objects'

WIDTH = 400
HEIGHT = 200



def draw(canvas):
    """
    Print str representation of each SimpleGUI object.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    image = simplegui.load_image('')
    sound = simplegui.load_sound('')
    timer = simplegui.create_timer(1000, lambda: None)

    for name, o in (('button', button),
                    ('canvas', canvas),
                    ('frame',  frame),
                    ('image',  image),
                    ('input',  input),
                    ('label',  label),
                    ('sound',  sound),
                    ('timer',  timer)):
        print(name + str(type(o)) + repr(o) + str(o))

    frame.stop()




# Main
frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

frame.add_label(TEST)
frame.add_label('')
frame.add_label(PYTHON_VERSION)
frame.add_label(GUI_VERSION)
frame.add_label(PYGAME_VERSION)

label = frame.add_label('label')
button = frame.add_button('button', lambda: None)
input = frame.add_input('input', lambda: None, 50)

frame.set_draw_handler(draw)

frame.start()
