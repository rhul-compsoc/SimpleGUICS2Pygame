#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test command line options. (March 4, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2016, 2020 Olivier Pirson
http://www.opimedia.be/
"""

from sys import argv


BEFORE = tuple(argv)

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # noqa

AFTER = tuple(argv)


# Main
def test():
    """
    Test command line options
    """
    print(BEFORE)
    print(AFTER)

    assert len(BEFORE) >= len(AFTER) >= 1
    assert BEFORE[0] == AFTER[0]


test()
