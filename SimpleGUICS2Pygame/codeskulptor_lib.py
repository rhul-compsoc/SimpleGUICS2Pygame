# -*- coding: latin-1 -*-

"""
codeskulptor_lib (June 22, 2013)

Some miscellaneous functions to help in CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""


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
    try:
        from simplegui import KEY_MAP

        return True
    except:
        return False


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


def rgba(red, green, blue,
         alpha=1):
    """
    Return the string HTML representation of the color
    in 'rgba(red,blue,green,alpha)' format.

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

    return 'rgba(%d, %d, %d, %s)' % (red, green, blue,
                                     # To avoid CodeSkulptor %f bug on Firefox!
                                     str(alpha))
