# -*- coding: latin-1 -*-

"""
codeskulptor (June 22, 2013)

Replace the codeskulptor module of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""


def file2url(filename):
    """
    Return a completed CodeSkulptor URL ressource from a short `filename`.

    Example given in the `CodeSkulptor documentation`_:
    `file2url('assets-Quick_fox.txt')`
    return
    `'http://codeskulptor-assets.commondatastorage.googleapis.com/assets-Quick_fox.txt'`

    .. _`CodeSkulptor documentation`: http://www.codeskulptor.org/docs.html

    :param filename: str

    :raise: ValueError if filename is in a incorrect format
                         (the good format is '^[a-zA-Z][a-zA-Z0-9]*[_-]')

    :return: str
    """
    from re import search

    m = search('^([a-zA-Z][a-zA-Z0-9]*)[_-]', filename)

    if m is None:
        raise ValueError("invalid filename: '{}'".format(filename))

    return ('http://codeskulptor-{}.commondatastorage.googleapis.com/{}'
            .format(m.group(1), filename))
