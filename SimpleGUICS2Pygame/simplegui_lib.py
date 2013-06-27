# -*- coding: latin-1 -*-

"""
simplegui_lib (June 27, 2013)

Some functions to help in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""


# Class
########
class Loader:
    """
    Help to load images and sounds from Internet
    and wait finished.

    With SimpleGUICS2Pygame,
    `load_image()` and `load_sound()`
    wait automatically until loading is completed.

    But in CodeSkulptor, the browser load images and sounds asynchronously.
    (With SimpleGUI it is **impossible to verify that the sounds are loaded**.
    So `Loader` begin load sounds, and next begin load images.
    It wait each image is loaded,
    and considers that all downloads are completed.)
    """

    _interval = 100
    """
    Interval in ms betweed two check.
    """

    def __init__(self, frame, progression_bar_width,
                 after_function, max_waiting=5000):
        """
        Set an empty loader.

        :param frame: simpleguics2pygame.Frame or simplegui.Frame
        :param progression_bar_width: (int or float) >= 0
        :param after_function: function () -> *
        :param max_waiting: (int or float) >= 0
        """
        assert (isinstance(progression_bar_width, int)
                or isinstance(progression_bar_width, float)), \
            type(progression_bar_width)
        assert progression_bar_width >= 0, progression_bar_width

        #assert callable(after_function), type(after_function)

        self._frame = frame
        self._progression_bar_width = progression_bar_width
        self._after_function = after_function
        self._max_waiting = max_waiting

        self._images = {}
        self._sounds = {}

    def add_image(self, url, name=None):
        """
        Add an image from `url`
        and give it a name.

        **Execute `Loader.load()` before use images.**

        If `name` == `None`
        then "filename" of url is used.

        Example:
        If `url` == `'http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png'`
           and `name` == `None`
        then `'asteroid_blue.png'` is used.

        :param url: str
        :param name: None or str
        :param wait: bool
        """
        assert isinstance(url, str), type(url)
        assert (name is None) or isinstance(name, str), type(name)

        self._images[(url.split('/')[-1] if name is None
                      else name)] = url

    def add_sound(self, url, name=None):
        """
        Add a sound from `url`
        and give it a `name`.

        **Execute `Loader.load()` before use sounds.**

        If `name` == `None`
        then "filename" of `url` is used.

        Example:
        If `url` == `'http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg'`
           and `name` == `None`
        then `'Epoq-Lepidoptera.ogg'` is used.

        :param url: str
        :param name: None or str
        :param wait: bool
        """
        assert isinstance(url, str), type(url)
        assert (name is None) or isinstance(name, str), type(name)

        self._sounds[(url.split('/')[-1] if name is None
                      else name)] = url

    def draw_loading(self, canvas):
        """
        Draw waiting message on the canvas
        when images and sounds loading.

        :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
        """
        nb = self.get_nb_images() + self.get_nb_sounds()

        size = 30

        if (self._progression_bar_width > 0) and (nb > 0):
            percent = (self.get_nb_images_loaded()
                       + self.get_nb_sounds_loaded())*100.0/nb

            y = 30 + size*3.0/4
            canvas.draw_line((0, y),
                             (self._progression_bar_width, y), 20, 'White')
            if percent > 0:
                canvas.draw_line((0, y),
                                 (self._progression_bar_width*percent/100.0,
                                  y),
                                 20, 'Green')

        canvas.draw_text('Loading... %d%%' % int(percent),
                         (10, 10 + size*3.0/4),
                         size, 'White')

        if not self._SIMPLEGUICS2PYGAME:
            nb = int(round(self.__max_waiting_remain/1000.0))
            canvas.draw_text('Cancellation after %d second%s...'
                             % (nb, ('s' if nb > 1
                                     else '')),
                             (10, 50 + size*2*3.0/4),
                             size, 'White')

    def get_image(self, name):
        """
        If an image named `name` exist
        then return it,
        else return `None`

        :param name: str

        :raise: Exception if Loader.load() was not executed
                since the addition of this image.

        :return: None or (simpleguics2pygame.Image or simplegui.Image)
        """
        assert isinstance(name, str), type(name)

        image = self._images.get(name)

        if isinstance(image, str):
            raise Exception(
                "load() not executed since the addition of the image '%s'!"
                % name)

        return image

    def get_nb_images(self):
        """
        Return the number of images (loaded or not).

        :return: int >= 0
        """
        return len(self._images)

    def get_nb_images_loaded(self):
        """
        Return the number of loaded images.

        It is the number of begin loading by `Loader.load()`
        **and** fully completed.

        :return: int >= 0
        """
        return len([None for name in self._images
                    if ((not isinstance(self._images[name], str))
                        and (self._images[name].get_width() > 0))])

    def get_nb_sounds(self):
        """
        Return the number of sounds (loaded or not).

        :return: int >= 0
        """
        return len(self._sounds)

    def get_nb_sounds_loaded(self):
        """
        Return the number of loaded sounds.

        It is the number of begin loading by `Loader.load()`,
        **but not necessarily completed**.
        Because with SimpleGUI of CodeSkulptor
        it is **impossible to verify that the sounds are loaded**.

        :return: int >= 0
        """
        return len([None for name in self._sounds
                    if not isinstance(self._sounds[name], str)])

    def get_sound(self, name):
        """
        If a sound named `name` exist
        then return it,
        else return `None`

        :param name: str

        :raise: Exception if load() was not executed
                since the addition of this sound.

        :return: None or (simpleguics2pygame.Sound or simplegui.Sound)
        """
        assert isinstance(name, str), type(name)

        sound = self._sounds.get(name)

        if isinstance(sound, str):
            raise Exception(
                "load() not executed since the addition of the sound '%s'!"
                % name)

        return sound

    def load(self):
        """
        **Begin loading** of all images and sounds added
        since last `Loader.load()` execution.
        """
        try:
            from simplegui import load_image, load_sound

            SIMPLEGUICS2PYGAME = False
        except:
            from SimpleGUICS2Pygame.simpleguics2pygame import load_image, \
                load_sound

            SIMPLEGUICS2PYGAME = True

        self._SIMPLEGUICS2PYGAME = SIMPLEGUICS2PYGAME

        if SIMPLEGUICS2PYGAME:
            handler_saved = self._frame._canvas._draw_handler
            self._frame._canvas._draw_handler = self.draw_loading

        for name in self._sounds:
            if SIMPLEGUICS2PYGAME:
                self._frame._canvas._draw()
            if isinstance(self._sounds[name], str):
                self._sounds[name] = load_sound(self._sounds[name])

        for name in self._images:
            if SIMPLEGUICS2PYGAME:
                self._frame._canvas._draw()
            if isinstance(self._images[name], str):
                self._images[name] = load_image(self._images[name])

        if SIMPLEGUICS2PYGAME:
            self._frame._canvas._draw()
            self._frame._canvas._draw_handler = handler_saved

    def wait_loaded(self):
        """
        Wait all images and sounds are fully loaded,
        and next execute `self._after_function`.

        While waiting, display message and progression bar on canvas of frame.

        After `self._max_waiting` milliseconds,
        abort and execute `self._after_function`.

        See details in `get_nb_sounds_loaded()` documentation.
        """
        if (((self.get_nb_images_loaded() == self.get_nb_images())
             and (self.get_nb_sounds_loaded() == self.get_nb_sounds()))
                or (self._max_waiting <= 0)):
            self._after_function()

            return

        def check_if_loaded():
            """
            If all images and sounds are loaded
            then stop waiting and execute `self._after_function`.
            """
            self.__max_waiting_remain -= Loader._interval

            if (((self.get_nb_images_loaded() == self.get_nb_images())
                 and (self.get_nb_sounds_loaded() == self.get_nb_sounds()))
                    or (self.__max_waiting_remain <= 0)):
                self.__max_waiting_remain = 0
                self.__timer.stop()
                self._frame.set_draw_handler(lambda canvas: None)

                del self.__timer

                self._after_function()

        self.__max_waiting_remain = self._max_waiting

        try:
            from simplegui import create_timer
        except:
            from SimpleGUICS2Pygame.simpleguics2pygame import create_timer

        self._frame.set_draw_handler(self.draw_loading)
        self.__timer = create_timer(Loader._interval, check_if_loaded)
        self.__timer.start()


#
# Functions
############
def draw_rect(canvas, pos, size, line_width, line_color, fill_color=None):
    """
    Draw a rectangle.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
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

    See `simpleguics2pygame.draw_text()` or `simplegui.draw_text()`.

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
