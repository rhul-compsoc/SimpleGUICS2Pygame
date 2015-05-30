#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/frame (May 30, 2015)

Class Frame.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import division
from __future__ import print_function


__all__ = ['Frame',
           'create_frame']


from SimpleGUICS2Pygame.simpleguics2pygame import _PYGAME_AVAILABLE
if _PYGAME_AVAILABLE:
    import pygame

from SimpleGUICS2Pygame.simpleguics2pygame._colors \
    import _SIMPLEGUICOLOR_TO_PYGAMECOLOR


#
# Class
#######
class Frame:
    """
    Frame similar to SimpleGUI `Frame` of CodeSkulptor.
    """

    _background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['white']
                                if _PYGAME_AVAILABLE
                                else None)
    """
    Default background color of frame.
    """

    _canvas_border_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['black']
                                   if _PYGAME_AVAILABLE
                                   else None)
    """
    Border color of canvas.
    """

    _controlpanel_background_pygame_color = (
        _SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
        else None)
    """
    Background color of control panel.
    """

    _default_font = False
    """
    If `True`
    then use Pygame default font instead serif, monospace...
    """

    _display_fps_average = False
    """
    If `True`
    then display FPS average on the canvas.
    """

    _fps = 60
    """
    Frames per second drawed (frequency of draw and check events)
    """

    _frame_instance = None
    """
    The only instance of Frame.
    """

    _hide_controlpanel = False
    """
    If `True`
    then hide control panel (and status box).
    """

    _hide_status = False
    """
    If `True`
    then hide status box.
    """

    _keep_timers = None
    """
    If `None`
    then ask if it should be stop timers when stop frame.

    If `True`
    then timers keep running when stop frame.

    If `False`
    then stop all timers when stop frame.
    """

    _print_load_medias = False
    """
    If `True`
    then print URLs or locals filename loaded by `load_image()`
    and `load_sound()`.
    """

    _print_stats_cache = False
    """
    If `True`
    then print some statistics of caches after frame stopped.
    """

    _pygamecolors_cached = {}
    """
    `Dict` {`str` CodeSkulptor color: `pygame.font.Color`}.
    """

    _pygamefonts_cached = {}
    """
    `Dict` {(`str` CodeSkulptor font face, `int` font size):
            `pygame.font.Font`}.
    """

    _pygamemedias_cached = {}
    """
    `Dict` {`str` URL: `pygame.Surface or pygame.mixer.Sound`}.
    """

    _pygame_mode_flags = 0
    """
    Default options of graphic mode.

    See http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    """

    _pygame_mode_depth = 0
    """
    Default number of bits used to represent color.

    See http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    """

    _save_canvas_requests = []
    """
    List of filenames in which to save canvas image.
    """

    _save_downloaded_medias = False
    """
    If `True`
    then save images and sounds downloaded from Web
    that don't already exist in local directory.
    See Frame._save_downloaded_medias_overwrite.
    """

    _save_downloaded_medias_overwrite = False
    """
    If `True` and `Frame._save_downloaded_medias`
    then download all images and sounds from Web
    and save in local directory even if they already exist.
    """

    _statuskey_background_pygame_color = (
        _SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
        else None)
    """
    `pygame.Color` of background in status key box.
    """

    _statuskey_height = 20
    """
    Height of the status key box.
    """

    _statuskey_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['black']
                               if _PYGAME_AVAILABLE
                               else None)
    """
    `pygame.Color` of status key box (text and rectangle).
    """

    _statuskey_pygame_font = (pygame.font.Font(None, _statuskey_height)
                              if _PYGAME_AVAILABLE
                              else None)
    """
    `pygame.font.Font` of status key box.
    """

    _statusmouse_background_pygame_color = (
        _SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
        else None)
    """
    `pygame.Color` of background in status mouse box.
    """

    _statusmouse_height = _statuskey_height
    """
    Height of the status mouse box.
    """

    _statusmouse_pygame_color = _statuskey_pygame_color
    """
    `pygame.Color` of status mouse box (text and rectangle).
    """

    _statusmouse_pygame_font = (pygame.font.Font(None, _statusmouse_height)
                                if _PYGAME_AVAILABLE
                                else None)
    """
    `pygame.font.Font` of status mouse box..
    """

    @classmethod
    def _pygamecolors_cached_clear(cls):
        """
        Empty the cache of Pygame colors used.

        Each color used is cached to accelerate drawing.
        If you use many many different colors maybe use this function
        to free memory.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        Side effect: Empty `Frame._pygamecolors_cached`.
        """
        cls._pygamecolors_cached = {}

    @classmethod
    def _pygamefonts_cached_clear(cls):
        """
        Empty the cache of Pygame fonts used.

        Each font used with each size is cached to accelerate drawing.
        If you use many many different sizes maybe use this function
        to free memory.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        Side effect: Empty `Frame._pygamefonts_cached`.
        """
        cls._pygamefonts_cached = {}

    def __init__(self,
                 title,
                 canvas_width, canvas_height,
                 control_width=200):
        """
        Set the frame.

        **Don't use directly**, use create_frame().

        :param title: str
        :param canvas_width: (int or float) >= 0
        :param canvas_height: (int or float) >= 0
        :param control_width: (int or float) >= 0
        """
        assert _PYGAME_AVAILABLE, """Pygame not available!
See http://simpleguics2pygame.readthedocs.org/en/latest/#installation"""

        assert Frame._frame_instance is None, \
            "You can't instantiate two Frame!"

        assert isinstance(title, str), type(title)

        assert (isinstance(canvas_width, int)
                or isinstance(canvas_width, float)), type(canvas_width)
        assert canvas_width >= 0, canvas_width

        assert (isinstance(canvas_height, int)
                or isinstance(canvas_height, float)), type(canvas_height)
        assert canvas_height >= 0, canvas_height

        assert (isinstance(control_width, int)
                or isinstance(control_width, float)), type(control_width)
        assert control_width >= 0, control_width

        Frame._frame_instance = self

        self._control_width = (0 if Frame._hide_controlpanel
                               else int(round(control_width)))

        self._border_size = (0 if Frame._hide_controlpanel
                             else 25)
        self._canvas_border_size = 2

        self._canvas_x_offset = (self._control_width + self._border_size*2
                                 + self._canvas_border_size)
        self._canvas_y_offset = self._border_size + self._canvas_border_size

        self._controls = []
        self._control_next_y = 10
        self._control_selected = None

        self._fps_average = 0

        self._keydown_handler = None
        self._keyup_handler = None

        self._mouseclic_handler = None
        self._mousedrag_handler = None

        self._running = False

        canvas_width = int(round(canvas_width))
        canvas_height = int(round(canvas_height))

        self._statusmouse_x_offset = 0
        self._statusmouse_y_offset = (self._canvas_y_offset + canvas_height
                                      - Frame._statusmouse_height)

        self._statuskey_x_offset = self._statusmouse_x_offset
        self._statuskey_y_offset = (self._statusmouse_y_offset
                                    - 5 - Frame._statuskey_height)

        # Create the window
        from os.path import sep

        icon_path = __file__.split(sep)[:-1]
        try:
            icon_path.extend(('_img', 'SimpleGUICS2Pygame_64x64_t.png'))
            pygame.display.set_icon(pygame.image.load(sep.join(icon_path)))
        except:
            pass

        self._pygame_surface = pygame.display.set_mode(
            ((self._canvas_x_offset + canvas_width
              + self._canvas_border_size + self._border_size),
             (self._canvas_y_offset + canvas_height
              + self._canvas_border_size + self._border_size)),
            Frame._pygame_mode_flags,
            Frame._pygame_mode_depth)
        pygame.display.set_caption(title)
        self._pygame_surface.fill(Frame._background_pygame_color)

        for i in range(1, self._canvas_border_size + 1):
            pygame.draw.rect(
                self._pygame_surface, Frame._canvas_border_pygame_color,
                (self._canvas_x_offset - i,
                 self._canvas_y_offset - i,
                 canvas_width + 2*i,
                 canvas_height + 2*i),
                1)

        # Create the canvas
        from SimpleGUICS2Pygame.simpleguics2pygame.canvas import Canvas

        self._canvas = Canvas(self, canvas_width, canvas_height)

        # Create the status boxes: key and mouse
        self._statuskey_pygame_surface = pygame.Surface(
            (self._control_width, Frame._statuskey_height))
        self._statusmouse_pygame_surface = pygame.Surface(
            (self._control_width, Frame._statusmouse_height))
        # will be drawn by self._draw_controlpanel()

        # Create the control panel
        self._controlpanel_pygame_surface = pygame.Surface(
            (self._control_width, canvas_height))
        self._draw_controlpanel()

        # Display all
        pygame.display.update()

    def __repr__(self):
        """
        Return '<Frame object>'.

        :return: str
        """
        return '<Frame object>'

    def _draw_controlpanel(self):
        """
        Draw the control panel
        and two status boxes.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        self._controlpanel_pygame_surface.fill(
            Frame._controlpanel_background_pygame_color)

        for control in self._controls:
            control._draw()

        if Frame._hide_controlpanel:
            return

        self._pygame_surface.blit(self._controlpanel_pygame_surface,
                                  (self._border_size,
                                   self._canvas_y_offset))

        self._draw_statuskey()
        self._draw_statusmouse()

        pygame.display.update((self._border_size,
                               self._canvas_y_offset,
                               self._control_width,
                               self._canvas._height))

    def _draw_statuskey(self, key=0, pressed=None):
        """
        Draw the status box of key.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param key: int
        :param pressed: None or bool
        """
        assert isinstance(key, int), type(key)
        assert (pressed is None) or isinstance(pressed, bool), type(pressed)

        if Frame._hide_status or Frame._hide_controlpanel:
            return

        self._statuskey_pygame_surface.fill(
            Frame._statuskey_background_pygame_color)
        pygame.draw.rect(self._statuskey_pygame_surface,
                         Frame._statuskey_pygame_color,
                         (0, 0, self._control_width, Frame._statuskey_height),
                         1)

        if pressed is not None:
            from SimpleGUICS2Pygame.simpleguics2pygame.keys \
                import _SIMPLEGUIKEY_TO_STATUSKEY

            key = _SIMPLEGUIKEY_TO_STATUSKEY.get(key, key)
            text = 'Key: {} {}'.format(('Down' if pressed
                                        else 'Up'),
                                       (key if isinstance(key, str)
                                        else '<{}>'.format(key)))
        else:
            text = 'Key:'

        pygame_surface_text = Frame._statuskey_pygame_font.render(
            text, True, Frame._statuskey_pygame_color)
        self._statuskey_pygame_surface.blit(
            pygame_surface_text,
            (5,
             (Frame._statuskey_height - pygame_surface_text.get_height())/2))

        self._pygame_surface.blit(self._statuskey_pygame_surface,
                                  ((self._border_size
                                    + self._statuskey_x_offset),
                                   self._statuskey_y_offset))

        pygame.display.update((self._border_size + self._statuskey_x_offset,
                               self._statuskey_y_offset,
                               self._control_width,
                               Frame._statuskey_height))

    def _draw_statusmouse(self, position=(0, 0), pressed=None):
        """
        Draw the status box of mouse.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param position: (int or float, int or float)
                         or [int or float, int or float]
        :param pressed: bool
        """
        assert isinstance(position, tuple) or isinstance(position, list), \
            type(position)
        assert len(position) == 2, len(position)
        assert isinstance(position[0], int) or isinstance(position[0], float),\
            type(position[0])
        assert isinstance(position[1], int) or isinstance(position[1], float),\
            type(position[1])

        assert (pressed is None) or isinstance(pressed, bool), type(pressed)

        if Frame._hide_status or Frame._hide_controlpanel:
            return

        self._statusmouse_pygame_surface.fill(
            Frame._statusmouse_background_pygame_color)
        pygame.draw.rect(self._statusmouse_pygame_surface,
                         Frame._statusmouse_pygame_color,
                         (0, 0,
                          self._control_width, Frame._statusmouse_height), 1)

        text = ('Mouse: {} {}, {}'.format(('Move' if pressed
                                           else 'Click'),
                                          position[0], position[1])
                if pressed is not None
                else 'Mouse:')

        pygame_surface_text = Frame._statusmouse_pygame_font.render(
            text, True, Frame._statusmouse_pygame_color)
        self._statusmouse_pygame_surface.blit(
            pygame_surface_text,
            (5,
             (Frame._statusmouse_height - pygame_surface_text.get_height())/2))

        self._pygame_surface.blit(self._statusmouse_pygame_surface,
                                  (self._border_size
                                   + self._statusmouse_x_offset,
                                   self._statusmouse_y_offset))

        pygame.display.update((self._border_size + self._statusmouse_x_offset,
                               self._statusmouse_y_offset,
                               self._control_width,
                               Frame._statusmouse_height))

    def _get_fps_average(self):
        """
        Return the framerate average (in frame per second) computed by Pygame.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :return: float
        """
        return float(self._fps_average)

    def _pos_in_control(self, x, y):
        """
        If position (`x`, `y`)
        is on the zone of one `Control` or `TextAreaControl`
        then return it
        else return `None`.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param x: int or float
        :param y: int or float

        :return: None or Control or TextAreaControl
        """
        assert isinstance(x, int) or isinstance(x, float), type(x)
        assert isinstance(y, int) or isinstance(y, float), type(y)

        if (self._controls
                and (self._controls[0]._y1 <= y <= self._controls[-1]._y2)):
            for control in self._controls:
                if control._pos_in(x, y):
                    return control

        return None

    def _save_canvas_request(self, filename):
        """
        Request to save the canvas image in a file.

        (The images are saved on each cycle fixed by `Frame._fps`.)

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param filename: str
        """
        assert isinstance(filename, str), type(filename)

        self._save_canvas_requests.append(filename)

    def _save_canvas_and_stop(self, filename, after=1000):
        """
        Wait after ms (first wait until the frame is started),
        then save the canvas in a file
        and stop the program.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param filename: str
        :param after: int or float >= 0
        """
        assert isinstance(filename, str), type(filename)
        assert isinstance(after, int) or isinstance(after, float), type(after)
        assert after >= 0, after

        def save_canvas_and_stop():
            """
            Handler function will be executed.
            """
            if self._running:
                self._save_canvas_request(filename)

                from SimpleGUICS2Pygame.simpleguics2pygame.timer import Timer

                Timer._stop_all()
                self.stop()

        if after == 0:
            save_canvas_and_stop()
        else:
            from SimpleGUICS2Pygame.simpleguics2pygame.timer \
                import create_timer

            timer = create_timer(after, save_canvas_and_stop)
            timer.start()

    def _set_canvas_background_image(self, image):
        """
        Set an image to replace the background color of the canvas.

        :param image: None or Image
        """
        if __debug__:
            from SimpleGUICS2Pygame.simpleguics2pygame.image import Image

            assert (image is None) or isinstance(image, Image), type(image)

        self._canvas._background_pygame_surface_image = image._pygame_surface

    def add_button(self,
                   text,
                   button_handler,
                   width=None):
        """
        Add a button in the control panel.

        When the button are pressed and released,
        `button_handler` are executed.

        If `width` is not `None`
        then `text` is possibly cutted.

        But, in CodeSkulptor, the accurate appearance is browser dependent.
        And in SimpleGUICS2Pygame, the accurate appearance is font dependent.

        :param text: str
        :param button_handler: function () -> *
        :param width: None or int

        :return: Control
        """
        assert isinstance(text, str), type(text)
        assert callable(button_handler), type(button_handler)
        assert (width is None) or isinstance(width, int), type(width)

        from SimpleGUICS2Pygame.simpleguics2pygame.control import Control

        control = Control(self, text, button_handler, width)
        self._controls.append(control)

        self._draw_controlpanel()

        return control

    def add_input(self,
                  text,
                  input_handler,
                  width):
        """
        Add a "label" with an input box in the control panel.

        When click with left button of mouse on the "label" or input box,
        the focus is give to this input box.

        When press Tab,
        the focus is give to the next input box (if exist).

        When press Enter,
        this input box lost the focus
        and `input_handler` are executed with the input text.

        :param text: str
        :param input_handler: function (str) -> *
        :param width: int

        :return: Control
        """
        assert isinstance(text, str), type(text)
        assert callable(input_handler), type(input_handler)
        assert isinstance(width, int), type(width)

        from SimpleGUICS2Pygame.simpleguics2pygame.control \
            import TextAreaControl

        control = TextAreaControl(self, text, input_handler, width)
        self._controls.append(control)

        self._draw_controlpanel()

        return control

    def add_label(self, text, width=None):
        """
        Add a label in the control panel.

        If `width` is not `None`
        then `text` is possibly cutted.

        But, in CodeSkulptor, the accurate appearance is browser dependent.
        And in SimpleGUICS2Pygame, the accurate appearance is font dependent.

        :param text: str
        :param width: None or int

        :return: Control
        """
        assert isinstance(text, str), type(text)
        assert (width is None) or isinstance(width, int), type(width)

        from SimpleGUICS2Pygame.simpleguics2pygame.control import Control

        control = Control(self, text, width=width)
        self._controls.append(control)

        self._draw_controlpanel()

        return control

    def get_canvas_image(self):
        """
        NOT YET IMPLEMENTED! (Does nothing.)

        (Available in SimpleGUI of CodeSkulptor
        but *not in CodeSkulptor documentation*!)
        """
        pass

    def get_canvas_textwidth(self,
                             text,
                             font_size,
                             font_face='serif'):
        """
        Return the width needed to draw `text` by `Frame.draw_text()`.

        :param text: str
        :param font_size: (int or float) >= 0
        :param font_face: str == 'monospace', 'sans-serif', 'serif'

        :return: int or float >= 0
        """
        assert isinstance(text, str), type(text)

        assert isinstance(font_size, int) or isinstance(font_size, float), \
            type(font_size)
        assert font_size >= 0, font_size

        from SimpleGUICS2Pygame.simpleguics2pygame._fonts \
            import _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME, \
            _simpleguifontface_to_pygamefont

        assert isinstance(font_face, str), type(font_face)
        assert font_face in _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME, font_face

        font_size = int(round(font_size))

        return (_simpleguifontface_to_pygamefont(font_face,
                                                 font_size).size(text)[0]
                if font_size > 0
                else 0)

    def set_canvas_background(self,
                              color):
        """
        Set the background color of the canvas.

        :param color: str
        """
        assert isinstance(color, str), type(color)

        from SimpleGUICS2Pygame.simpleguics2pygame._colors \
            import _simpleguicolor_to_pygamecolor

        self._canvas._background_pygame_color = \
            _simpleguicolor_to_pygamecolor(color)

    def set_draw_handler(self,
                         draw_handler):
        """
        Set the function handler
        that will be executed each cycle fixed by `Frame._fps`.

        :param draw_handler: function (Canvas) -> *
        """
        assert callable(draw_handler), type(draw_handler)

        self._canvas._draw_handler = draw_handler

    def set_keydown_handler(self,
                            key_handler):
        """
        Set the function handler
        that will be executed (with the key code) when a key is released.

        (The events are checked on each cycle fixed by `Frame._fps`.)

        :param key_handler: function (int >= 0) -> *
        """
        assert callable(key_handler), type(key_handler)

        self._keydown_handler = key_handler

    def set_keyup_handler(self,
                          key_handler):
        """
        Set the function handler
        that will be executed (with the key code) when a key is pressed.

        (The events are checked on each cycle fixed by `Frame._fps`.)

        :param key_handler: function (int >= 0) -> *
        """
        assert callable(key_handler), type(key_handler)

        self._keyup_handler = key_handler

    def set_mouseclick_handler(self,
                               mouse_handler):
        """
        Set the function handler
        that will be executed (with the position of the mouse)
        when the left button of mouse is **released**.

        (The events are checked on each cycle fixed by `Frame._fps`.)

        :param mouse_handler: function ((int >= 0, int >= 0)) -> *
        """
        assert callable(mouse_handler), type(mouse_handler)

        self._mouseclic_handler = mouse_handler

    def set_mousedrag_handler(self,
                              mouse_handler):
        """
        Set the function handler
        that will be executed  (with the position of the mouse)
        **for each** new mouse position
        when the left button of mouse is pressed.

        (The events are checked on each cycle fixed by `Frame._fps`.)

        :param mouse_handler: function ((int >= 0, int >= 0)) -> *
        """
        assert callable(mouse_handler), type(mouse_handler)

        self._mousedrag_handler = mouse_handler

    def start(self):
        """
        Start the frame and these handler events.

        .. warning::
           ``Frame.start()`` is blocking
           until ``Frame.stop()`` execution or closing window.
           So timers must be started *before*,
           and states must be initialized *before*.
           (Or maybe after by a handler function.)

        (In SimpleGUI of CodeSkulptor this function is *not* blocking.)
        """
        from SimpleGUICS2Pygame.simpleguics2pygame.control \
            import TextAreaControl
        from SimpleGUICS2Pygame.simpleguics2pygame.keys \
            import _pygamekey_to_simpleguikey

        self._running = True

        mouse_drag_out_of_canvas = None

        clock = pygame.time.Clock()

        # Core of the drawing canvas and dealing events
        while self._running:
            # Draw canvas
            self._canvas._draw()

            # Save canvas images
            while Frame._save_canvas_requests:
                self._canvas._save(Frame._save_canvas_requests.pop(0))

            # Check events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:        # mouse moved
                    if self._mousedrag_handler is not None:
                        x = event.pos[0] - self._canvas_x_offset
                        y = event.pos[1] - self._canvas_y_offset
                        if pygame.mouse.get_pressed()[0]:  # left click
                            if ((not 0 <= x < self._canvas._width)
                                    or (not 0 <= y < self._canvas._height)):
                                # Out of canvas
                                mouse_drag_out_of_canvas = True

                            if not mouse_drag_out_of_canvas:
                                # In canvas
                                # and not out of canvas
                                #   since last mouse left button pressed
                                self._draw_statusmouse((x, y), True)
                                self._mousedrag_handler((x, y))
                elif event.type == pygame.MOUSEBUTTONDOWN:  # mouse b. pressed
                    if event.button == 1:  # left click
                        if ((0
                             <= event.pos[0] - self._canvas_x_offset
                             < self._canvas._width)
                            and (0
                                 <= event.pos[1] - self._canvas_y_offset
                                 < self._canvas._height)):  # in canvas
                            mouse_drag_out_of_canvas = False

                        if event.pos[0] < self._canvas_x_offset:
                            # In control panel
                            control = self._pos_in_control(
                                event.pos[0] - self._border_size,
                                event.pos[1] - self._canvas_y_offset)
                            if control is not None:
                                control._mouse_left_button(True)
                            elif self._control_selected is not None:
                                self._control_selected = None
                                self._draw_controlpanel()
                        elif self._control_selected is not None:
                            self._control_selected = None
                            self._draw_controlpanel()
                elif event.type == pygame.MOUSEBUTTONUP:    # mouse b. released
                    if event.button == 1:  # left click
                        x = event.pos[0] - self._canvas_x_offset
                        y = event.pos[1] - self._canvas_y_offset
                        if ((0 <= x < self._canvas._width)
                                and (0 <= y < self._canvas._height)):
                            # In canvas
                            if self._mouseclic_handler is not None:
                                self._draw_statusmouse((x, y), False)
                                self._mouseclic_handler((x, y))
                        elif x < 0:
                            # In control panel
                            control = self._pos_in_control(
                                event.pos[0] - self._border_size, y)
                            if control is not None:
                                control._mouse_left_button(False)
                elif event.type == pygame.KEYDOWN:          # key pressed
                    if ((self._control_selected is not None)
                        and isinstance(self._control_selected,
                                       TextAreaControl)):
                        self._control_selected._key(event, True)
                    elif self._keydown_handler is not None:
                        key = _pygamekey_to_simpleguikey(event.key)
                        self._draw_statuskey(key, True)
                        self._keydown_handler(key)
                elif event.type == pygame.KEYUP:            # key released
                    if ((self._control_selected is not None)
                        and isinstance(self._control_selected,
                                       TextAreaControl)):
                        self._control_selected._key(event, False)
                    elif self._keyup_handler is not None:
                        key = _pygamekey_to_simpleguikey(event.key)
                        self._draw_statuskey(key, False)
                        self._keyup_handler(key)
                elif event.type == pygame.QUIT:             # quit
                    self.stop()

            # Wait (if necessary) next cycle
            self._fps_average = clock.get_fps()
            clock.tick(Frame._fps)
            #clock.tick_busy_loop(Frame._fps)

        self.stop()

        while Frame._save_canvas_requests:
            self._canvas._save(Frame._save_canvas_requests.pop(0))

        Frame._frame_instance = None

        pygame.display.quit()

        if Frame._print_stats_cache:
            _print_stats_cache()

        Frame._pygamecolors_cached_clear()
        Frame._pygamefonts_cached_clear()

    def stop(self):
        """
        Stop frame activities.

        If (Frame._keep_timers is None) and there is still running timers
        then ask in the canvas if they must be stopped.

        (Maybe available in SimpleGUI of CodeSkulptor
        but *not in CodeSkulptor documentation*!)
        """
        from SimpleGUICS2Pygame.simpleguics2pygame.timer import Timer

        if Frame._keep_timers is not None or not Timer._timers_running:
            if not Frame._keep_timers:
                Timer._stop_all()

            self._running = False
        else:
            def check_key(key):
                """
                If key is 'Y'
                then stop all timers and stop the frame.

                If key is 'N'
                then stop the frame.

                :param key: int >= 0
                """
                from SimpleGUICS2Pygame.simpleguics2pygame.keys import KEY_MAP

                if key == KEY_MAP['Y']:
                    Timer._stop_all()
                    self._running = False
                elif key == KEY_MAP['N']:
                    self._running = False

            def draw_ask(canvas):
                """
                Draw request about running timers.

                :param canvas: simpleguics2pygame.Canvas
                """
                nb_timers_running = len(Timer._timers_running)
                if nb_timers_running == 0:
                    self._running = False

                size = 20
                canvas.draw_text('Stop {} running timer{}?'
                                 .format(nb_timers_running,
                                         ('s' if nb_timers_running >= 2
                                          else '')),
                                 (10, 10 + size*3/4), size, 'Black')
                canvas.draw_text('(Yes/No)',
                                 (10, 10 + size*7/4), size, 'Black')

            self._keydown_handler = None
            self._keyup_handler = None

            self._mouseclic_handler = None
            self._mousedrag_handler = None

            Frame._hide_status = True
            self._controls = []
            self._draw_controlpanel()

            self.set_draw_handler(draw_ask)
            self.set_canvas_background('White')

            self.set_keyup_handler(check_key)


#
# "Private" functions
#####################
def _print_stats_cache():
    """
    Print to stderr some statistics of cached colors, fonts and medias.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """
    from sys import stderr

    print("""# cached colors: {}
# cached fonts: {}
# cached medias: {}""".format(len(Frame._pygamecolors_cached),
                              len(Frame._pygamefonts_cached),
                              len(Frame._pygamemedias_cached)),
          file=stderr)
    stderr.flush()


#
# SimpleGUI function
####################
def create_frame(title,
                 canvas_width, canvas_height,
                 control_width=200):
    """
    Create and return an interactive window. ::

    | +-------+
    | | title |
    | +---------+--------------+
    | | control |              |
    | | panel   |    canvas    |
    | |         |              |
    | +---------+--------------+

    | `title`: title of the window.
    | `canvas_width`, canvas_height: dimensions of the canvas.
    | `control_width`: width of the control panel.

    (The frame is inactive until the execution of `Frame.start()`.)

    **Don't run twice!**

    :param title: str
    :param canvas_width: (int or float) >= 0
    :param canvas_height: (int or float) >= 0
    :param control_width: (int or float) >= 0

    :return: Frame
    """
    assert _PYGAME_AVAILABLE, """Pygame not available!
See http://simpleguics2pygame.readthedocs.org/en/latest/#installation"""

    assert isinstance(title, str), type(title)

    assert isinstance(canvas_width, int) or isinstance(canvas_width, float), \
        type(canvas_width)
    assert canvas_width >= 0, canvas_width

    assert isinstance(canvas_height, int) or isinstance(canvas_height, float),\
        type(canvas_height)
    assert canvas_height >= 0, canvas_height

    assert isinstance(control_width, int) or isinstance(control_width, float),\
        type(control_width)
    assert control_width >= 0, control_width

    return Frame(title, canvas_width, canvas_height, control_width)
