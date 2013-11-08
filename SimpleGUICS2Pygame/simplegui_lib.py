# -*- coding: latin-1 -*-

"""
simplegui_lib (November 8, 2013)

Some functions and classes to help
in SimpleGUI of CodeSkulptor,
from `simplegui_lib_draw`,
`simplegui_lib_keys`
and `simplegui_lib_loader`.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

try:
    from user23_HY71NDvHu7WKaMa import draw_rect, draw_text_side
    from user23_9gk3AFlrXCZJFMe import Keys
    from user23_XEsEdVoFmntP29T import Loader
except:
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_rect, draw_text_side
    from SimpleGUICS2Pygame.simplegui_lib_keys import Keys
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader
