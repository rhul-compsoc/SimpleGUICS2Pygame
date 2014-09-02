#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test simpleplot bars. (September 1st, 2014)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui  # to avoid other simpleplot available in Python
    import simpleplot

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleplot as simpleplot

    SIMPLEGUICS2PYGAME = True


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version
    from matplotlib import __version__ as matplotlib_version

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    MATPLOTLIB_VERSION = 'matplotlib ' + matplotlib_version
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/
    MATPLOTLIB_VERSION = ''

datalist = [(1, 2), (2, 3), (5, 4), (8, 3), (9, 2)]
dataset = {1: 3, 2: 4, 5: 5, 8: 4, 9: 3}

filename = None

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        filename = argv[1]

if filename is None:
    simpleplot.plot_bars('Test plot_bars', 400, 400, 'x', 'y',
                         (datalist, dataset),
                         ('datalist', 'dataset'))
else:
    simpleplot.plot_bars('Test plot_bars', 400, 400, 'x', 'y',
                         (datalist, dataset),
                         ('datalist', 'dataset'),
                         _filename=filename)

if SIMPLEGUICS2PYGAME and (len(argv) != 2):
    simpleplot._block()
