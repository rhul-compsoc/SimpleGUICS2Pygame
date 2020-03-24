# -*- coding: latin-1 -*-

"""
codeskulptor

Replace the codeskulptor module of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 24, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


def file2url(filename):
    """
    Return a completed CodeSkulptor URL ressource from a short `filename`.

    Example given in the `CodeSkulptor file2url documentation`_:
    `file2url('assets-Quick_fox.txt')`
    returns
    `'http://codeskulptor-assets.commondatastorage.googleapis.com/assets-Quick_fox.txt'`

    Example given in the `CodeSkulptor3 urllib2-urlopen documentation`_
    (there is an error in `file2url` documentation):
    `file2url('assets_sample_text.txt')`
    returns
    `'//codeskulptor-assets.commondatastorage.googleapis.com/assets_sample_text.txt'`

    .. _`CodeSkulptor file2url documentation`: http://www.codeskulptor.org/docs.html#file2url
    .. _`CodeSkulptor3 urllib2-urlopen documentation`: https://py3.codeskulptor.org/docs.html#urllib2-urlopen

    :param filename: str

    :raise: ValueError if filename is in a incorrect format
                         (the good format is '^[a-zA-Z][a-zA-Z0-9]*[_-]')

    :return: str
    """  # noqa
    from re import search

    match = search('^([a-zA-Z][a-zA-Z0-9]*)[_-]', filename)

    if match is None:
        raise ValueError("invalid filename: '{}'".format(filename))

    return ('http://codeskulptor-{}.commondatastorage.googleapis.com/{}'
            .format(match.group(1), filename))


def set_timeout(seconds):
    """
    Does nothing.

    In CodeSkulptor, this function change the timeout imposed on all programs
    (by default 5 seconds).
    See `CodeSkulptor set_timeout documentation`_.

    .. _`CodeSkulptor set_timeout documentation`: http://www.codeskulptor.org/docs.html#set-timeout

    .. warning::
       This function is not available in SimpleGUI of CodeSkulptor3.

    :param seconds: int >= 0
    """  # noqa
    assert isinstance(seconds, int), type(seconds)
    assert seconds >= 0, seconds
