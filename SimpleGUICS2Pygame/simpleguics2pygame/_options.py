#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/_options (August 16, 2015)

Options helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import division
from __future__ import print_function


__all__ = []


try:
    import pygame

    _PYGAME_AVAILABLE = True
except ImportError:
    _PYGAME_AVAILABLE = False


#
# "Private" function
####################
def _set_option_from_argv():
    """
    Read arguments in sys.argv
    and set options.

    * ``--default-font``: Use Pygame default font instead serif, monospace...
      (this is faster if you display a lot of text).
    * ``--display-fps``: Display FPS average on the canvas.
    * ``--fps n``: Set Frame Per Second (default is 60 FPS).
    * ``--fullscreen``: Fullscreen mode.
    * ``--keep-timers``: Keep running timers when close frame without ask.
    * ``--no-border``: Window without border.
    * ``--no-controlpanel``: Hide the control panel (and status boxes).
    * ``--no-load-sound``: Don't load any sound.
    * ``--no-status``: Hide two status boxes.
    * ``--overwrite-downloaded-medias``: Download all images and sounds
      from Web and save in local directory even if they already exist.
    * ``--print-load-medias``: Print URLs or locals filename loaded.
    * ``--print-stats-cache``: After frame stopped,
      print some statistics of caches.
    * ``--save-downloaded-medias``: Save images and sounds downloaded
      from Web that don't already exist in local directory.
    * ``--stop-timers``: Stop all timers when close frame without ask.

    If an argument is not in this list
    then it is ignored and all next arguments are ignored.

    Arguments used by SimpleGUICS2Pygame is deleted to ``sys.argv``.

    This function is executed when the module is imported.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """
    from sys import argv

    from SimpleGUICS2Pygame.simpleguics2pygame.frame import Frame
    from SimpleGUICS2Pygame.simpleguics2pygame.sound import Sound

    nb_module_arg = 0
    i = 1
    while i < len(argv):
        arg = argv[i]
        nb_module_arg += 1
        if arg == '--default-font':
            Frame._default_font = True
        elif arg == '--display-fps':
            Frame._display_fps_average = True
        elif arg == '--fps':
            nb_module_arg += 1
            i += 1
            try:
                Frame._fps = max(0, int(argv[i]))
            except (IndexError, ValueError):
                Frame._fps = 0
        elif arg == '--fullscreen':
            if _PYGAME_AVAILABLE:
                Frame._pygame_mode_flags |= (pygame.FULLSCREEN
                                             | pygame.HWSURFACE)
        elif arg == '--keep-timers':
            Frame._keep_timers = True
        elif arg == '--no-border':
            if _PYGAME_AVAILABLE:
                Frame._pygame_mode_flags |= pygame.NOFRAME
        elif arg == '--no-controlpanel':
            Frame._hide_controlpanel = True
        elif arg == '--no-load-sound':
            Sound._load_disabled = True
        elif arg == '--no-status':
            Frame._hide_status = True
        elif arg == '--overwrite-downloaded-medias':
            Frame._save_downloaded_medias = True
            Frame._save_downloaded_medias_overwrite = True
        elif arg == '--print-load-medias':
            Frame._print_load_medias = True
        elif arg == '--print-stats-cache':
            Frame._print_stats_cache = True
        elif arg == '--save-downloaded-medias':
            Frame._save_downloaded_medias = True
            Frame._save_downloaded_medias_overwrite = False
        elif arg == '--stop-timers':
            Frame._keep_timers = False
        else:
            nb_module_arg -= 1

            break

        i += 1

    del argv[1:nb_module_arg + 1]
