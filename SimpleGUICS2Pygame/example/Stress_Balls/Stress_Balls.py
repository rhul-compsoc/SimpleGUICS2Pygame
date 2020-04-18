#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Stress Ball: display many "balls" and calculate FPS (Frame Per Second).

On Safari: exception failed!

Inspired by "Classy Balls" of Bill:
https://py3.codeskulptor.org/#user14_iNYvGMFtb8poj1S.py

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: April 18, 2020
"""

import sys

try:
    import simplegui  # pytype: disable=import-error
    # import simpleguitk as simplegui  # SimpleGUITk https://pypi.org/project/SimpleGUITk  # noqa
    import simpleplot  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore
    import SimpleGUICS2Pygame.simpleplot as simpleplot  # type: ignore

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access


# ### Config >>>
MAX_NB_SECONDS = 30  # number of seconds before next step

REVERSE = False  # reverse LIST_NB_SHAPES if true
TRANSPARENCY = False  # start with transparency if True

PLOT = True  # plot results at the end if True

# Use Frame._get_fps_average() (only with SimpleGUICS2Pygame)
_FPS_AVERAGE = False

# Number of shapes of each step
LIST_NB_SHAPES = [1, 10, 20, 30, 40, 50, 75,
                  100, 200, 300, 400, 500, 750,
                  1000, 1250, 1500, 1750, 2000]
# ### <<< config

FONT_SIZE = 40

WIDTH = 599
HEIGHT = 407

RGB_COLORS = ((0, 0, 128),
              (0, 0, 255),
              (0, 128, 0),
              (0, 128, 128),
              (0, 255, 0),
              (0, 255, 255),
              (128, 0, 0),
              (128, 0, 128),
              (128, 128, 0),
              (128, 128, 128),
              (192, 192, 192),
              (255, 0, 0),
              (255, 0, 255),
              (255, 165, 0),
              (255, 255, 0),
              (255, 255, 255))


RESULTS = {}  # type: ignore

FPS = None
FRAME = None
FREEZED = None
NB_SHAPES = None
NB_FRAMES_DRAWED = None
NB_SECONDS = None
SHAPES = None
TIMER = None
TO_NEXT_STEP = None


class Shape:  # pylint: disable=too-many-instance-attributes
    """Shape (ball, disc, square) with its properties."""

    def __init__(self, center, radius,  # pylint: disable=too-many-arguments
                 color, fill_color, velocity, shape):
        """
        Initialize this object.

        :param center:
        :param radius:
        :param color:
        :param fill_color:
        :param veloctiy:
        :param shape:
        """
        self.center_x = center[0]
        self.center_y = center[1]

        self.radius = radius

        self.color_rgba = color
        self.color = rgba_to_str(color)

        self.fill_color_rgba = fill_color
        self.fill_color = rgba_to_str(fill_color)

        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]

        self.velocity_x_save = 0
        self.velocity_y_save = 0

        self.draw = (self.draw_circle,
                     self.draw_disc,
                     self.draw_disc_border,
                     self.draw_square,
                     self.draw_squarefill,
                     self.draw_squarefill_border)[shape]

    def draw_circle(self, canvas):
        """
        Draw a circle.

        :param canvas:
        """
        canvas.draw_circle((self.center_x, self.center_y),
                           self.radius, 2, self.color)

    def draw_disc(self, canvas):
        """
        Draw a disc.

        :param canvas:
        """
        canvas.draw_circle((self.center_x, self.center_y),
                           self.radius, 1, self.color, self.color)

    def draw_disc_border(self, canvas):
        """
        Draw a disc with a border.

        :param canvas:
        """
        canvas.draw_circle((self.center_x, self.center_y),
                           self.radius, 2, self.color, self.fill_color)

    def draw_square(self, canvas):
        """
        Draw an empty square.

        :param canvas:
        """
        canvas.draw_polygon(((self.center_x - self.radius,
                              self.center_y - self.radius),
                             (self.center_x + self.radius,
                              self.center_y - self.radius),
                             (self.center_x + self.radius,
                              self.center_y + self.radius),
                             (self.center_x - self.radius,
                              self.center_y + self.radius)),
                            2, self.color)

    def draw_squarefill(self, canvas):
        """
        Draw a filled square.

        :param canvas:
        """
        canvas.draw_polygon(((self.center_x - self.radius,
                              self.center_y - self.radius),
                             (self.center_x + self.radius,
                              self.center_y - self.radius),
                             (self.center_x + self.radius,
                              self.center_y + self.radius),
                             (self.center_x - self.radius,
                              self.center_y + self.radius)),
                            1, self.color, self.color)

    def draw_squarefill_border(self, canvas):
        """
        Draw a filled square with a border.

        :param canvas:
        """
        canvas.draw_polygon(((self.center_x - self.radius,
                              self.center_y - self.radius),
                             (self.center_x + self.radius,
                              self.center_y - self.radius),
                             (self.center_x + self.radius,
                              self.center_y + self.radius),
                             (self.center_x - self.radius,
                              self.center_y + self.radius)),
                            2, self.color, self.fill_color)

    def freeze_off(self):
        """Unfreeze by restore velocity."""
        self.velocity_x = self.velocity_x_save
        self.velocity_y = self.velocity_y_save

        del self.velocity_x_save
        del self.velocity_y_save

    def freeze_on(self):
        """Freeze by setting velocity to 0."""
        self.velocity_x_save = self.velocity_x
        self.velocity_y_save = self.velocity_y

        self.velocity_x = 0
        self.velocity_y = 0

    def revert(self):
        """Revert velocity."""
        if FREEZED:
            self.velocity_x_save = -self.velocity_x_save
            self.velocity_y_save = -self.velocity_y_save
        else:
            self.velocity_x = -self.velocity_x
            self.velocity_y = -self.velocity_y

    def transparency_reset(self):
        """Reset all colors after switching transparency mode."""
        self.color = rgba_to_str(self.color_rgba)
        self.fill_color = rgba_to_str(self.fill_color_rgba)

    def move(self):
        """Update position."""
        self.center_x += self.velocity_x

        if self.center_x <= self.radius:
            self.velocity_x = abs(self.velocity_x)
        elif self.center_x >= WIDTH - 1 - self.radius:
            self.velocity_x = -abs(self.velocity_x)

        self.center_y += self.velocity_y

        if self.center_y <= self.radius:
            self.velocity_y = abs(self.velocity_y)
        elif self.center_y > HEIGHT - 1 - self.radius:
            self.velocity_y = -abs(self.velocity_y)


# Functions
def dict_to_ordered_list(d):
    """
    :param d: dictionary

    :return: ordered list of keys from dictionary d
    """
    seq = list(d.keys())
    seq.sort()

    return [(NB_SHAPES, d[NB_SHAPES])
            for NB_SHAPES in seq]


def flush():
    """With SimpleGUICS2Pygame flush the standard output, else do nothing."""
    if SIMPLEGUICS2PYGAME:
        sys.stdout.flush()


def init():
    """Init list of shapes, corresponding to the current step."""
    global FPS  # pylint: disable=global-statement
    global FREEZED  # pylint: disable=global-statement
    global NB_SHAPES  # pylint: disable=global-statement
    global NB_FRAMES_DRAWED  # pylint: disable=global-statement
    global NB_SECONDS  # pylint: disable=global-statement
    global SHAPES  # pylint: disable=global-statement
    global TO_NEXT_STEP  # pylint: disable=global-statement

    if len(LIST_NB_SHAPES) == 0:
        TIMER.stop()  # type: ignore

        final_result = dict_to_ordered_list(RESULTS)

        print('Results: {' + ', '
              .join(['%d: %d' % result for result in final_result]) + '}')

        try:
            FRAME.stop()
        except Exception as e:  # pylint: disable=broad-except
            # To avoid failed when run with simpleguitk
            print('FRAME.stop():' + str(e))

        if PLOT:
            try:
                simpleplot.plot_lines('Stress Balls', 800, 650,
                                      '# balls', 'FPS',
                                      (final_result, ), True)
                if SIMPLEGUICS2PYGAME:
                    simpleplot._block()  # pylint: disable=protected-access
            except Exception as e:  # pylint: disable=broad-except
                # To avoid fail if no simpleplot
                print('simpleplot.plot_lines():' + str(e))

        flush()

        return

    if LIST_NB_SHAPES:
        NB_SHAPES = LIST_NB_SHAPES.pop(0)

    FPS = 0
    FREEZED = False
    NB_FRAMES_DRAWED = 0
    NB_SECONDS = 0
    TO_NEXT_STEP = False

    SHAPES = tuple([Shape([47 + n % (WIDTH - 100),
                           47 + n % (HEIGHT - 100)],  # position
                          19 + n % 11,  # radius
                          n_to_rgba((n + 1) % len(RGB_COLORS),
                                    .2 + float(n % 13) / 15),  # color of border  # noqa
                          n_to_rgba((n + 2) % len(RGB_COLORS),
                                    .2 + float((n + 3) % 14) / 17),  # fill color  # noqa
                          [3 + n % 7, 2 + n % 5],  # velocity
                          (n + 2) % 6)  # shape
                    for n in range(NB_SHAPES)])


def n_to_rgba(n, alpha):
    """:return: RGB tuple with alpha"""
    n = RGB_COLORS[n]

    return (n[0], n[1], n[2], alpha)


def rgba_to_str(rgba):
    """
    :param rgba: RGB tuple with alpha

    :return: color in correct Pygame string, with transparency or not
    """
    # %f failed on CodeSkulptor
    return ('rgba(%d, %d, %d, %s)' % rgba if TRANSPARENCY
            else '#%02x%02x%02x' % rgba[:3])


# Handler
def freeze_on_off():
    """Switch freeze mode."""
    global FREEZED  # pylint: disable=global-statement

    if FREEZED:
        for shape in SHAPES:
            shape.freeze_off()
    else:
        for shape in SHAPES:
            shape.freeze_on()

    FREEZED = not FREEZED


def draw(canvas):
    """
    Display all shapes in frame.

    :param canvas:
    """
    global NB_FRAMES_DRAWED  # pylint: disable=global-statement

    for shape in SHAPES:
        shape.draw(canvas)
        shape.move()

    NB_FRAMES_DRAWED += 1

    s = '#%d | %d FPS' % (NB_SHAPES,
                          (int(round(FRAME._get_fps_average())) if _FPS_AVERAGE  # noqa  # pylint: disable=protected-access
                           else FPS))
    canvas.draw_text(s, (12, 13 + FONT_SIZE * 3 // 4), FONT_SIZE, 'Gray')
    canvas.draw_text(s, (10, 10 + FONT_SIZE * 3 // 4), FONT_SIZE, 'White')

    s = '%ds' % (MAX_NB_SECONDS - NB_SECONDS)
    x = WIDTH - 11 - FRAME.get_canvas_textwidth(s, FONT_SIZE)
    canvas.draw_text(s, (x - 2, 13 + FONT_SIZE * 3 // 4), FONT_SIZE, 'Gray')
    canvas.draw_text(s, (x, 10 + FONT_SIZE * 3 // 4), FONT_SIZE, 'White')


def next_step():
    """Set variable to increment step during next draw."""
    global TO_NEXT_STEP  # pylint: disable=global-statement

    TO_NEXT_STEP = True


def print_fps():
    """Dislay FPS in frame."""
    global FPS  # pylint: disable=global-statement
    global NB_SECONDS  # pylint: disable=global-statement

    NB_SECONDS += 1

    FPS = (FRAME._get_fps_average() if _FPS_AVERAGE  # noqa  # pylint: disable=protected-access
           else int(round(float(NB_FRAMES_DRAWED) / NB_SECONDS)))

    if (NB_SECONDS > MAX_NB_SECONDS) or TO_NEXT_STEP:
        print('%d | %d' % (NB_SHAPES, FPS))
        flush()
        RESULTS[NB_SHAPES] = FPS

        init()


def revert():
    """Revert list of shapes."""
    for shape in SHAPES:
        shape.revert()


def stop():
    """Stop timer and frame."""
    TIMER.stop()  # type: ignore
    try:
        FRAME.stop()
    except Exception as e:  # pylint: disable=broad-except
        # To avoid failed when run with simpleguitk
        print('FRAME.stop():' + str(e))


def transparency_on_off():
    """Switch transparency mode."""
    global TRANSPARENCY  # pylint: disable=global-statement

    TRANSPARENCY = not TRANSPARENCY

    for shape in SHAPES:
        shape.transparency_reset()


#
# Main
######
def main():
    """Get command line arguments, run and print results."""
    global FRAME  # pylint: disable=global-statement
    global PLOT  # pylint: disable=global-statement
    global REVERSE  # pylint: disable=global-statement
    global TIMER  # pylint: disable=global-statement
    global TRANSPARENCY  # pylint: disable=global-statement

    for arg in sys.argv[1:]:
        if arg == '--no-plot':
            PLOT = False
        elif arg == '--reverse':
            REVERSE = True
        elif arg == '--transparency':
            TRANSPARENCY = True
        else:
            print('Unknow command line argument "%s"!' % arg)

    if REVERSE:
        LIST_NB_SHAPES.reverse()

    print("""Stress Balls:
    # balls | FPS...""")
    flush()

    FRAME = simplegui.create_frame('Stress Balls' +
                                   (' TRANSPARENCY' if TRANSPARENCY
                                    else '') +
                                   (' REVERSE' if REVERSE
                                    else '') +
                                   (' _FPS_AVERAGE' if _FPS_AVERAGE
                                    else ''),
                                   WIDTH, HEIGHT)

    FRAME.add_button('Un/Freeze', freeze_on_off)
    FRAME.add_button('Revert', revert)
    FRAME.add_button('Without/With transparency', transparency_on_off)
    FRAME.add_button('Next step', next_step)
    FRAME.add_label('')
    FRAME.add_button('Quit', stop)

    init()

    FRAME.set_draw_handler(draw)

    TIMER = simplegui.create_timer(1000, print_fps)
    TIMER.start()

    FRAME.start()


if __name__ == '__main__':
    main()
