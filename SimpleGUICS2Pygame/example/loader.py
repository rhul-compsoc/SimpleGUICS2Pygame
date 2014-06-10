#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Example of simplegui_lib_loader.Loader use. (June 10, 2014)

Documentation:
https://simpleguics2pygame.readthedocs.org/en/latest/simplegui_lib_loader.html

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui

    from user34_7pdNdCOBbyLqAZs import Loader
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader

    simplegui.Frame._hide_status = True


WIDTH = 400
HEIGHT = 200


def draw(canvas):
    """
    The real draw handler function.

    :param canvas: simplegui.Canvas
    """
    img = loader.get_image('asteroid')  # get an image by its name
    canvas.draw_image(img,
                      (img.get_width()/2, img.get_height()/2),
                      (img.get_width(), img.get_height()),
                      (img.get_width()/2, img.get_height()/2),
                      (img.get_width(), img.get_height()))

    img = loader.get_image('double_ship')  # get an image by its name
    canvas.draw_image(img,
                      (img.get_width()/2, img.get_height()/2),
                      (img.get_width(), img.get_height()),
                      (img.get_width()/2, img.get_height()/2 + 100),
                      (img.get_width(), img.get_height()))


# Main
frame = simplegui.create_frame('Loader example', WIDTH, HEIGHT, 50)


def init():
    """
    Init function called after image loaded.
    """
    # Init your stuff...
    frame.add_button('Quit', quit_prog)

    music = loader.get_sound('soundtrack')  # get a sound by its name
    music.play()

    snd = loader.get_sound('explosion')  # get a sound by its name
    snd.play()

    # Medias failed
    img = loader.get_image('incorrect url')  # get an image by its name

    assert img.get_width() == 0, img.get_width()

    snd = loader.get_sound('incorrect url')  # get a sound by its name
    snd.play()

    # Set the real draw handler
    frame.set_draw_handler(draw)


def quit_prog():
    """
    Stop sounds and frame
    """
    loader.pause_sounds()  # stop all sounds
    frame.stop()
    if frame._print_stats_cache:
        loader.print_stats_cache()


loader = Loader(frame,  # the frame
                WIDTH,  # the width frame
                init)   # the function to call after loading

# Specified images to load with its URL and give them a name.
loader.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png',
                 'asteroid')
loader.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png',
                 'double_ship')
loader.add_image('xxx',
                 'incorrect url')

# Specified sounds to load with its URL and give them a name.
loader.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.ogg',
                 'explosion')
loader.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.ogg',
                 'soundtrack')
loader.add_sound('xxx',
                 'incorrect url')


# Start loading images and sounds:
# - In standard Python with SimpleGUICS2Pygame:
#   draw a progression bar on canvas and wait until the loading is finished.
# - In SimpleGUI of CodeSkulptor: *don't* wait.
loader.load()

# Draw a progression bar on canvas
# and wait until all images and sounds are fully loaded.
# Then execute the function specified by Loader().
# (Abort if times out.)
loader.wait_loaded()

frame.start()
