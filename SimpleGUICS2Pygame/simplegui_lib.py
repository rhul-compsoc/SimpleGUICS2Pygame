# -*- coding: latin-1 -*-

"""
simplegui_lib (June 10, 2014)

Some functions and classes to help
in SimpleGUI of CodeSkulptor,
from `simplegui_lib_draw`,
`simplegui_lib_fps`,
`simplegui_lib_keys`
and `simplegui_lib_loader`.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from user23_HY71NDvHu7WKaMa import draw_rect, draw_text_side
    from user33_Bhc7VzXKbXGVQV1 import FPS
    from user30_VE5zdyz5OZwgen9 import Keys
    from user34_7pdNdCOBbyLqAZs import Loader
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_rect, draw_text_side
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_keys import Keys
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader
