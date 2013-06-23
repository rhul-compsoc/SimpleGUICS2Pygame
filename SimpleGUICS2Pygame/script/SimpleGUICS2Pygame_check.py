#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
script/SimpleGUICS2Pygame_check.py

(June 23, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import print_function


########
# Main #
########
if __name__ == '__main__':
    print("""script/SimpleGUICS2Pygame_check.py
==================================""")

    try:
        cmd = 'import pygame'

        import pygame

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'failed!', e)

    try:
        cmd = 'pygame.init()'
        pygame.init()

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'failed!', e)

    print()

    try:
        cmd = 'import SimpleGUICS2Pygame'

        import SimpleGUICS2Pygame

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'failed!', e)

    print()

    try:
        cmd = 'import SimpleGUICS2Pygame.codeskulptor'

        import SimpleGUICS2Pygame.codeskulptor

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'failed!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.codeskulptor_lib'

        import SimpleGUICS2Pygame.codeskulptor_lib

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'failed!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simplegui_lib'

        import SimpleGUICS2Pygame.simplegui_lib

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'failed!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simpleguics2pygame'

        import SimpleGUICS2Pygame.simpleguics2pygame

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'failed!', e)
