# -*- coding: latin-1 -*-

"""
codeskulptor_lib (October 4, 2014)

Some miscellaneous functions to help in CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""


# Private global variable
#########################
_codeskulptor_is = None
"""
Used to memoization by codeskulptor_is().
"""


# Functions
###########
def assert_position(position, non_negative=False, non_zero=False):
    """
    Assertions to check valid `position`:
    (int or float, int or float) or [int or float, int or float].

    If non_negative
    then each `int` or `float` must be >= 0.

    If non_zero
    then each `int` or `float` must be != 0.

    :param position: object
    :param non_negative: bool
    """
    assert isinstance(non_negative, bool), type(non_negative)
    assert isinstance(non_zero, bool), type(non_zero)

    assert isinstance(position, tuple) or isinstance(position, list), \
        type(position)
    assert len(position) == 2, len(position)

    assert isinstance(position[0], int) or isinstance(position[0], float), \
        type(position[0])
    assert isinstance(position[1], int) or isinstance(position[1], float), \
        type(position[1])

    if non_negative:
        assert position[0] >= 0, position
        assert position[1] >= 0, position

    if non_zero:
        assert position[0] != 0, position
        assert position[1] != 0, position


def codeskulptor_is():
    """
    If run in CodeSkulptor environment
    then return `True`,
    else return `False`.

    :return: bool
    """
    global _codeskulptor_is

    if _codeskulptor_is is None:
        try:
            from codeskulptor import file2url
            from simplegui import KEY_MAP

            _codeskulptor_is = True
        except ImportError:
            _codeskulptor_is = False

    return _codeskulptor_is


def hex2(n, uppercase=True):
    """
    Return 2 characters corresponding to the hexadecimal representation of `n`.

    :param n: 0 <= int < 256
    :param uppercase: bool

    :return: str (length == 2)
    """
    assert isinstance(n, int)
    assert 0 <= n < 256
    assert isinstance(uppercase, bool), type(uppercase)

    return hex_fig(n//16) + hex_fig(n % 16)


def hex_fig(n, uppercase=True):
    """
    Return the hexadecimal figure of `n`.

    :param n: 0 <= int < 16
    :param uppercase: bool

    :return: str (one character from 0123456789ABCDEF or 0123456789abcdef)
    """
    assert isinstance(n, int), type(n)
    assert 0 <= n < 16
    assert isinstance(uppercase, bool), type(uppercase)

    return (str(n) if n < 10
            else chr((ord('A' if uppercase
                          else 'a')
                      + n - 10)))


def hsl(hue, saturation, lightness):
    """
    Return the string HTML representation of the color
    in 'hsl(hue, lightness, saturation)' format.

    :param hue: float or int
    :param saturation: 0 <= float or int <= 100
    :param lightness: 0 <= float or int <= 100

    :return: str
    """
    assert isinstance(hue, float) or isinstance(hue, int)

    assert isinstance(saturation, float) or isinstance(saturation, int)
    assert 0 <= saturation <= 100

    assert isinstance(lightness, float) or isinstance(lightness, int)
    assert 0 <= lightness <= 100

    # %s to avoid CodeSkulptor %% bug
    return 'hsla(%d, %d%s, %d%s)' % (hue % 360,
                                     saturation, '%',
                                     lightness, '%')


def hsla(hue, saturation, lightness,
         alpha=1):
    """
    Return the string HTML representation of the color
    in 'hsla(hue, lightness, saturation, alpha)' format.

    :param hue: float or int
    :param saturation: 0 <= float or int <= 100
    :param lightness: 0 <= float or int <= 100
    :param alpha: 0 <= float or int <= 1

    :return: str
    """
    assert isinstance(hue, float) or isinstance(hue, int)

    assert isinstance(saturation, float) or isinstance(saturation, int)
    assert 0 <= saturation <= 100

    assert isinstance(lightness, float) or isinstance(lightness, int)
    assert 0 <= lightness <= 100

    assert isinstance(alpha, float) or isinstance(alpha, int)
    assert 0 <= alpha <= 1

    # %s to avoid CodeSkulptor %% bug
    return 'hsla(%d, %d%s, %d%s, %f)' % (hue % 360,
                                         saturation, '%',
                                         lightness, '%',
                                         alpha)


def rgb(red, green, blue):
    """
    Return the string HTML representation of the color
    in 'rgb(red, blue, green)' format.

    :param red:   0 <= int <= 255
    :param green: 0 <= int <= 255
    :param blue:  0 <= int <= 255

    :return: str
    """
    assert isinstance(red, int)
    assert 0 <= red < 256

    assert isinstance(green, int)
    assert 0 <= green < 256

    assert isinstance(blue, int)
    assert 0 <= blue < 256

    return 'rgba(%d, %d, %d)' % (red, green, blue)


def rgba(red, green, blue,
         alpha=1):
    """
    Return the string HTML representation of the color
    in 'rgba(red, blue, green, alpha)' format.

    :param red:   0 <= int <= 255
    :param green: 0 <= int <= 255
    :param blue:  0 <= int <= 255
    :param alpha: 0 <= float or int <= 1

    :return: str
    """
    assert isinstance(red, int)
    assert 0 <= red < 256

    assert isinstance(green, int)
    assert 0 <= green < 256

    assert isinstance(blue, int)
    assert 0 <= blue < 256

    assert isinstance(alpha, float) or isinstance(alpha, int)
    assert 0 <= alpha <= 1

    return 'rgba(%d, %d, %d, %f)' % (red, green, blue, alpha)
