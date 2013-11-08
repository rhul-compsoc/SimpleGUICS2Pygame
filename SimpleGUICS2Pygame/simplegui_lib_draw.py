# -*- coding: latin-1 -*-

"""
simplegui_lib_draw (November 8, 2013)

Draw functions to help
in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""


#
# Functions
############
def draw_rect(canvas, pos, size, line_width, line_color, fill_color=None):
    """
    Draw a rectangle.

    :param canvas: simplegui.Canvas
    :param pos: (int or float, int or float) or [int or float, int or float]
    :param size: (int or float, int or float) or [int or float, int or float]
    :param line_width: int >= 0
    :param line_color: str
    :param fill_color: str
    """
    assert isinstance(pos, tuple) or isinstance(pos, list), type(pos)
    assert len(pos) == 2, len(pos)
    assert isinstance(pos[0], int) or isinstance(pos[0], float), type(pos[0])
    assert isinstance(pos[1], int) or isinstance(pos[1], float), type(pos[1])

    assert isinstance(size, tuple) or isinstance(size, list), type(size)
    assert len(size) == 2, len(size)
    assert isinstance(size[0], int) or isinstance(size[0], float), \
        type(size[0])
    assert isinstance(size[1], int) or isinstance(size[1], float), \
        type(size[1])

    assert isinstance(line_width, int) or isinstance(line_width, float), \
        type(line_width)
    assert line_width >= 0, line_width
    assert isinstance(line_color, str), type(str)
    assert (fill_color is None) or isinstance(fill_color, str), type(str)

    x0 = pos[0]
    y0 = pos[1]

    width = size[0] - 1
    height = size[1] - 1

    canvas.draw_polygon(((x0, y0),
                         (x0 + width, y0),
                         (x0 + width, y0 + height),
                         (x0, y0 + height)),
                        line_width, line_color, fill_color)


def draw_text_side(frame, canvas,
                   text, point,
                   font_size, font_color,
                   font_face='serif',
                   font_size_coef=3.0/4,
                   rectangle_color=None, rectangle_fill_color=None,
                   side_x=-1, side_y=1):
    """
    Draw the `text` string at the position `point`.

    See `simplegui.draw_text()`.

    If `rectangle_color` != `None`
    then draw a rectangle around the text.

    If `rectangle_fill_color` != `None`
    then draw a filled rectangle under the text.

    | If `side_x`
    |   < 0 then `point[0]` is the left of the text,
    |  == 0 then `point[0]` is the center of the text,
    |   > 0 then `point[0]` is the right of the text.

    | If `side_y`
    |   < 0 then `point[1]` is the top of the text,
    |  == 0 then `point[1]` is the center of the text,
    |   > 0 then `point[1]` is the bottom of the text.

    :param text: str
    :param point: (int or float, int or float) or [int or float, int or float]
    :param font_size: (int or float) >= 0
    :param font_color: str
    :param font_face: str == 'monospace', 'sans-serif', 'serif'
    :param rectangle_color: None or str
    :param rectangle_fill_color: None or str
    :param side_x: int or float
    :param side_y: int or float
    :param font_size_coef: int or float
    """
    assert isinstance(text, str), type(text)

    assert isinstance(point, tuple) or isinstance(point, list), type(point)
    assert len(point) == 2, len(point)
    assert isinstance(point[0], int) or isinstance(point[0], float), \
        type(point[0])
    assert isinstance(point[1], int) or isinstance(point[1], float), \
        type(point[1])

    assert isinstance(font_size, int) or isinstance(font_size, float), \
        type(font_size)
    assert font_size >= 0, font_size

    assert isinstance(font_color, str), type(font_color)
    assert isinstance(font_face, str), type(font_face)

    assert (rectangle_color is None) or isinstance(rectangle_color, str), \
        type(rectangle_color)
    assert ((rectangle_fill_color is None)
            or isinstance(rectangle_fill_color, str)), \
        type(rectangle_fill_color)

    assert isinstance(side_x, int) or isinstance(side_x, float), type(side_x)
    assert isinstance(side_y, int) or isinstance(side_y, float), type(side_y)
    assert (isinstance(font_size_coef, int)
            or isinstance(font_size_coef, float)), type(font_size_coef)

    text_width = (frame.get_canvas_textwidth(text, font_size)
                  if font_face is None
                  else frame.get_canvas_textwidth(text, font_size, font_face))

    text_height = font_size*font_size_coef

    if side_x < 0:
        x = point[0]
    elif side_x == 0:
        x = point[0] - text_width/2.0
    else:
        x = point[0] - text_width

    if side_y < 0:
        y = point[1] + text_height
    elif side_y == 0:
        y = point[1] + text_height/2.0
    else:
        y = point[1]

    if rectangle_color is not None:
        draw_rect(canvas, (x, y), (text_width, -text_height),
                  1, rectangle_color, rectangle_fill_color)
    elif rectangle_fill_color is not None:
        draw_rect(canvas, (x, y), (text_width, -text_height),
                  1, rectangle_fill_color, rectangle_fill_color)

    canvas.draw_text(text, (x, y), font_size, font_color, font_face)
