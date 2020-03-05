#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame/_media (June 4, 2015)

Media helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import division
from __future__ import print_function


from io import BytesIO
from os import makedirs
from os.path import dirname, isdir, isfile, join, splitext
from re import sub
from sys import argv, stderr, version_info

if version_info[0] >= 3:
    from urllib.parse import urlsplit
    from urllib.request import urlopen
else:
    from urlparse import urlsplit
    from urllib2 import urlopen


__all__ = []


from SimpleGUICS2Pygame.simpleguics2pygame._pygame_lib import _PYGAME_AVAILABLE  # noqa
if _PYGAME_AVAILABLE:
    import pygame


#
# "Private" functions
#####################
def _load_local_media(type_of_media, filename):
    """
    Load an image or a sound from local file `filename`.

    **Don't use directly**,
    this function is use by `_LocalImage` and `_LocalSound` classes.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effects:

    * If the media is a valid sound\
      then init the pygame.mixer and set Sound._mixer_initialized to `True`.

    :param type_of_media: Image or Sound
    :param filename: str

    :return: pygame.Surface or pygame.mixer.Sound or None
    """
    assert type_of_media in ('Image', 'Sound'), type(type_of_media)
    assert isinstance(filename, str), type(filename)

    if not isfile(filename):
        return None

    media_is_image = (type_of_media == 'Image')

    from SimpleGUICS2Pygame.simpleguics2pygame.sound \
        import _MIXER_FREQUENCY, Sound

    if (not media_is_image) and (not Sound._mixer_initialized):
        Sound._mixer_initialized = True
        pygame.mixer.init(_MIXER_FREQUENCY)

    media = (pygame.image.load(filename) if media_is_image
             else pygame.mixer.Sound(filename))

    return media


def _load_media(type_of_media, url, local_dir):
    """
    Load an image or a sound from Web or local directory,
    and save if asked with Frame._save_downloaded_medias
    and Frame._save_downloaded_medias_overwrite.

    If local_dir don't exist it is created.

    **Don't use directly**,
    this function is use by `Image` and `Sound` classes.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effects:

    * Each new url is added to `Frame._pygamemedias_cached`.
    * If the media is a valid sound\
      then init the pygame.mixer and set Sound._mixer_initialized to `True`.
    * If `Frame._print_load_medias` then print loading informations to stderr.

    :param type_of_media: Image or Sound
    :param url: str
    :param local_dir: str

    :return: pygame.Surface or pygame.mixer.Sound or None
    """
    assert type_of_media in ('Image', 'Sound'), type(type_of_media)
    assert isinstance(url, str), type(url)
    assert isinstance(local_dir, str), type(local_dir)

    media_is_image = (type_of_media == 'Image')

    from SimpleGUICS2Pygame.simpleguics2pygame.frame import Frame
    from SimpleGUICS2Pygame.simpleguics2pygame.sound \
        import _MIXER_FREQUENCY, Sound

    cached = Frame._pygamemedias_cached.get(url)
    if cached is not None:  # Already in cache
        if (not media_is_image) and (not Sound._mixer_initialized):
            Sound._mixer_initialized = True
            pygame.mixer.init(_MIXER_FREQUENCY)

        media = (cached.copy() if media_is_image
                 else pygame.mixer.Sound(cached))
        if Frame._print_load_medias:
            print("{} '{}' got in cache".format(type_of_media, url),
                  file=stderr)
            stderr.flush()

        return media

    # Build a "normalized" filename
    filename = __normalized_filename(url, local_dir)

    # Check if is correct extension
    if not media_is_image and (filename[-4:].lower() not in ('.ogg', '.wav')):
        if Frame._print_load_medias:
            print("Sound format not supported '{}'".format(url),
                  file=stderr)
            stderr.flush()

        return None

    filename_exist = isfile(filename)

    # Load...
    if not Frame._save_downloaded_medias_overwrite and filename_exist:
        if (not media_is_image) and (not Sound._mixer_initialized):
            Sound._mixer_initialized = True
            pygame.mixer.init(_MIXER_FREQUENCY)

        try:
            # Load from local file
            media = (pygame.image.load(filename) if media_is_image
                     else pygame.mixer.Sound(filename))
            if Frame._print_load_medias:
                print("{} loaded '{}' instead '{}'".format(type_of_media,
                                                           filename, url),
                      file=stderr)
                stderr.flush()

            Frame._pygamemedias_cached[url] = media

            return media
        except Exception as exc:
            pass

    try:
        # Download from url
        media_data = urlopen(url).read()
        if Frame._print_load_medias:
            print("{} downloaded '{}'".format(type_of_media, url),
                  file=stderr)
            stderr.flush()
    except Exception as exc:
        if Frame._print_load_medias:
            print("{} downloading '{}' FAILED! {}".format(type_of_media,
                                                          url, exc),
                  file=stderr)
            stderr.flush()

        return None

    if (not media_is_image) and (not Sound._mixer_initialized):
        Sound._mixer_initialized = True
        pygame.mixer.init(_MIXER_FREQUENCY)

    try:
        media = (pygame.image.load(BytesIO(media_data)) if media_is_image
                 else pygame.mixer.Sound(BytesIO(media_data)))
    except Exception as exc:
        if Frame._print_load_medias:
            print("{} Pygame loading '{}' FAILED! {}".format(type_of_media,
                                                             url, exc),
                  file=stderr)
            stderr.flush()

        return None

    if Frame._save_downloaded_medias:
        if Frame._save_downloaded_medias_overwrite or not filename_exist:
            if not isdir(dirname(filename)):
                try:
                    # Create local directory
                    makedirs(dirname(filename))
                    if Frame._print_load_medias:
                        print("      Created '{}' directory"
                              .format(dirname(filename)),
                              file=stderr)
                except Exception as exc:
                    if Frame._print_load_medias:
                        print("      Creating '{}' directory FAILED!! {}"
                              .format(dirname(filename), exc),
                              file=stderr)

            try:
                # Save to local file
                outfile = open(filename, 'wb')
                outfile.write(media_data)
                outfile.close()
                if Frame._print_load_medias:
                    print("      {} in '{}'"
                          .format(('Overwritten' if filename_exist
                                   else 'Saved'), filename),
                          file=stderr)
            except Exception as exc:
                if Frame._print_load_medias:
                    print("      {} in '{}' FAILED! {}"
                          .format(('Overwriting' if filename_exist
                                   else 'Saving'), filename, exc),
                          file=stderr)
        elif Frame._print_load_medias:
            print("      Local file '{}' already exist"
                  .format(filename),
                  file=stderr)

    if Frame._print_load_medias:
        stderr.flush()

    Frame._pygamemedias_cached[url] = media

    return media


#
# Private functions
###################
def __normalized_filename(url, local_dir):
    """
    Build a "normalized" filename from url.

    :param url: str
    :param local_dir: str

    :return: str
    """
    assert isinstance(url, str), type(url)
    assert isinstance(local_dir, str), type(local_dir)

    urlsplitted = urlsplit(url)

    filename = join(dirname(argv[0]),
                    local_dir,
                    sub('[^._/0-9A-Za-z]', '_',
                        join(urlsplitted.netloc + '/',
                             urlsplitted.path[1:]).replace('\\', '/')))

    if urlsplitted.query != '':  # add "normalized" query part
        filename = list(splitext(filename))
        filename.insert(1, sub('[^._0-9A-Za-z]', '_', urlsplitted.query))
        filename = ''.join(filename)

    return filename
