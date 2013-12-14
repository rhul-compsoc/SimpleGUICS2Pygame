# -*- coding: latin-1 -*-

"""
simplegui_lib (December 14, 2013)

Some functions and classes to help
in SimpleGUI of CodeSkulptor,
from `simplegui_lib_draw`,
`simplegui_lib_fps`,
`simplegui_lib_keys`
and `simplegui_lib_loader`.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from user23_HY71NDvHu7WKaMa import draw_rect, draw_text_side
    from user27_0ymhUVX6zleSFrB import FPS
    from user27_KX2DJkIN6iSjW19 import Keys
    from user27_rSvHGawbvoYISaV import Loader
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_rect, draw_text_side
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_keys import Keys
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader
