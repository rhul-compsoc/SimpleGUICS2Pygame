#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Display my results of Stress_Balls.py on differents environments.
(March 7, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2018, 2020 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from codeskulptor import file2url  # to avoid other simpleplot available in Python  # noqa  # pylint: disable=unused-import
    import simpleplot

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleplot as simpleplot

    SIMPLEGUICS2PYGAME = True


# All my (old) results on Pentium Dual-Core 2.7GHz 2Gio, Windows 7 64 bits:
#   - Chrome 27.0
#   - Firefox 21.0
#   - Safari 5.1.7
#   - Python 2.7.5 (with -O option)
#   - Python 3.3.2 (with -O option)
#   - SimpleGUICS2Pygame 00.70.00 (with Pygame 1.9.2pre)
#   - SimpleGUITk 1.1.1
#       by David Holm, https://pypi.org/project/SimpleGUITk
#  https://class.coursera.org/interactivepython-002/forum/thread?thread_id=5767
ALL_RESULTS = {'Chrome':
               ({1: 40, 10: 40, 20: 38, 30: 35, 40: 33, 50: 35, 75: 35,
                 100: 30, 200: 20, 300: 16, 400: 13, 500: 12, 750: 8,
                 1000: 6, 1500: 5, 2000: 4},   # normal
                {1: 35, 10: 35, 20: 36, 30: 38, 40: 34, 50: 34, 75: 30,
                 100: 30, 200: 20, 300: 15, 400: 13, 500: 12, 750: 8,
                 1000: 6, 1500: 4, 2000: 4}),  # REVERSE
               'Firefox':
               ({1: 60, 10: 60, 20: 60, 30: 58, 40: 57, 50: 47, 75: 29,
                 100: 22, 200: 12, 300: 8, 400: 6, 500: 5, 750: 3,
                 1000: 2, 1500: 2, 2000: 1},   # normal
                {1: 60, 10: 60, 20: 59, 30: 58, 40: 48, 50: 41, 75: 30,
                 100: 23, 200: 12, 300: 8, 400: 6, 500: 5, 750: 3,
                 1000: 3, 1500: 2, 2000: 1}),  # REVERSE
               'Safari':
               ({1: 62, 10: 63, 20: 62, 30: 59, 40: 44, 50: 36, 75: 23,
                 100: 19, 200: 12, 300: 8, 400: 7, 500: 6, 750: 5,
                 1000: 4, 1500: 3, 2000: 3},   # normal
                {1: 63, 10: 63, 20: 63, 30: 55, 40: 42, 50: 35, 75: 23,
                 100: 18, 200: 11, 300: 8, 400: 7, 500: 6, 750: 4,
                 1000: 4, 1500: 3, 2000: 3}),  # REVERSE
               'Python2 SimpleGUICS2Pygame':
               ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
                 100: 62, 200: 62, 300: 62, 400: 62, 500: 59, 750: 46,
                 1000: 37, 1500: 26, 2000: 21},   # normal
                {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
                 100: 62, 200: 62, 300: 62, 400: 62, 500: 59, 750: 46,
                 1000: 37, 1500: 27, 2000: 21}),  # REVERSE
               'Python3 SimpleGUICS2Pygame':
               ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
                 100: 62, 200: 62, 300: 62, 400: 57, 500: 50, 750: 37,
                 1000: 30, 1500: 21, 2000: 16},   # normal
                {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
                 100: 62, 200: 62, 300: 61, 400: 56, 500: 48, 750: 35,
                 1000: 28, 1500: 20, 2000: 15}),  # REVERSE
               'Python2 SimpleGUITk':
               ({1: 45, 10: 38, 20: 35, 30: 35, 40: 35, 50: 35, 75: 33,
                 100: 31, 200: 24, 300: 20, 400: 17, 500: 15, 750: 11,
                 1000: 9, 1500: 6, 2000: 5},   # normal
                {1: 44, 10: 38, 20: 37, 30: 35, 40: 35, 50: 34, 75: 33,
                 100: 30, 200: 24, 300: 20, 400: 17, 500: 14, 750: 11,
                 1000: 9, 1500: 6, 2000: 5}),  # REVERSE
               'Python3 SimpleGUITk':
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

        nb_balls_a = list(data_a.keys())
        nb_balls_a.sort()

        nb_balls_b = list(data_b.keys())
        nb_balls_b.sort()

        assert nb_balls_a == nb_balls_b, (nb_balls_a, nb_balls_b)

        results = {}

        for nb in nb_balls_b:
            alls_nb_set.add(nb)
            results[nb] = int(round((data_a[nb] + data_b[nb]) / 2))

        ALL_RESULTS[legend] = results

    # Sort results to display
    alls_nb = list(alls_nb_set)
    alls_nb.sort()

    legends = list(ALL_RESULTS.keys())
    legends.sort()

    datas = []

    for legend in legends:
        data = ALL_RESULTS[legend]

        nb_balls = list(data.keys())
        nb_balls.sort()

        r = []

        for nb in nb_balls:
            r.append((nb, data[nb]))

        datas.append(r)

    # Display
    print('|'.join(['%4d' % nb for nb in alls_nb]) + '|Environment')

    print('----+' * len(alls_nb) + '-----------')
    for legend in legends:
        l = []
        for nb in alls_nb:
            fps = ALL_RESULTS[legend].get(nb, None)
            l.append(('%4d' % fps if fps is not None
                      else ' ' * 4))
        print('|'.join(l) + '|' + legend)

    # Graph
    try:
        simpleplot.plot_lines('Stress Balls', 800, 650, '# balls', 'FPS',
                              datas, True, legends)
        if SIMPLEGUICS2PYGAME:
            simpleplot._block()  # pylint: disable=protected-access
    except Exception as e:  # pylint: disable=broad-except
        # To avoid fail if no simpleplot
        print('!simpleplot.plot_lines():' + str(e))

if __name__ == '__main__':
    main()
