#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Display results of Stress_Balls.py on my different environments.

See
https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/example/Stress_Balls/Stress_Balls.py

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2018, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: April 16, 2020
"""

try:
    # To avoid other simpleplot available in Python
    from codeskulptor import file2url    # noqa  # pytype: disable=import-error  # pylint: disable=unused-import
    import simpleplot  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleplot as simpleplot  # type: ignore

    SIMPLEGUICS2PYGAME = True


# Last results were evaluate on
#   Intel Xeon W3530 Quad-Core 2.8GHz 6Gio, Debian 9.12 Stretch
# All old results were evaluate on
#   Pentium Dual-Core 2.7GHz 2Gio, Window$ 7 64 bits:
ALL_RESULTS = {
    # SimpleGUICS2Pygame
    'SimpleGUICS2Pygame 02.00.00 Python 2.7.13 -O pygame 1.9.6':
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 60, 1250: 51, 1500: 43, 1750: 38, 2000: 33},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 59, 1250: 49, 1500: 41, 1750: 36, 2000: 32}),  # REVERSE
    'SimpleGUICS2Pygame 02.00.00 Python 3.5.3 -O pygame 1.9.6':
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 60, 1250: 50, 1500: 43, 1750: 38, 2000: 33},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 60, 1250: 50, 1500: 43, 1750: 38, 2000: 33}),  # REVERSE
    'old SimpleGUICS2Pygame 00.70.00 Python 2.7.5 -O Pygame 1.9.2pre':
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 59, 750: 46,
      1000: 37, 1500: 26, 2000: 21},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 59, 750: 46,
      1000: 37, 1500: 27, 2000: 21}),  # REVERSE
    'old SimpleGUICS2Pygame 00.70.00 Python 3.3.2 -O Pygame 1.9.2pre':
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 57, 500: 50, 750: 37,
      1000: 30, 1500: 21, 2000: 16},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 61, 400: 56, 500: 48, 750: 35,
      1000: 28, 1500: 20, 2000: 15}),  # REVERSE
    # SimpleGUI in CodeSkulptor 2
    'old Chrome 27.0':
    ({1: 40, 10: 40, 20: 38, 30: 35, 40: 33, 50: 35, 75: 35,
      100: 30, 200: 20, 300: 16, 400: 13, 500: 12, 750: 8,
      1000: 6, 1500: 5, 2000: 4},   # normal
     {1: 35, 10: 35, 20: 36, 30: 38, 40: 34, 50: 34, 75: 30,
      100: 30, 200: 20, 300: 15, 400: 13, 500: 12, 750: 8,
      1000: 6, 1500: 4, 2000: 4}),  # REVERSE
    'old Firefox 21.0':
    ({1: 60, 10: 60, 20: 60, 30: 58, 40: 57, 50: 47, 75: 29,
      100: 22, 200: 12, 300: 8, 400: 6, 500: 5, 750: 3,
      1000: 2, 1500: 2, 2000: 1},   # normal
     {1: 60, 10: 60, 20: 59, 30: 58, 40: 48, 50: 41, 75: 30,
      100: 23, 200: 12, 300: 8, 400: 6, 500: 5, 750: 3,
      1000: 3, 1500: 2, 2000: 1}),  # REVERSE
    'old Safari 5.1.7':
    ({1: 62, 10: 63, 20: 62, 30: 59, 40: 44, 50: 36, 75: 23,
      100: 19, 200: 12, 300: 8, 400: 7, 500: 6, 750: 5,
      1000: 4, 1500: 3, 2000: 3},   # normal
     {1: 63, 10: 63, 20: 63, 30: 55, 40: 42, 50: 35, 75: 23,
      100: 18, 200: 11, 300: 8, 400: 7, 500: 6, 750: 4,
      1000: 4, 1500: 3, 2000: 3}),  # REVERSE
    # SimpleGUITk by David Holm, https://pypi.org/project/SimpleGUITk
    'old SimpleGUITk 1.1.1 Python 2':
    ({1: 45, 10: 38, 20: 35, 30: 35, 40: 35, 50: 35, 75: 33,
      100: 31, 200: 24, 300: 20, 400: 17, 500: 15, 750: 11,
      1000: 9, 1500: 6, 2000: 5},   # normal
     {1: 44, 10: 38, 20: 37, 30: 35, 40: 35, 50: 34, 75: 33,
      100: 30, 200: 24, 300: 20, 400: 17, 500: 14, 750: 11,
      1000: 9, 1500: 6, 2000: 5}),  # REVERSE
    'old SimpleGUITk 1.1.1 Python 3':
    ({1: 45, 10: 39, 20: 37, 30: 37, 40: 36, 50: 36, 75: 33,
      100: 31, 200: 24, 300: 20, 400: 17, 500: 15, 750: 11,
      1000: 9, 1500: 6, 2000: 5},  # normal
     {1: 45, 10: 38, 20: 35, 30: 36, 40: 34, 50: 35, 75: 33,
      100: 31, 200: 24, 300: 20, 400: 17, 500: 15, 750: 11,
      1000: 9, 1500: 6, 2000: 5})}  # REVERSE


#
# Main
######
def main():  # pylint: disable=too-many-locals
    """Calculate and print average, and open plot."""
    # Calculate average
    alls_nb_set = set()

    for legend in ALL_RESULTS:
        data_a, data_b = ALL_RESULTS[legend]

        nb_balls_a = list(data_a.keys())  # pytype: disable=attribute-error
        nb_balls_a.sort()

        nb_balls_b = list(data_b.keys())  # pytype: disable=attribute-error
        nb_balls_b.sort()

        assert nb_balls_a == nb_balls_b, (nb_balls_a, nb_balls_b)

        results = {}

        for nb in nb_balls_b:
            alls_nb_set.add(nb)
            results[nb] = (data_a[nb] + data_b[nb]) / 2.0

        ALL_RESULTS[legend] = results

    # Sort results to display
    alls_nb = list(alls_nb_set)
    alls_nb.sort()

    legends = list(ALL_RESULTS.keys())
    legends.sort()

    datas = []
    datas_with_old = []

    for legend in legends:
        data = ALL_RESULTS[legend]

        nb_balls = list(data.keys())  # noqa  # type: ignore  # pylint: disable=no-member
        nb_balls.sort()

        r = []

        for nb in nb_balls:
            r.append((nb, data[nb]))

        if not legend.startswith('old '):
            datas.append(r)
        datas_with_old.append(r)

    # Display
    print('|'.join(['%4d' % nb for nb in alls_nb]) + '|Environment')

    print('----+' * len(alls_nb) + '-----------')
    for legend in legends:
        seq = []
        for nb in alls_nb:
            fps = ALL_RESULTS[legend].get(nb, None)  # noqa  # type: ignore  # pylint: disable=no-member
            seq.append((('%2d  ' % fps
                         if int(fps) == fps
                         else '%4.1f' % fps)
                        if fps is not None
                        else ' ' * 4))
        print('|'.join(seq) + '|' + legend)

    # Graph
    try:
        simpleplot.plot_lines('Stress Balls results (with old results)',
                              800, 650, '# balls', 'FPS',
                              datas_with_old, True, legends)
        simpleplot.plot_lines('Stress Balls results',
                              800, 650, '# balls', 'FPS',
                              datas, True,
                              tuple(legend for legend in legends
                                    if not legend.startswith('old ')))
        if SIMPLEGUICS2PYGAME:
            simpleplot._block()  # pylint: disable=protected-access
    except Exception as e:  # pylint: disable=broad-except
        # To avoid fail if no simpleplot
        print('!simpleplot.plot_lines():' + str(e))


if __name__ == '__main__':
    main()
