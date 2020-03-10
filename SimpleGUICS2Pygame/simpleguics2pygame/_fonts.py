#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/_fonts (March 10, 2020)

Fonts helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
http://www.opimedia.be/
"""

__all__ = []


from SimpleGUICS2Pygame.simpleguics2pygame._pygame_lib import _PYGAME_AVAILABLE  # noqa  # pylint: disable=no-name-in-module
if _PYGAME_AVAILABLE:
    import pygame


#
# Private global constant
#########################
_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME = {
    'monospace': 'courier,couriernew',
    'sans-serif': 'arial,tahoma',
    'serif': 'timesnewroman,garamond,georgia'}
"""
Font faces using by SimpleGUI
to corresponding font names list used by Pygame.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# "Private" function
####################
def _simpleguifontface_to_pygamefont(font_face, font_size):  # noqa  # pylint: disable=invalid-name
    """
    Return a `pygame.font.Font` object
    corresponding to the SimpleGUI `font_face` name
    by using the `_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME` dictionary.

    If font_face is None or the correponding font is not founded,
    then use the default `pygame.font.Font`.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effect:
    Each new font with new size is added to `Frame._pygamefonts_cached`.
    See `Frame._pygamefonts_cached_clear()`.

    .. _`Frame._pygamefonts_cached_clear()`: frame.html#SimpleGUICS2Pygame.simpleguics2pygame.frame.Frame._pygamefonts_cached_clear

    :param font_face: None
                      or (str == key of _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME)
    :param font_size: int > 0

    :return: pygame.font.Font
    """  # noqa
    assert ((font_face is None) or
            ((isinstance(font_face, str) and
              (font_face in _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME)))), \
        font_face
    assert isinstance(font_size, int), type(font_size)
    assert font_size > 0, font_size

    from SimpleGUICS2Pygame.simpleguics2pygame.frame import Frame  # noqa  # pylint: disable=no-name-in-module

    font = Frame._pygamefonts_cached.get((font_face, font_size))  # noqa  # pylint: disable=protected-access

    if font is None:
        if (font_face is None) or Frame._default_font:  # noqa  # pylint: disable=protected-access
            font = pygame.font.SysFont(None, font_size)
        else:
            try:
                font = pygame.font.SysFont(
                    _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME[font_face],
                    font_size)
            except:  # pylint: disable=bare-except
                font = pygame.font.SysFont(None, font_size)

        Frame._pygamefonts_cached[(font_face, font_size)] = font  # noqa  # pylint: disable=protected-access

    return font
