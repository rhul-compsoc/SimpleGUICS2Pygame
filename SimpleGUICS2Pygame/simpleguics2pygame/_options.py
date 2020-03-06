#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/_options (March 6, 2020)

Options helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015, 2016, 2020 Olivier Pirson
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
def _set_option_from_argv():  # noqa  # pylint: disable=too-many-branches,too-many-statements
    """
    Read arguments in sys.argv
    and set options.

    * ``--default-font``: Use Pygame default font instead serif, monospace...
      (this is faster if you display a lot of text).
    * ``--display-fps``: Display FPS average on the canvas.
    * ``--fps n``: Set Frame Per Second (default is 60 FPS).
    * ``--frame-padding n``: Set the padding in pixels found around the canvas.
    * ``--fullscreen``: Fullscreen mode.
    * ``--keep-timers``: Keep running timers when close frame without ask.
    * ``--last``: Mark this argument
      as the last  SimpleGUICS2Pygame's argument. (Do nothing else.)
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

    (See `Tips.html#command-line-options`_ for usage examples.)

    .. _`Tips.html#command-line-options`: ../Tips.html#command-line-options

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """
    from sys import argv

    from SimpleGUICS2Pygame.simpleguics2pygame.frame import Frame  # noqa  # pylint: disable=no-name-in-module
    from SimpleGUICS2Pygame.simpleguics2pygame.sound import Sound  # noqa  # pylint: disable=no-name-in-module

    nb_module_arg = 0
    i = 1
    while i < len(argv):
        arg = argv[i]
        nb_module_arg += 1
        if arg == '--default-font':
            Frame._default_font = True  # pylint: disable=protected-access
        elif arg == '--display-fps':
            Frame._display_fps_average = True  # noqa  # pylint: disable=protected-access
        elif arg == '--fps':
            nb_module_arg += 1
            i += 1
            try:
                Frame._fps = max(0, int(argv[i]))  # noqa  # pylint: disable=protected-access
            except (IndexError, ValueError):
                Frame._fps = 0  # pylint: disable=protected-access
        elif arg == '--frame-padding':
            nb_module_arg += 1
            i += 1
            try:
                Frame._frame_padding = max(0, int(argv[i]))  # noqa  # pylint: disable=protected-access
            except (IndexError, ValueError):
                Frame._frame_padding = 0  # pylint: disable=protected-access
        elif arg == '--fullscreen':
            if _PYGAME_AVAILABLE:
                Frame._pygame_mode_flags |= pygame.FULLSCREEN | pygame.HWSURFACE  # noqa  # pylint: disable=no-member
        elif arg == '--keep-timers':
            Frame._keep_timers = True  # pylint: disable=protected-access
        elif arg == '--last':
            break
        elif arg == '--no-border':
            if _PYGAME_AVAILABLE:
                Frame._pygame_mode_flags |= pygame.NOFRAME  # noqa  # pylint: disable=protected-access,no-member
        elif arg == '--no-controlpanel':
            Frame._hide_controlpanel = True  # pylint: disable=protected-access
        elif arg == '--no-load-sound':
            Sound._load_disabled = True  # pylint: disable=protected-access
        elif arg == '--no-status':
            Frame._hide_status = True  # pylint: disable=protected-access
        elif arg == '--overwrite-downloaded-medias':
            Frame._save_downloaded_medias = True  # noqa  # pylint: disable=protected-access
            Frame._save_downloaded_medias_overwrite = True  # noqa  # pylint: disable=protected-access
        elif arg == '--print-load-medias':
            Frame._print_load_medias = True  # pylint: disable=protected-access
        elif arg == '--print-stats-cache':
            Frame._print_stats_cache = True  # pylint: disable=protected-access
        elif arg == '--save-downloaded-medias':
            Frame._save_downloaded_medias = True  # noqa  # pylint: disable=protected-access
            Frame._save_downloaded_medias_overwrite = False  # noqa  # pylint: disable=protected-access
        elif arg == '--stop-timers':
            Frame._keep_timers = False  # pylint: disable=protected-access
        else:
            nb_module_arg -= 1

            break

        i += 1

    del argv[1:nb_module_arg + 1]
