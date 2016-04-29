#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/sound (April 29, 2016)

Class Sound.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015, 2016 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import division
from __future__ import print_function


__all__ = ['Sound',
           'create_sound', 'load_sound',
           '_load_local_sound']


try:
    import pygame

    _PYGAME_AVAILABLE = True
except ImportError:
    _PYGAME_AVAILABLE = False


#
# Private global constant
#########################
_MIXER_FREQUENCY = 22050
"""
Sound frequency used by the mixer module of Pygame.
"""


#
# "Private" function
####################
def _load_local_sound(filename):
    """
    Create and return a sound by loading a file from `filename`.
    Not founded file and errors are ignored.

    I recommend to use only Internet resources
    with the `load_sound()` function.
    Then you can use your program **both**
    in standard Python and in CodeSkulptor.
    (See `Tips.html#download-medias`_ .)

    .. _`Tips.html#download-medias`: ../Tips.html#download-medias

    But if it is necessary,
    you can load local sound with this "private" function.

    Supported formats are the same as the `load_sound()` function.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param filename: str (**only a valid filename**, not URL)

    :return: _LocalSound
    """
    assert isinstance(filename, str), type(filename)

    return _LocalSound(filename)


#
# Class
#######
class Sound:
    """
    Sound similar to SimpleGUI `Sound` of CodeSkulptor.
    """

    _dir_search_first = '_snd/'
    """
    `load_sound()` try **first** to loading sound from this directory,
    and next if failed, try to loading from URL.

    This local directory is relative to the directory of your program.
    """

    _load_disabled = False
    """
    If `True`
    then load sounds are disabled.
    """

    _mixer_initialized = False
    """
    If `True`
    then pygame.mixer is initialized.
    """

    def __init__(self, url):
        """
        Set a sound (if not Sound._load_disabled).

        **Don't use directly**, use `load_sound()`.

        :param url: str
        """
        assert _PYGAME_AVAILABLE, """Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation"""

        assert isinstance(url, str), type(url)

        from SimpleGUICS2Pygame.simpleguics2pygame._media import _load_media

        self._pygame_channel = None
        self._pygame_sound = (None if Sound._load_disabled or (url == '')
                              else _load_media('Sound', url,
                                               Sound._dir_search_first))

        assert (self._pygame_sound is None) or Sound._mixer_initialized

    def __repr__(self):
        """
        Return `'<Sound object>'`.

        :return: str
        """
        return '<Sound object>'

    def _get_length(self):
        """
        Return the length of this sound in seconds.

        (If initialization of this sound was failed
        then return `0`.)

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :return: int or float
        """
        return (self._pygame_sound.get_length()
                if (self._pygame_sound is not None)
                else 0)

    def pause(self):
        """
        Pause this sound.
        (Use `Sound.play()` to resume.)
        """
        if ((self._pygame_channel is not None)
                and (self._pygame_channel.get_sound() == self._pygame_sound)):
            self._pygame_channel.pause()

    def play(self):
        """
        If this sound is paused
        then resume the sound,
        else start the sound.
        """
        if self._pygame_channel is not None:
            if self._pygame_channel.get_sound() == self._pygame_sound:
                self._pygame_channel.unpause()
            else:
                self._pygame_channel = self._pygame_sound.play()
        elif self._pygame_sound is not None:
            self._pygame_channel = self._pygame_sound.play()

    def rewind(self):
        """
        If this sound has already been started
        then stop the sound and rewind to the begining.
        """
        if ((self._pygame_channel is not None)
                and (self._pygame_channel.get_sound() == self._pygame_sound)):
            self._pygame_sound.stop()

    def set_volume(self, volume):
        """
        Change the volume of this sound.
        The default volume is `1` (maximum).

        :param volume: 0 <= int or float <= 1
        """
        assert isinstance(volume, int) or isinstance(volume, float), \
            type(volume)
        assert 0 <= volume <= 1, volume

        if self._pygame_sound is not None:
            self._pygame_sound.set_volume(volume)


#
# "Private" class
#################
class _LocalSound(Sound):
    """
    Child of Sound to load local file sound.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """

    def __init__(self, filename):
        """
        Set a sound (if not Sound._load_disabled).

        **Don't use directly**, use `_local_load_sound()`.

        :param filename: str
        """
        assert _PYGAME_AVAILABLE, """Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation"""

        assert isinstance(filename, str), type(filename)

        from SimpleGUICS2Pygame.simpleguics2pygame._media \
            import _load_local_media

        self._pygame_channel = None
        self._pygame_sound = (None if Sound._load_disabled or (filename == '')
                              else _load_local_media('Sound', filename))

        assert (self._pygame_sound is None) or Sound._mixer_initialized

    def __repr__(self):
        """
        Return `'<_LocalSound object>'`.

        :return: str
        """
        return '<_LocalSound object>'


#
# SimpleGUI functions
#####################
def create_sound(sound_data, sample_rate=8000, num_channels=1):
    """
    NOT YET IMPLEMENTED! (Return an empty `Sound`.)

    (Available in SimpleGUI of CodeSkulptor
    but *not in CodeSkulptor documentation*!)

    :param sound_data: (tuple or list) of (0 <= int < 256)
    :param sample_rate: int >= 0
    :param num_channels: int >= 0

    :return: Sound
    """
    assert _PYGAME_AVAILABLE, """Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation"""

    assert isinstance(sound_data, tuple) or isinstance(sound_data, list), \
        type(sound_data)
    if __debug__:
        for data in sound_data:
            assert isinstance(data, int), type(data)
            assert 0 <= data < 256, data

    assert isinstance(sample_rate, int), type(sample_rate)
    assert sample_rate >= 0, sample_rate

    assert isinstance(num_channels, int), type(num_channels)
    assert num_channels >= 0, num_channels

    return Sound('')


def load_sound(url):
    """
    Create and return a sound by loading a file from `url`.
    Not founded URL and errors are ignored.

    SimpleGUICS2Pygame try **first** to loading sound
    from `Sound._dir_search_first` local directory (`_snd/` by default),
    and next if failed, try to loading from `url`.

    This local directory is relative to the directory of your program.

    For example,
    ``load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/jump.ogg')``
    try first to loading from
    ``_snd/commondatastorage.googleapis.com/codeskulptor_assets/jump.ogg``.

    Supported formats are supported formats by Pygame:
    OGG and uncompressed WAV
    (see http://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound ).

    (CodeSkulptor may supported also MP3,
    dependant on browser support.)

    (The sound can be started by `Sound.play()`.)

    :param url: str (**only a valid URL**, not local filename)

    :return: Sound
    """
    assert _PYGAME_AVAILABLE, """Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation"""

    assert isinstance(url, str), type(url)

    return Sound(url)
