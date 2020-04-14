# -*- coding: latin-1 -*-

"""
simplegui_lib module.

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
:version: April 14, 2020
"""

# print('IMPORT', __name__)


try:
    from user305_2AIoOM1Isi08A9H import draw_rect, draw_text_multi, draw_text_side  # noqa  # type: ignore  # pylint: disable=unused-import
    from user305_sqdXmWMw7Jq9Sdc import FPS  # noqa  # type: ignore  # pylint: disable=unused-import
    from user305_3Ofv0u7rEhsrJ6G import Keys  # noqa  # type: ignore  # pylint: disable=unused-import
    from user305_5j0j5Vq5STd2mPH import Loader  # noqa  # type: ignore  # pylint: disable=unused-import
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_rect, draw_text_multi, draw_text_side  # noqa
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_keys import Keys
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader
