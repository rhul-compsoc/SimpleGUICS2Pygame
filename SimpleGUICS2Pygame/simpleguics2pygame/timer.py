#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/timer (March 10, 2020)

Class Timer.

**Don't require Pygame.**

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import division


__all__ = ['Timer',
           'create_timer']


#
# Class
#######
class Timer:
    """
    Timer similar to SimpleGUI `Timer` of CodeSkulptor.

    **Don't require Pygame.**
    """

    _timers_running = {}
    """
    `Dict` {(Timer id): `Timer`} of all timers are running.
    """

    @classmethod
    def _stop_all(cls):
        """
        Stop all timers.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        Side effect: Empty `Timer._timers_running`.
        """
        for timer in tuple(cls._timers_running.values()):
            timer.stop()

    def __init__(self, interval, timer_handler):
        """
        Set a time.

        **Don't use directly**, use `create_timer()`.

        :param interval: int or float > 0
        :param timer_handler: function () -> *
        """
        assert isinstance(interval, int) or isinstance(interval, float), \
            type(interval)
        assert interval > 0, interval
        assert callable(timer_handler), type(timer_handler)

        import threading

        def repeat_handler():
            """
            Function to create and start a new timer.
            """
            Timer._timers_running[id(self)] = self
            self._timer = threading.Timer(self._interval / 1000, self._handler)
            self._timer.start()
            timer_handler()

        self._interval = interval
        self._handler = repeat_handler

        self._is_running = False
        self._timer = None

    def __repr__(self):
        """
        Return `'<Timer object>'`.

        :return: str
        """
        return '<Timer object>'

    def get_interval(self):
        """
        Return the interval of this timer.

        (Maybe available in SimpleGUI of CodeSkulptor
        but *not in CodeSkulptor documentation*!)

        :return: (int or float) > 0
        """
        return self._interval

    def is_running(self):
        """
        If this timer is running
        then return `True`,
        else return `False`.

        :return: bool
        """
        return self._timer is not None

    def start(self):
        """
        Start this timer.

        .. warning::
           With SimpleGUICS2Pygame,
           ``Frame.start()`` is blocking
           until ``Frame.stop()`` execution or closing window.
           So timers must be started *before*,
           and states must be initialized *before*.
           (Or maybe after by a handler function.)

        (Side effect: Add `id(self)`: `self` in `Timer._timers_running`.)
        """
        if self._timer is None:
            import threading

            Timer._timers_running[id(self)] = self
            self._timer = threading.Timer(self._interval / 1000, self._handler)
            self._timer.start()

    def stop(self):
        """
        Stop this timer.

        (Side effect: Remove `id(self)` of `Timer. _timers_running`.)
        """
        if self._timer is not None:
            self._timer.cancel()
            self._timer = None

            del Timer._timers_running[id(self)]


#
# SimpleGUI function
####################
def create_timer(interval, timer_handler):
    """
    Create and return a timer
    that will execute the function `timer_handler`
    every `interval` milliseconds.

    The first execution of `time_handler`
    will take place after the first period.

    (The timer can be started by `Timer.start()`.)

    :param interval: int or float > 0
    :param timer_handler: function () -> *

    :return: Timer
    """
    assert isinstance(interval, int) or isinstance(interval, float), \
        type(interval)
    assert interval > 0, interval
    assert callable(timer_handler), type(timer_handler)

    return Timer(interval, timer_handler)
