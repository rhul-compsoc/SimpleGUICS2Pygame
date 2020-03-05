#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Stopwatch: The Game (March 4, 2020)
(Stop the timer when 0 decisecond.)

My solution (slightly retouched) of the mini-project #3 of the course
https://www.coursera.org/course/interactivepython (Coursera 2013).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2020 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False


# Global constants
CANVAS_WIDTH = 350
CANVAS_HEIGHT = 220


# Global variables
nb_attempts = 0
nb_success = 0

time = 0


# Helper function
def format_time(decisecond):
    """
    Convert time in tenths of seconds
    into formatted string m:ss.t

    :param decisecond: int >= 0

    :return: str
    """
    assert isinstance(decisecond, int)
    assert decisecond >= 0

    decisecond, tenths = decisecond // 10, decisecond % 10
    minutes, seconds = decisecond // 60, decisecond % 60

    return '%d:%02d.%d' % (minutes, seconds, tenths)


# Event handlers for buttons
def quit_prog():
    """
    Stop timer and quit.
    """
    timer.stop()
    frame.stop()


def reset():
    """
    Reinit nb_attempts, nb_success and time
    and stop timer
    """
    global nb_attempts
    global nb_success
    global time

    timer.stop()

    nb_attempts = 0
    nb_success = 0

    time = 0


def start():
    """
    Start timer
    """
    timer.start()


def stop():
    """
    If timer is running
    then stop timer
    and increment nb_attempts
    and if time is multiple of 10 then increment nb_success
    """
    global nb_attempts
    global nb_success

    if timer.is_running():
        timer.stop()

        nb_attempts += 1
        if time % 10 == 0:
            nb_success += 1


# Event handler for timer
def tick():
    """
    Increment time
    """
    global time

    time += 1


# Draw handler
def draw(canvas):
    """
    Display time in center
    and display nb_success / nb_attempts on upper-right

    :param canvas: simplegui.Canvas
    """
    text = format_time(time)
    size = 60
    width = frame.get_canvas_textwidth(text, size, 'monospace')
    canvas.draw_text(text,
                     ((CANVAS_WIDTH - width) // 2,
                      # (CANVAS_HEIGHT - size) // 2 + size * 3 // 4
                      (CANVAS_HEIGHT * 2 + size) // 4),
                     size, 'Lime', 'monospace')

    if nb_attempts > 0:
        text = '%d/%d' % (nb_success, nb_attempts)
        percent_success = nb_success * 100 // nb_attempts
        size = (30 if nb_success == nb_attempts
                else 20)
        width = frame.get_canvas_textwidth(text, size, 'monospace')
        canvas.draw_text(text, (CANVAS_WIDTH - width * 5 // 4, size), size,
                         ('Red' if percent_success < 25
                          else ('Yellow' if percent_success >= 75
                                else 'White')),
                         'monospace')

    if timer.is_running():
        text = 'Stop the timer when 0 decisecond.'
        size = 20
        width = frame.get_canvas_textwidth(text, size)
        canvas.draw_text(text,
                         ((CANVAS_WIDTH - width) // 2, (CANVAS_HEIGHT - size)),
                         size, 'White')


# Create frame
frame = simplegui.create_frame('Stopwatch (Stop the timer when 0 decisecond)',
                               CANVAS_WIDTH, CANVAS_HEIGHT, 100)


# Register event handlers
frame.add_button('Start', start, 100)
frame.add_label('')
frame.add_button('Stop', stop, 100)
frame.add_label('')
frame.add_button('Reset', reset, 100)
frame.add_label('')
frame.add_button('Quit', quit_prog)

frame.set_draw_handler(draw)

timer = simplegui.create_timer(100, tick)


# Main
assert format_time(0) == '0:00.0'
assert format_time(3) == '0:00.3'
assert format_time(11) == '0:01.1'
assert format_time(321) == '0:32.1'
assert format_time(613) == '1:01.3'
assert format_time(1234) == '2:03.4'

frame.start()
