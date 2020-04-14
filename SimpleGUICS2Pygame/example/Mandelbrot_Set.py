#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Mandelbrot Set simple computation.

See http://en.wikipedia.org/wiki/Mandelbrot_set#Computer_drawings .

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: April 14, 2020
"""

import math

try:
    from user305_2YRLOxXzAvucSDa import codeskulptor_is, hex2  # pytype: disable=import-error  # noqa

    import simplegui  # pytype: disable=import-error

    from codeskulptor import set_timeout  # pytype: disable=import-error

    set_timeout(10)
except ImportError:
    from SimpleGUICS2Pygame.codeskulptor_lib import codeskulptor_is, hex2

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


#
# Global constants
###################
# draw FPS average (only with SimpleGUICS2Pygame)
_FPS_AVERAGE = not codeskulptor_is()

CANVAS_WIDTH = 256
CANVAS_HEIGHT = 256


#
# Global variables
###################
colors = None

grid = None

nb_iter_max = 50
nb_iter = 0

z0_real = -2.0
z0_imag = 1.5

z1_real = 1.0
z1_imag = -1.5


#
# Functions
############
def draw_and_calculate(canvas):  # pylint: disable=too-many-branches
    """
    Draw and calculate image of Mandelbrot set from grid.

    :param canvas: simplegui.Canvas
    """
    global nb_iter  # pylint: disable=global-statement

    print(nb_iter)
    nb_iter += 1

    for y, line in enumerate(grid):
        contiguous_color = None
        contiguous_x0 = 0

        for x, point in enumerate(line):
            color = point[3]
            if color is None:
                z = point[0]

                z_real2 = z[0] * z[0]
                z_imag2 = z[1] * z[1]
                z_abs2 = z_real2 + z_imag2

                if z_abs2 > 4:
                    point[3] = color = point[2] % len(colors)  # color
                else:
                    color = None
                    c = point[1]
                    point[0] = (z_real2 - z_imag2 + c[0],  # z
                                z[0] * z[1] * 2 + c[1])
                    point[2] += 1  # number of iterations

            if contiguous_color != color:
                if contiguous_color is not None:
                    contiguous_color = colors[contiguous_color]
                    if contiguous_x0 + 1 == x:
                        canvas.draw_point((contiguous_x0, y),
                                          contiguous_color)
                        canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                                          contiguous_color)
                    else:
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, y,
                                   contiguous_color)
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, CANVAS_HEIGHT - y,
                                   contiguous_color)

                contiguous_color = color
                contiguous_x0 = x

        if contiguous_color is not None:
            contiguous_color = colors[contiguous_color]
            if contiguous_x0 + 1 == len(line):
                canvas.draw_point((contiguous_x0, y),
                                  contiguous_color)
                canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                                  contiguous_color)
            else:
                draw_hline(canvas,
                           contiguous_x0, len(line) - 1, y,
                           contiguous_color)
                draw_hline(canvas,
                           contiguous_x0, len(line) - 1, CANVAS_HEIGHT - y,
                           contiguous_color)

    if nb_iter >= nb_iter_max:
        frame.set_draw_handler(draw_only)
        print('\nEnd.')

    if _FPS_AVERAGE:
        canvas.draw_text('{:.3}'.format(frame._get_fps_average()),  # noqa  # pylint: disable=protected-access
                         (5, 20), 20, 'Black')


if codeskulptor_is():
    def draw_hline(canvas, x0, x1, y, color):
        """
        Draw a horizontal line
        (point by point
        because CodeSkulptor draw_line() is problematic with line_width=1).

        :param canvas: simplegui.Canvas
        :param x0: int >= 0
        :param x1: int >= 0
        :param y: int >= 0
        :param color: str
        """
        for x in range(x0, x1 + 1):
            canvas.draw_point((x, y), color)
else:
    def draw_hline(canvas, x0, x1, y, color):
        """
        Draw a horizontal line.

        :param canvas: simplegui.Canvas
        :param x0: int >= 0
        :param x1: int >= 0
        :param y: int >= 0
        :param color: str
        """
        canvas.draw_line((x0, y), (x1, y), 1, color)


def draw_only(canvas):
    """
    Draw image of Mandelbrot set from grid.

    :param canvas: simplegui.Canvas
    """
    for y, line in enumerate(grid):
        contiguous_color = None
        contiguous_x0 = 0

        for x, point in enumerate(line):
            color = point[3]
            if contiguous_color != color:
                if contiguous_color is not None:
                    contiguous_color = colors[contiguous_color]
                    if contiguous_x0 + 1 == x:
                        canvas.draw_point((contiguous_x0, y),
                                          contiguous_color)
                        canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                                          contiguous_color)
                    else:
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, y,
                                   contiguous_color)
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, CANVAS_HEIGHT - y,
                                   contiguous_color)

                contiguous_color = color
                contiguous_x0 = x

        contiguous_color = colors[contiguous_color]
        if contiguous_x0 + 1 == len(line):
            canvas.draw_point((contiguous_x0, y),
                              contiguous_color)
            canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                              contiguous_color)
        else:
            draw_hline(canvas,
                       contiguous_x0, len(line) - 1, y,
                       contiguous_color)
            draw_hline(canvas,
                       contiguous_x0, len(line) - 1, CANVAS_HEIGHT - y,
                       contiguous_color)

    if _FPS_AVERAGE:
        canvas.draw_text('{:.3}'.format(frame._get_fps_average()),  # noqa  # pylint: disable=protected-access
                         (5, 20), 20, 'Black')


def init():
    """
    Set a grid of point information :
    [z, C, numbers of iterations, None or color number]
    """
    global colors  # pylint: disable=global-statement
    global grid  # pylint: disable=global-statement
    global nb_iter  # pylint: disable=global-statement

    print('Init.')

    assert nb_iter_max < 256, nb_iter_max

    colors = tuple(['#%s%s%s'
                    % (hex2(255 - 256 * int(math.log10(i) // nb_iter_max)),
                       hex2(255 - 256 * i // nb_iter_max),
                       hex2(255 - 256 * i // nb_iter_max))
                    for i in range(1, nb_iter_max)])

    nb_iter = 0

    coef_c_real = (z1_real - z0_real) / (CANVAS_WIDTH - 1)
    coef_c_imag = (z0_imag - z1_imag) / (CANVAS_HEIGHT - 1)

    grid = []
    for y in range(CANVAS_HEIGHT // 2 + 1):
        c_imag = z0_imag - coef_c_imag * y

        line = []
        for x in range(CANVAS_WIDTH):
            c_real = z0_real + coef_c_real * x
            line.append([(0, 0),            # z
                         (c_real, c_imag),  # C
                         0,                 # number of iterations
                         None])             # color number

        grid.append(line)

    print('\nNumber of iterations:')


#
# Main
#######
init()

frame = simplegui.create_frame('Mandelbrot Viewer',
                               CANVAS_WIDTH, CANVAS_HEIGHT, 50)

frame.add_button('Quit', frame.stop)

frame.set_draw_handler(draw_and_calculate)

frame.start()
