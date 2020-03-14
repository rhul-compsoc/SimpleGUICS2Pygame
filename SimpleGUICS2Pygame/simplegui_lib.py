# -*- coding: latin-1 -*-

"""
simplegui_lib

Some functions and classes to help
in SimpleGUI of CodeSkulptor,
from `simplegui_lib_draw`,
`simplegui_lib_fps`,
`simplegui_lib_keys`
and `simplegui_lib_loader`.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 14, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


try:
    from user40_AeChfAkzlcqs3wG import draw_rect, draw_text_multi, draw_text_side  # noqa  # pylint: disable=unused-import
    from user33_Bhc7VzXKbXGVQV1 import FPS  # pylint: disable=unused-import
    from user30_VE5zdyz5OZwgen9 import Keys  # pylint: disable=unused-import
    from user40_nMs7JxzimyImAv2 import Loader  # pylint: disable=unused-import
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_draw \
        import draw_rect, draw_text_multi, draw_text_side
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_keys import Keys
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader
