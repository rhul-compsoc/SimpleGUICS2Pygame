# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/image.

Class Image.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: April 12, 2020
"""

from __future__ import division
from __future__ import print_function

# print('IMPORT', __name__)


__all__ = ('Image', '_LocalImage',
           'load_image',
           '_load_local_image')

import collections  # noqa
import sys  # noqa


from SimpleGUICS2Pygame.simpleguics2pygame._pygame_init import _PYGAME_AVAILABLE  # noqa  # pylint: disable=no-name-in-module

from SimpleGUICS2Pygame.simpleguics2pygame._media import _load_local_media, _load_media  # noqa  # pylint: disable=no-name-in-module


#
# "Private" function
####################
def _load_local_image(filename):
    """
    Create and return an image by loading a file from `filename`.
    Not founded file and errors are ignored.

    I recommend to use only Internet resources
    with the `load_image()` function.
    Then you can use your program **both**
    in standard Python and in CodeSkulptor.
    (See `Tips.html#download-medias`_ .)

    .. _`Tips.html#download-medias`: ../Tips.html#download-medias

    But if it is necessary,
    you can load local image with this "private" function.

    Supported formats are the same as the `load_image()` function.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param filename: str (**only a valid filename**, not URL)

    :return: _LocalImage
    """
    assert isinstance(filename, str), type(filename)

    return _LocalImage(filename)


#
# Class
#######
class Image:
    """Image similar to SimpleGUI `Image` of CodeSkulptor."""

    _dir_search_first = '_img/'
    """
    `load_image()` try **first** to loading image from this directory,
    and next if failed, try to loading from URL.

    This local directory is relative to the directory of your program.
    """

    _pygamesurfaces_cache_default_max_size = 1000  # noqa  # pylint: disable=invalid-name
    """
    Default maximum number of Pygame surfaces
    in the `self._pygamesurfaces_cached`.
    """

    def __init__(self, url):
        """
        Set an image.

        **Don't use directly**, use `load_image()`.

        :param url: str
        """
        assert _PYGAME_AVAILABLE, """Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation"""

        assert isinstance(url, str), type(url)

        self._url = url

        self._pygame_surface = (None if url == ''
                                else _load_media('Image', url,
                                                 Image._dir_search_first))

        self._pygamesurfaces_cached = collections.OrderedDict()

        self._pygamesurfaces_cache_max_size = \
            Image._pygamesurfaces_cache_default_max_size

        if __debug__:
            self._pygamesurfaces_cached_counts = [0, 0]
            self._draw_count = 0

    def __repr__(self):
        """
        Return `'<Image object>'`.

        :return: str
        """
        return '<Image object>'

    def _print_stats_cache(self, text='', short_url=True):
        """
        Print to stderr some statistics of cached Pygame surfaces
        used by this image.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param text: str
        :param short_url: bool
        """
        if __debug__:
            print('{}{:4} {:4}({:4},{:4})/{:4}={:2}% {}'
                  .format(text,
                          len(self._pygamesurfaces_cached),
                          sum(self._pygamesurfaces_cached_counts),
                          self._pygamesurfaces_cached_counts[0],
                          self._pygamesurfaces_cached_counts[1],
                          self._draw_count,
                          ((sum(self._pygamesurfaces_cached_counts) * 100 //
                            self._draw_count)
                           if self._draw_count != 0
                           else ''),
                          (self._url.split('/')[-1] if short_url
                           else self._url)),
                  file=sys.stderr)
        else:
            print('{}{:4} {}'.format(text,
                                     len(self._pygamesurfaces_cached),
                                     (self._url.split('/')[-1] if short_url
                                      else self._url)),
                  file=sys.stderr)

    def _pygamesurfaces_cached_clear(self):
        """
        Empty the cache of Pygame surfaces used by this image.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        self._pygamesurfaces_cached = collections.OrderedDict()

        if __debug__:
            self._pygamesurfaces_cached_counts = [0, 0]
            self._draw_count = 0

    def get_height(self):
        """
        Return the height ot this image.

        (If initialization of this image was failed
        then return `0`.)

        :return: int
        """
        return (self._pygame_surface.get_height()
                if self._pygame_surface is not None
                else 0)

    def get_width(self):
        """
        Return the width ot this image.

        (If initialization of this image was failed
        then return `0`.)

        :return: int
        """
        return (self._pygame_surface.get_width()
                if self._pygame_surface is not None
                else 0)


#
# "Private" class
#################
class _LocalImage(Image):
    """
    Child of Image to load local file image.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """

    def __init__(self, filename):  # pylint: disable=super-init-not-called
        """
        Set an image.

        **Don't use directly**, use `_load_local_image()`.

        :param filename: str
        """
        assert _PYGAME_AVAILABLE, """Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation"""

        assert isinstance(filename, str), type(filename)

        self._url = filename

        self._pygame_surface = (None if filename == ''
                                else _load_local_media('Image', filename))

        self._pygamesurfaces_cached = collections.OrderedDict()

        self._pygamesurfaces_cache_max_size = \
            Image._pygamesurfaces_cache_default_max_size

        if __debug__:
            self._pygamesurfaces_cached_counts = [0, 0]
            self._draw_count = 0

    def __repr__(self):
        """
        Return `'<_LocalImage object>'`.

        :return: str
        """
        return '<_LocalImage object>'


#
# SimpleGUI function
####################
def load_image(url):
    """
    Create and return an image by loading a file from `url`.
    Not founded URL and errors are ignored.

    SimpleGUICS2Pygame try **first** to loading image
    from `Image._dir_search_first` local directory (`_img/` by default),
    and next if failed, try to loading from `url`.

    This local directory is relative to the directory of your program.

    For example,
    ``load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png')``
    try first to loading from
    ``_img/commondatastorage.googleapis.com/codeskulptor_assets/lathrop/double_ship.png``.

    Supported formats are supported formats by Pygame to load:
    PNG, JPG, GIF (not animated)...
    (see https://www.pygame.org/docs/ref/image.html ).

    (CodeSkulptor may supported other formats,
    dependant on browser support.)

    I recommend PNG and JPG format.

    CodeSkulptor loads images **asynchronously**
    (the program continues without waiting for the images to be loaded).
    To handle this problem, you can use ``simplegui_lib_loader.Loader`` class.

    :param url: str (**only a valid URL**, not local filename)

    :return: Image
    """
    assert _PYGAME_AVAILABLE, """Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation"""

    assert isinstance(url, str), type(url)

    return Image(url)
