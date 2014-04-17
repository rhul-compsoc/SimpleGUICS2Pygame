#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
script/SimpleGUICS2Pygame_check.py

(December 15, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import print_function

from sys import version


########
# Main #
########
if __name__ == '__main__':
    print("""script/SimpleGUICS2Pygame_check.py (December 13, 2013)
======================================================
python - version""", version)

    print('\n')

    try:
        cmd = 'import matplotlib'

        import matplotlib

        print(cmd, 'ok - Version', matplotlib.__version__)
    except Exception as e:
        print(cmd, 'FAILED!', e)

    print('\n')

    try:
        cmd = 'import pygame'

        import pygame

        print(cmd, 'ok - Version', pygame.version.ver)
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'pygame.init()'
        pygame.init()

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    print('\n')

    try:
        cmd = 'import SimpleGUICS2Pygame'

        import SimpleGUICS2Pygame

        print(cmd, 'ok - Version', SimpleGUICS2Pygame._VERSION)
    except Exception as e:
        print(cmd, 'FAILED!', e)

    print()

    try:
        cmd = 'import SimpleGUICS2Pygame.codeskulptor'

        import SimpleGUICS2Pygame.codeskulptor

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.codeskulptor_lib'

        import SimpleGUICS2Pygame.codeskulptor_lib

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.numeric'

        import SimpleGUICS2Pygame.numeric

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simplegui_lib'

        import SimpleGUICS2Pygame.simplegui_lib

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simplegui_lib_draw'

        import SimpleGUICS2Pygame.simplegui_lib_draw

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simplegui_lib_fps'

        import SimpleGUICS2Pygame.simplegui_lib_fps

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simplegui_lib_keys'

        import SimpleGUICS2Pygame.simplegui_lib_keys

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simplegui_lib_loader'

        import SimpleGUICS2Pygame.simplegui_lib_loader

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simpleguics2pygame'

        import SimpleGUICS2Pygame.simpleguics2pygame

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)

    try:
        cmd = 'import SimpleGUICS2Pygame.simpleplot'

        import SimpleGUICS2Pygame.simpleplot

        print(cmd, 'ok')
    except Exception as e:
        print(cmd, 'FAILED!', e)
