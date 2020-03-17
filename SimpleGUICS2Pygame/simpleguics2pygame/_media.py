# -*- coding: latin-1 -*-

"""
simpleguics2pygame/_media

Media (images and sounds) helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 14, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = []


from io import BytesIO  # noqa
from os import makedirs  # noqa
from os.path import dirname, isdir, isfile, join, splitext  # noqa
from re import sub  # noqa
from sys import argv, stderr, version_info  # noqa

if version_info[0] >= 3:
    from urllib.parse import urlsplit
    from urllib.request import urlopen
else:
    from urlparse import urlsplit  # pylint: disable=import-error
    from urllib2 import urlopen  # pylint: disable=import-error

from SimpleGUICS2Pygame.simpleguics2pygame._arguments import _CONFIG  # noqa  # pylint: disable=wrong-import-position,no-name-in-module

from SimpleGUICS2Pygame.simpleguics2pygame._pygame_init import _PYGAME_AVAILABLE  # noqa  # pylint: disable=no-name-in-module,wrong-import-position
if _PYGAME_AVAILABLE:
    import pygame


#
# Private global constant
#########################
_MIXER_FREQUENCY = 22050
"""
Sound frequency used by the mixer module of Pygame.
"""


_MIXER_INITIALIZED = False
"""
If `True`
then pygame.mixer is initialized.
"""


#
# Private global variables
##########################
_PRINT_LOAD_MEDIAS = _CONFIG['--print-load-medias']
"""
If `True`
then print URLs or locals filename loaded by `load_image()`
and `load_sound()`.
"""

__PYGAMEMEDIAS_CACHED = {}
"""
`Dict` {`str` URL: `pygame.Surface or pygame.mixer.Sound`}.
"""

_SAVE_DOWNLOADED_MEDIAS = _CONFIG['--save-downloaded-medias']
"""
If `True`
then save images and sounds downloaded from Web
that don't already exist in local directory.
See _SAVE_DOWNLOADED_MEDIAS_OVERWRITE.
"""

_SAVE_DOWNLOADED_MEDIAS_OVERWRITE = _CONFIG['--overwrite-downloaded-medias']
"""
If `True` and `_SAVE_DOWNLOADED_MEDIAS`
then download all images and sounds from Web
and save in local directory even if they already exist.
"""


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
      then init the pygame.mixer and set _MIXER_INITIALIZED to `True`.

    :param type_of_media: Image or Sound
    :param filename: str

    :return: pygame.Surface or pygame.mixer.Sound or None
    """
    global _MIXER_INITIALIZED  # pylint: disable=global-statement

    assert type_of_media in ('Image', 'Sound'), type(type_of_media)
    assert isinstance(filename, str), type(filename)

    if not _PYGAME_AVAILABLE or not isfile(filename):
        return None

    media_is_image = (type_of_media == 'Image')

    if (not media_is_image) and (not _MIXER_INITIALIZED):  # noqa  # pylint: disable=protected-access
        _MIXER_INITIALIZED = True  # pylint: disable=protected-access
        pygame.mixer.init(_MIXER_FREQUENCY)  # pylint: disable=protected-access

    media = (pygame.image.load(filename) if media_is_image
             else pygame.mixer.Sound(filename))

    return media


def _load_media(type_of_media, url, local_dir):  # noqa  # pylint: disable=too-many-branches,too-many-statements,too-many-return-statements
    """
    Load an image or a sound from Web or local directory,
    and save if asked with _SAVE_DOWNLOADED_MEDIAS
    and _SAVE_DOWNLOADED_MEDIAS_OVERWRITE.

    If local_dir don't exist it is created.

    **Don't use directly**,
    this function is use by `Image` and `Sound` classes.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effects:

    * Each new url is added to `__PYGAMEMEDIAS_CACHED`.
    * If the media is a valid sound\
      then init the pygame.mixer and set _MIXER_INITIALIZED to `True`.
    * If `_PRINT_LOAD_MEDIAS` then print loading informations to stderr.

    :param type_of_media: Image or Sound
    :param url: str
    :param local_dir: str

    :return: pygame.Surface or pygame.mixer.Sound or None
    """
    global _MIXER_INITIALIZED  # pylint: disable=global-statement

    assert type_of_media in ('Image', 'Sound'), type(type_of_media)
    assert isinstance(url, str), type(url)
    assert isinstance(local_dir, str), type(local_dir)

    if not _PYGAME_AVAILABLE:
        return None

    media_is_image = (type_of_media == 'Image')

    cached = __PYGAMEMEDIAS_CACHED.get(url)
    if cached is not None:
        # Already in cache
        if (not media_is_image) and (not _MIXER_INITIALIZED):  # noqa  # pylint: disable=protected-access
            _MIXER_INITIALIZED = True  # pylint: disable=protected-access
            pygame.mixer.init(_MIXER_FREQUENCY)

        media = (cached.copy() if media_is_image
                 else pygame.mixer.Sound(cached))
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print("{} '{}' got in cache".format(type_of_media, url),
                  file=stderr)
            stderr.flush()

        return media

    # Build a "normalized" filename
    filename = __normalized_filename(url, local_dir)

    # Check if is correct extension
    if not media_is_image and (filename[-4:].lower() not in ('.ogg', '.wav')):
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print("Sound format not supported '{}'".format(url),
                  file=stderr)
            stderr.flush()

        return None

    filename_exist = isfile(filename)

    # Load...
    if not _SAVE_DOWNLOADED_MEDIAS_OVERWRITE and filename_exist:
        if (not media_is_image) and (not _MIXER_INITIALIZED):
            _MIXER_INITIALIZED = True
            pygame.mixer.init(_MIXER_FREQUENCY)

        try:
            # Load from local file
            media = (pygame.image.load(filename) if media_is_image
                     else pygame.mixer.Sound(filename))
            if _PRINT_LOAD_MEDIAS:
                print("{} loaded '{}' instead '{}'".format(type_of_media,
                                                           filename, url),
                      file=stderr)
                stderr.flush()

            __PYGAMEMEDIAS_CACHED[url] = media

            return media
        except Exception as exc:  # pylint: disable=broad-except
            pass

    try:
        # Download from url
        media_data = urlopen(url).read()
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print("{} downloaded '{}'".format(type_of_media, url),
                  file=stderr)
            stderr.flush()
    except Exception as exc:  # pylint: disable=broad-except
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print("{} downloading '{}' FAILED! {}".format(type_of_media,
                                                          url, exc),
                  file=stderr)
            stderr.flush()

        return None

    if (not media_is_image) and (not _MIXER_INITIALIZED):  # noqa  # pylint: disable=protected-access
        _MIXER_INITIALIZED = True  # pylint: disable=protected-access
        pygame.mixer.init(_MIXER_FREQUENCY)

    try:
        media = (pygame.image.load(BytesIO(media_data)) if media_is_image
                 else pygame.mixer.Sound(BytesIO(media_data)))
    except Exception as exc:  # pylint: disable=broad-except
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print("{} Pygame loading '{}' FAILED! {}".format(type_of_media,
                                                             url, exc),
                  file=stderr)
            stderr.flush()

        return None

    if _SAVE_DOWNLOADED_MEDIAS:
        if _SAVE_DOWNLOADED_MEDIAS_OVERWRITE or not filename_exist:
            if not isdir(dirname(filename)):
                try:
                    # Create local directory
                    makedirs(dirname(filename))
                    if _PRINT_LOAD_MEDIAS:  # noqa  # pylint: disable=protected-access
                        print("      Created '{}' directory"
                              .format(dirname(filename)),
                              file=stderr)
                except Exception as exc:  # pylint: disable=broad-except
                    if _PRINT_LOAD_MEDIAS:  # noqa  # pylint: disable=protected-access
                        print("      Creating '{}' directory FAILED!! {}"
                              .format(dirname(filename), exc),
                              file=stderr)

            try:
                # Save to local file
                outfile = open(filename, 'wb')
                outfile.write(media_data)
                outfile.close()
                if _PRINT_LOAD_MEDIAS:  # noqa  # pylint: disable=protected-access
                    print("      {} in '{}'"
                          .format(('Overwritten' if filename_exist
                                   else 'Saved'), filename),
                          file=stderr)
            except Exception as exc:  # pylint: disable=broad-except
                if _PRINT_LOAD_MEDIAS:  # noqa  # pylint: disable=protected-access
                    print("      {} in '{}' FAILED! {}"
                          .format(('Overwriting' if filename_exist
                                   else 'Saving'), filename, exc),
                          file=stderr)
        elif _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print("      Local file '{}' already exist"
                  .format(filename),
                  file=stderr)

    if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
        stderr.flush()

    __PYGAMEMEDIAS_CACHED[url] = media

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
        pieces = list(splitext(filename))
        pieces.insert(1, sub('[^._0-9A-Za-z]', '_', urlsplitted.query))
        filename = ''.join(pieces)

    return filename
