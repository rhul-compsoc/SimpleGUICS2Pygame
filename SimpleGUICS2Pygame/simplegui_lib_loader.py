# -*- coding: latin-1 -*-

"""
simplegui_lib_loader (June 10, 2014)

A class to help load images and sounds
in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""


# Class
########
class Loader:
    """
    Help to load images and sounds from Internet
    and wait finished.

    With SimpleGUICS2Pygame,
    `SimpleGUICS2Pygame.load_image()` and `SimpleGUICS2Pygame.load_sound()`
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

    __SIMPLEGUICS2PYGAME = False
    """
    `True` if SimpleGUICS2Pygame are used,
    else `False`.
    """

    def __init__(self, frame, progression_bar_width,
                 after_function, max_waiting=5000):
        """
        Set an empty loader.

        :param frame: simplegui.Frame
        :param progression_bar_width: (int or float) >= 0
        :param after_function: function () -> *
        :param max_waiting: (int or float) >= 0
        """
        assert (isinstance(progression_bar_width, int)
                or isinstance(progression_bar_width, float)), \
            type(progression_bar_width)
        assert progression_bar_width >= 0, progression_bar_width

        # assert callable(after_function), type(after_function)

        self._frame = frame
        self._progression_bar_width = progression_bar_width
        self._after_function = after_function
        self._max_waiting = max_waiting

        self._images = {}
        self._sounds = {}

        self.__max_waiting_remain_started = False

        self.__max_waiting_remain = None
        self.__timer = None

        try:
            from SimpleGUICS2Pygame.simpleguics2pygame import load_image

            Loader.__SIMPLEGUICS2PYGAME = True
        except ImportError:
            pass

    def _draw_loading(self, canvas):
        """
        Draw waiting message on the canvas
        when images and sounds loading.

        :param canvas: simplegui.Canvas
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

        if self.__max_waiting_remain_started:
            nb = int(round(self.__max_waiting_remain/1000.0))
            canvas.draw_text('Abort after %d second%s...'
                             % (nb, ('s' if nb > 1
                                     else '')),
                             (10, 50 + size*2*3.0/4),
                             size, 'White')

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

    def cache_clear(self):
        """
        * In standard Python with SimpleGUICS2Pygame: Empty the cache of Pygame surfaces used by each image of this Loader. See `Image._pygamesurfaces_cached_clear`_ .
        * In SimpleGUI of CodeSkulptor: do nothing.

        .. _`Image._pygamesurfaces_cached_clear`: simpleguics2pygame_private.html#SimpleGUICS2Pygame.simpleguics2pygame.Image._pygamesurfaces_cached_clear
        """
        if Loader.__SIMPLEGUICS2PYGAME:
            for name, image in sorted(self._images.items()):
                image._pygamesurfaces_cached_clear()

    def get_image(self, name):
        """
        If an image named `name` exist
        then return it,
        else return `None`

        :param name: str

        :raise: Exception if Loader.load() was not executed
                since the addition of this image.

        :return: None or simplegui.Image
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

        :return: None or simplegui.Sound
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
        **Start loading** of all images and sounds added
        since last `Loader.load()` execution.

        * In standard Python with SimpleGUICS2Pygame: draw a progression bar on canvas and wait until the loading is finished.
        * In SimpleGUI of CodeSkulptor: *don't* wait.
        """
        if Loader.__SIMPLEGUICS2PYGAME:
            from SimpleGUICS2Pygame.simpleguics2pygame import load_image, \
                load_sound
        else:
            from simplegui import load_image, load_sound

        if Loader.__SIMPLEGUICS2PYGAME:
            handler_saved = self._frame._canvas._draw_handler
            self._frame._canvas._draw_handler = self._draw_loading

        for name in self._sounds:
            if Loader.__SIMPLEGUICS2PYGAME:
                self._frame._canvas._draw()
            if isinstance(self._sounds[name], str):
                self._sounds[name] = load_sound(self._sounds[name])

        for name in self._images:
            if Loader.__SIMPLEGUICS2PYGAME:
                self._frame._canvas._draw()
            if isinstance(self._images[name], str):
                self._images[name] = load_image(self._images[name])

        if Loader.__SIMPLEGUICS2PYGAME:
            self._frame._canvas._draw()
            self._frame._canvas._draw_handler = handler_saved

    def pause_sounds(self):
        """
        Pause all sounds.
        """
        for name in self._sounds:
            if not isinstance(self._sounds[name], str):
                self._sounds[name].pause()

    def print_stats_cache(self):
        """
        * In standard Python with SimpleGUICS2Pygame: Print to stderr some statistics of cached Pygame surfaces used by each image of this Loader. See `Image._print_stats_cache`_ .
        * In SimpleGUI of CodeSkulptor: do nothing.

        .. _`Image._print_stats_cache`: simpleguics2pygame_private.html#SimpleGUICS2Pygame.simpleguics2pygame.Image._print_stats_cache
        """
        if Loader.__SIMPLEGUICS2PYGAME:
            max_length = max([len(name) for name in self._images])
            for name, image in sorted(self._images.items()):
                image._print_stats_cache('Loader %s%s'
                                         % (name,
                                            ' '*(max_length - len(name))))

    def wait_loaded(self):
        """
        Draw a progression bar on canvas
        and wait until all images and sounds are fully loaded.
        Then execute `self._after_function`.

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

        self.__max_waiting_remain_started = True
        self.__max_waiting_remain = self._max_waiting

        if Loader.__SIMPLEGUICS2PYGAME:
            from SimpleGUICS2Pygame.simpleguics2pygame import create_timer
        else:
            from simplegui import create_timer

        self._frame.set_draw_handler(self._draw_loading)
        self.__timer = create_timer(Loader._interval, check_if_loaded)
        self.__timer.start()
