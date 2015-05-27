#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Stop example (May 27, 2015)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300


def click():
    """
    Simple handler function to the timer.
    """
    print('click')


def draw(canvas):
    """
    Draw a simple text.

    :param canvas: simplegui.Canvas
    """
    text = 'Canvas'

    font_size = 40
    text_width = frame.get_canvas_textwidth(text, font_size)

    canvas.draw_text(text,
                     ((CANVAS_WIDTH - text_width)//2,
                      CANVAS_HEIGHT//2 + font_size//4),
                     font_size, 'Green')


def stop_all():
    """
    Handler function to the Quit button.
    """
    timer.stop()
    sound.pause()
    frame.stop()


# Main
sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')
sound.play()

frame = simplegui.create_frame('Stop example', CANVAS_WIDTH, CANVAS_HEIGHT)

frame.add_button('Quit', stop_all)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000, click)
timer.start()

frame.start()
