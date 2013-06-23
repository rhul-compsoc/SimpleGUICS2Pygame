#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Stress Ball - REVERSE (June 22, 2013)
  Display many "balls" and calculate FPS (Frame Per Second)

On Chrome: simpleplot failed!
On Safari: exception failed!

Inspired by "Classy Balls" of Bill:
  http://www.codeskulptor.org/#user14_iNYvGMFtb8poj1S.py
  https://class.coursera.org/interactivepython-002/forum/thread?thread_id=6142

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True

try:
    import simpleplot
except:
    print('No simpleplot!')


### Config >>>
MAX_NB_SECONDS = 30  # number of seconds before next step

ALPHA = False  # start with transparency if True
REVERSE = True  # reverse list_nb_balls if true

_FPS_AVERAGE = False  # use Frame._get_fps_average()
                      #   (only with SimpleGUICS2Pygame)

# Number of balls of each step
list_nb_balls = [1, 10, 20, 30, 40, 50, 75,
                 100, 200, 300, 400, 500, 750,
                 1000, 1500, 2000]
### <<< config

if REVERSE:
    list_nb_balls.reverse()


FONT_SIZE = 40

WIDTH = 599
HEIGHT = 407

RGB_COLORS = ((0,   0,   128),
              (0,   0,   255),
              (0,   128, 0),
              (0,   128, 128),
              (0,   255, 0),
              (0,   255, 255),
              (128, 0,   0),
              (128, 0,   128),
              (128, 128, 0),
              (128, 128, 128),
              (192, 192, 192),
              (255, 0,   0),
              (255, 0,   255),
              (255, 165, 0),
              (255, 255, 0),
              (255, 255, 255))


results = {}

transparency = ALPHA


class Ball:
    def __init__(self, center, radius, color, fill_color, velocity, shape):
        self.center_x = center[0]
        self.center_y = center[1]

        self.radius = radius

        self.color_rgba = color
        self.color = rgba_to_str(color)

        self.fill_color_rgba = fill_color
        self.fill_color = rgba_to_str(fill_color)

        self.velocity_x = velocity[0]
        self.velocity_y = velocity[1]

        self.draw = (self.draw_circle,
                     self.draw_disc,
                     self.draw_disc_border,
                     self.draw_square,
                     self.draw_squarefill,
                     self.draw_squarefill_border)[shape]

    def draw_circle(self, canvas):
        canvas.draw_circle((self.center_x, self.center_y),
                           self.radius, 2, self.color)

    def draw_disc(self, canvas):
        canvas.draw_circle((self.center_x, self.center_y),
                           self.radius, 1, self.color, self.color)

    def draw_disc_border(self, canvas):
        canvas.draw_circle((self.center_x, self.center_y),
                           self.radius, 2, self.color, self.fill_color)

    def draw_square(self, canvas):
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
        self.velocity_x = self.velocity_x_save
        self.velocity_y = self.velocity_y_save

        del self.velocity_x_save
        del self.velocity_y_save

    def freeze_on(self):
        self.velocity_x_save = self.velocity_x
        self.velocity_y_save = self.velocity_y

        self.velocity_x = 0
        self.velocity_y = 0

    def revert(self):
        if freezed:
            self.velocity_x_save = -self.velocity_x_save
            self.velocity_y_save = -self.velocity_y_save
        else:
            self.velocity_x = -self.velocity_x
            self.velocity_y = -self.velocity_y

    def transparency_reset(self):
        self.color = rgba_to_str(self.color_rgba)
        self.fill_color = rgba_to_str(self.fill_color_rgba)

    def move(self):
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
    l = list(d.keys())
    l.sort()

    return [(nb_balls, d[nb_balls])
            for nb_balls in l]


def init():
    global balls
    global fps
    global freezed
    global nb_balls
    global nb_frames_drawed
    global nb_seconds
    global results
    global to_next_step

    if len(list_nb_balls) == 0:
        timer.stop()

        results = dict_to_ordered_list(results)

        print('Results: {' + ', '
              .join(['%d: %d' % result for result in results]) + '}')

        try:
            # Don't work in Chrome!
            simpleplot.plot_lines('Stress Balls', 800, 650,
                                  '# balls', 'FPS',
                                  (results, ), True)
        except Exception as e:  # to avoid fail if no simpleplot
            print('simpleplot.plot_lines():' + str(e))

        try:
            frame.stop()
        except Exception as e:  # to avoid simpleguitk failed
            print('frame.stop():' + str(e))

        return

    if list_nb_balls:
        nb_balls = list_nb_balls.pop(0)

    fps = 0
    freezed = False
    nb_frames_drawed = 0
    nb_seconds = 0
    to_next_step = False

    balls = tuple([Ball([47 + n % (WIDTH - 100),
                         47 + n % (HEIGHT - 100)],  # position
                        19 + n % 11,  # radius
                        n_to_rgba((n + 1) % len(RGB_COLORS),
                                  .2 + float(n % 13)/15),  # color of border
                        n_to_rgba((n + 2) % len(RGB_COLORS),
                                  .2 + float((n + 3) % 14)/17),  # fill color
                        [3 + n % 7, 2 + n % 5],  # velocity
                        (n + 2) % 6)  # shape
                   for n in range(nb_balls)])


def n_to_rgba(n, alpha):
    n = RGB_COLORS[n]

    return (n[0], n[1], n[2], alpha)


def rgba_to_str(rgba):
    # %f failed on CodeSkulptor
    return ('rgba(%d, %d, %d, %s)' % rgba if transparency
            else 'rgba(%d, %d, %d, 1)' % rgba[:3])


# Handler
def freeze_on_off():
    global freezed

    if freezed:
        for ball in balls:
            ball.freeze_off()
    else:
        for ball in balls:
            ball.freeze_on()

    freezed = not freezed


def draw(canvas):
    global nb_frames_drawed

    for ball in balls:
        ball.draw(canvas)
        ball.move()

    nb_frames_drawed += 1

    s = '#%d | %d FPS' % (nb_balls,
                          (int(round(frame._get_fps_average())) if _FPS_AVERAGE
                           else fps))
    canvas.draw_text(s, (12, 13 + FONT_SIZE*3//4), FONT_SIZE, 'Gray')
    canvas.draw_text(s, (10, 10 + FONT_SIZE*3//4), FONT_SIZE, 'White')

    s = '%ds' % (MAX_NB_SECONDS - nb_seconds)
    x = WIDTH - 11 - frame.get_canvas_textwidth(s, FONT_SIZE)
    canvas.draw_text(s, (x - 2, 13 + FONT_SIZE*3//4), FONT_SIZE, 'Gray')
    canvas.draw_text(s, (x, 10 + FONT_SIZE*3//4), FONT_SIZE, 'White')


def next_step():
    global to_next_step

    to_next_step = True


def print_fps():
    global fps
    global nb_seconds

    nb_seconds += 1

    fps = (frame._get_fps_average() if _FPS_AVERAGE
           else int(round(float(nb_frames_drawed)/nb_seconds)))

    if (nb_seconds > MAX_NB_SECONDS) or to_next_step:
        print('%d | %d' % (nb_balls, fps))
        results[nb_balls] = fps

        init()


def revert():
    for ball in balls:
        ball.revert()


def stop():
    timer.stop()
    frame.stop()


def transparency_on_off():
    global transparency

    transparency = not transparency

    for ball in balls:
        ball.transparency_reset()


# Main
print("""Stress Balls:
# balls | FPS...""")

simplegui.Frame._stop_timers = True

frame = simplegui.create_frame('Stress Balls'
                               + (' ALPHA' if ALPHA
                                  else '')
                               + (' REVERSE' if REVERSE
                                  else '')
                               + (' _FPS_AVERAGE' if _FPS_AVERAGE
                                  else ''),
                               WIDTH, HEIGHT)

frame.add_button('Un/Freeze', freeze_on_off)
frame.add_button('Revert', revert)
frame.add_button('Without/With transparency', transparency_on_off)
frame.add_button('Next step', next_step)
frame.add_label('')
frame.add_button('Quit', stop)

init()

frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000, print_fps)
timer.start()

frame.start()
