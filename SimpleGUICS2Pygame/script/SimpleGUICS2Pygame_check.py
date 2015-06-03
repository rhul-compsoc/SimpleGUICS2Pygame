#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
script/SimpleGUICS2Pygame_check.py

(June 3, 2015)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2015 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import print_function

import os
import sys


########
# Main #
########
if __name__ == '__main__':
    print("""script/SimpleGUICS2Pygame_check.py (June 3, 2014)
=================================================""")

    # Environment variables
    print('PATH:')
    path_str = os.getenv('PATH')
    if path_str is not None:
        for path in path_str.split(os.pathsep):
            print(' ', path)

    print()

    print('PYTHONPATH:')
    path_str = os.getenv('PYTHONPATH')
    if path_str is not None:
        for path in path_str.split(os.pathsep):
            print(' ', path)

    print('\n')

    # Python
    print('python - version', sys.version, end='\n\n')

    print('sys.path:')
    for path in sys.path:
        print(' ', path)

    print('\n')

    # matplotlib
    CMD = 'import matplotlib'
    try:
        import matplotlib

        print(CMD, 'ok - Version', matplotlib.__version__)
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    print('\n')

    # Pygame
    CMD = 'import pygame'
    try:
        import pygame

        print(CMD, 'ok - Version', pygame.version.ver)

        CMD = 'pygame.init()'
        try:
            SUCCESS, FAILED = pygame.init()

            if FAILED == 0:
                print(' ', CMD, SUCCESS, 'modules loaded ok')
            else:
                print(' ', CMD, SUCCESS, 'modules loaded',
                      FAILED, 'failed WARNING!')
        except Exception as exc:
            print(' ', CMD, 'FAILED!', exc)
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    print('\n')

    # SimpleGUICS2Pygame
    CMD = 'import SimpleGUICS2Pygame'
    try:
        import SimpleGUICS2Pygame

        print(CMD, 'ok - Version', SimpleGUICS2Pygame._VERSION)
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    print()

    CMD = 'import SimpleGUICS2Pygame.codeskulptor'
    try:
        import SimpleGUICS2Pygame.codeskulptor

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.codeskulptor_lib'
    try:
        import SimpleGUICS2Pygame.codeskulptor_lib

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.numeric'
    try:
        import SimpleGUICS2Pygame.numeric

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib'
    try:
        import SimpleGUICS2Pygame.simplegui_lib

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_draw'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_draw

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_fps'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_fps

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_keys'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_keys

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simplegui_lib_loader'
    try:
        import SimpleGUICS2Pygame.simplegui_lib_loader

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simpleguics2pygame'
    try:
        import SimpleGUICS2Pygame.simpleguics2pygame

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)

    CMD = 'import SimpleGUICS2Pygame.simpleplot'
    try:
        import SimpleGUICS2Pygame.simpleplot

        print(CMD, 'ok')
    except Exception as exc:
        print(CMD, 'FAILED!', exc)
