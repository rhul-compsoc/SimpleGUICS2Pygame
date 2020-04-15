#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test play sounds.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: April 16, 2020
"""

try:
    import simplegui  # type: ignore

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    SIMPLEGUICS2PYGAME = True
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access


LOCAL_SOUNDS = []
SOUNDS = []
TIMER = None


def load_from_web(url):
    """
    Load a sound from web.

    :param url: str
    """
    name = url.split('/')[-1]
    print('Load from web "%s"' % name)
    SOUNDS.append((True, name, simplegui.load_sound(url)))


def load_local(pathname):
    """
    Load a local sound from pathname.

    :param pathname: str
    """
    name = pathname.split('/')[-1]
    print('Load local "%s"' % name)
    LOCAL_SOUNDS.append((False, name, simplegui._load_local_sound(pathname)))  # noqa  # type: ignore  # pylint: disable=no-member,protected-access


def play():
    """Play one sound"""
    global TIMER  # pylint: disable=global-statement

    if SOUNDS:
        web, name, sound = SOUNDS.pop(0)
        if SIMPLEGUICS2PYGAME:
            length = sound._get_length()  # pylint: disable=protected-access
            length_str = ' %fs' % length
        else:
            length_str = ''
        print('Play "%s"%s loaded from %s' %
              (name, length_str, ('web' if web
                                  else 'local')))
        sound.play()
        if SIMPLEGUICS2PYGAME and (sound._get_length() == 0):  # noqa  # pylint: disable=protected-access
            # Don't wait for next sound
            play()
    else:
        print('End of test_sound')
        TIMER.stop()
        TIMER = None


#
# Main
######
def main():
    """Play WAV, OGG and MP3 sounds."""
    global SOUNDS  # pylint: disable=global-statement
    global TIMER  # pylint: disable=global-statement

    load_from_web('http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/bonus.wav')  # noqa
    load_from_web('http://commondatastorage.googleapis.com/codeskulptor-assets/jump.ogg')  # noqa
    load_from_web('http://codeskulptor-demos.commondatastorage.googleapis.com/pang/arrow.mp3')  # noqa

    if SIMPLEGUICS2PYGAME:
        load_local('_snd/chirp_1s.wav')
        load_local('_snd/missile.ogg')
        load_local('_snd/missile.mp3')
        SOUNDS = LOCAL_SOUNDS + SOUNDS

    TIMER = simplegui.create_timer(2000, play)
    TIMER.start()


if __name__ == '__main__':
    main()
