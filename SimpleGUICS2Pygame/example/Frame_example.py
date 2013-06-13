#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Frame example (June 13, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300



def draw(canvas):
    text = 'Canvas'

    font_size = 40
    text_width = frame.get_canvas_textwidth(text, font_size)

    canvas.draw_text(text,
                     ((CANVAS_WIDTH - text_width)/2,
                      CANVAS_HEIGHT/2 + font_size/4),
                     font_size, 'Green')



# Main
frame = simplegui.create_frame('Title', CANVAS_WIDTH, CANVAS_HEIGHT)

frame.add_label('Control Panel')

frame.add_label('')
frame.add_button('Quit', lambda: frame.stop())

frame.set_draw_handler(draw)

frame.start()
