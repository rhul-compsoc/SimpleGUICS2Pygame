# -*- coding: latin-1 -*-

"""
simplegui_lib_fps (May 25, 2014)

A class to calculate and display FPS (Frames Per Second)
in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""


# Class
########
class FPS:
    """
    Calculate and display FPS (Frames Per Second).

    How to use:

    * Create an instance of FPS: ``fps = FPS()``
    * Start: ``fps.start()``
    * And put the ``draw_fct()`` in the end of your canvas' draw handler: ``fps.draw_fct(canvas)``
    """

    def __init__(self, x=10, y=10, font_color='Red', font_size=40):
        """
        Set an instance to calculate FPS and drawing on position (x, y).

        :param x: int or float
        :param y: int or float
        :param font_color: str
        :param font_size: int > 0
        """
        assert isinstance(x, int) or isinstance(x, float), type(x)
        assert isinstance(y, int) or isinstance(y, float), type(y)
        assert isinstance(font_color, str), type(font_color)
        assert font_size > 0, font_size

        self._font_color = font_color
        self._font_size = font_size
        self._x = x
        self._y = y

        self._timer = None

    def draw_fct(self, canvas):
        """
        Update the number of frames drawn
        and draw the FPS.

        This method **must be** called from the canvas' draw handler
        (the function passed as a parameter
        to `simplegui.Frame.set_draw_handler()`).

        :param canvas: simplegui.Canvas
        """
        if self._timer is not None:
            self._nb_frames_drawed += 1

            canvas.draw_text(str(self._fps),
                             (self._x, self._y + self._font_size*3//4),
                             self._font_size, self._font_color)

    def is_started(self):
        """
        If FPS is active
        then return True,
        else return False.
        """
        return self._timer is not None

    def start(self):
        """
        Start calculation and drawing.

        See `draw_fct()`.
        """
        if self._timer is not None:
            self.stop()

        self._fps = 0
        self._nb_frames_drawed = 0
        self._nb_seconds = 0

        try:
            from simplegui import create_timer
        except ImportError:
            from SimpleGUICS2Pygame.simpleguics2pygame import create_timer

        def update():
            """
            Update counters.
            """
            if self._timer is not None:
                self._nb_seconds += 1
                self._fps = int(round(float(self._nb_frames_drawed)
                                      / self._nb_seconds))

        self._timer = create_timer(1000, update)

        self._timer.start()

    def stop(self):
        """
        Stop calculation and drawing.
        """
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
