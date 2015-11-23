#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
script/pygame_check.py

(November 23, 2015)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import print_function

import sys


########
# Main #
########
if __name__ == '__main__':
    print("""script/pygame_check.py (November 23, 2015)
==========================================""")

    # Python
    print('python - version', sys.version, end='\n\n')

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
