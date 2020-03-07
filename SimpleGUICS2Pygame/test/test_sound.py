#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test play sounds. (March 7, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access


SOUNDS = []
TIMER = None


def play():
    """Play one sound"""
    global TIMER  # pylint: disable=global-statement

    if SOUNDS:
        first = SOUNDS.pop(0)
        name, sound = first
        if SIMPLEGUICS2PYGAME:
            length = sound._get_length()  # pylint: disable=protected-access
            length_str = ' %fs' % length
        else:
            length_str = ''
        print('Play "%s"%s' % (name, length_str))
        sound.play()
    else:
        print('stop')
        TIMER.stop()
        TIMER = None


#
# Main
######
def main():
    """Play MP3, OGG and WAV sounds."""
    global TIMER  # pylint: disable=global-statement

    print('Load from web "arrow.mp3"')
    SOUNDS.append(('arrow.mp3', simplegui.load_sound('http://codeskulptor-demos.commondatastorage.googleapis.com/pang/arrow.mp3')))  # noqa

    print('Load from web "jump.ogg"')
    SOUNDS.append(('jump.ogg', simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/jump.ogg')))  # noqa

    print('Load from web "bonus.wav"')
    SOUNDS.append(('bonus.wav', simplegui.load_sound('http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/bonus.wav')))  # noqa

    if SIMPLEGUICS2PYGAME:
        print('Load local "chirp_1s.wav"')
        local_sound_chirp_wav = simplegui._load_local_sound('_snd/chirp_1s.wav')  # noqa  # pylint: disable=protected-access,no-member

        length = local_sound_chirp_wav._get_length()  # noqa  # pylint: disable=protected-access
        print('Play local "chirp_1s.wav" %fs' % length)
        local_sound_chirp_wav.play()

    print('(MP3 is NOT supported by Pygame)')

    TIMER = simplegui.create_timer(2000, play)
    TIMER.start()

if __name__ == '__main__':
    main()
