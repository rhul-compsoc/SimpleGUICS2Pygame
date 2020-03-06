#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Spaceship prototype (March 6, 2020)

My retouched solution of the mini-project #7 of the MOOC
https://www.coursera.org/learn/interactive-python-2 (Coursera 2013).

Run on:
  - Chrome 31
  - Firefox 26
  - Safari 5.1.7 (without sounds).
  - and Python 2 and 3 with SimpleGUICS2Pygame.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2015, 2020 Olivier Pirson
http://www.opimedia.be/
"""

import math
import random

try:
    from user38_ZmhOVHGm2lhVRhk import assert_position
    from user33_Bhc7VzXKbXGVQV1 import FPS
    from user40_nMs7JxzimyImAv2 import Loader

    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    from SimpleGUICS2Pygame.codeskulptor_lib import assert_position
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access

    SIMPLEGUICS2PYGAME = True


#
# Global constants
###################
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#
# Global variables
###################
FRAME = None

KEYDOWN_LEFT = False
KEYDOWN_RIGHT = False

LIVES = 3

LOADER = None

SCORE = 0

TIME = 0.5

TIMER = None


# Sprites and (ship)
A_MISSILE = None

A_ROCK = None

MY_SHIP = None


#
# Helper function
##################
def angle_to_vector(angle):
    """
    Return the vector corresponding to the angle expressed in radians.

    :param angle: int or float

    :return: (-1 <= float <= 1, -1 <= float <= 1)
    """
    return (math.cos(angle), math.sin(angle))


#
# Classes
##########
class ImageInfo:
    """
    Informations to use with Sprite.
    """
    def __init__(self, center, size,  # pylint: disable=too-many-arguments
                 radius=None, lifespan=None, animated=False):
        """
        Set informations.

        If radius is None
        then use maximum of size components.

        :param center: (int or float, int or float)
                       or [int or float, int or float]
        :param size: ((int or float) > 0, (int or float) > 0)
                     or [(int or float) > 0, (int or float) > 0]
        :param radius: None or ((int or float) > 0)
        :param lifespan: None or ((int or float) > 0)
        :param animated: bool
        """
        assert_position(center)
        assert_position(size, True, True)
        assert ((radius is None) or
                ((isinstance(radius, int) or isinstance(radius, float)) and
                 (radius > 0))), radius
        assert ((lifespan is None) or
                ((isinstance(lifespan, int) or isinstance(lifespan, float)) and
                 (lifespan > 0))), lifespan
        assert isinstance(animated, bool), type(animated)

        self._center = list(center)
        self._size = list(size)
        self._radius = (max(size) if radius is None
                        else radius)
        self._lifespan = (lifespan if lifespan
                          else float('inf'))
        self._animated = animated

    def get_animated(self):
        """
        If is a animated image
        then return True,
        else return False.

        :return: bool
        """
        return self._animated

    def get_center(self):
        """
        Return position of the center of image.

        :return: [int or float, int or float]
        """
        return self._center

    def get_lifespan(self):
        """
        Return lifespan of image.

        :return: None or ((int or float) > 0)
        """
        return self._lifespan

    def get_radius(self):
        """
        Return radius of image.

        :return: (int or float) > 0
        """
        return self._radius

    def get_size(self):
        """
        Return size of image.

        :return: [(int or float) > 0, (int or float) > 0]
        """
        return self._size


class Sprite:  # pylint: disable=too-many-instance-attributes
    """
    Sprite class
    """
    def __init__(self, position,  # pylint: disable=too-many-arguments
                 velocity, angle,
                 angle_velocity,
                 image, image_info,
                 sound=None):
        """
        Set sprite.

        :param position: (int or float, int or float)
                         or [int or float, int or float]
        :param velocity: (int or float, int or float)
                         or [int or float, int or float]
        :param angle: int or float
        :param image: simplegui.Image
        :param image_info: ImageInfo
        :param sound: simplegui.Sound
        """
        assert_position(position)
        assert_position(velocity)
        assert isinstance(angle, int) or isinstance(angle, float), type(angle)
        assert (isinstance(angle_velocity, int) or
                isinstance(angle_velocity, float)), type(angle_velocity)
        assert isinstance(image_info, ImageInfo), type(image_info)

        self.position = list(position)
        self.velocity = list(velocity)
        self.angle = angle
        self.angle_velocity = angle_velocity
        self.image = image

        self.image_center = image_info.get_center()
        self.image_size = image_info.get_size()
        self.radius = image_info.get_radius()

        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        """
        Draw the sprite
        (if the associated image are not loaded, draw a red disc).
        """
        if self.image.get_width() > 0:
            canvas.draw_image(self.image,
                              self.image_center, self.image_size,
                              self.position, self.image_size,
                              self.angle)
        else:
            canvas.draw_circle(self.position, self.radius, 1, 'Red', 'Red')

    def update(self):
        """
        Update position adding velocity,
        and angle adding angle_velocity.
        """
        self.angle += self.angle_velocity

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]


class Ship(Sprite):
    """
    Ship class
    """
    def __init__(self, position,  # pylint: disable=too-many-arguments
                 velocity, angle,
                 image, image_info):
        """
        Set ship sprite.

        :param position: (int or float, int or float)
                         or [int or float, int or float]
        :param velocity: (int or float, int or float)
                         or [int or float, int or float]
        :param angle: int or float
        :param image: simplegui.Image
        :param image_info: ImageInfo
        """
        assert_position(position)
        assert_position(velocity)
        assert isinstance(angle, int) or isinstance(angle, float), type(angle)
        assert isinstance(image_info, ImageInfo), type(image_info)

        Sprite.__init__(self, position, velocity, angle,
                        0,
                        image, image_info)

        self.thrust = False

    def shot(self):  # pylint: disable=no-self-use
        """
        Launch a missile.
        """
        global A_MISSILE  # pylint: disable=global-statement

        vector = angle_to_vector(MY_SHIP.angle)

        A_MISSILE = Sprite((MY_SHIP.position[0] + MY_SHIP.radius * vector[0],
                            MY_SHIP.position[1] + MY_SHIP.radius * vector[1]),
                           (MY_SHIP.velocity[0] + vector[0] * 10,
                            MY_SHIP.velocity[1] + vector[1] * 10),
                           0, 0,
                           LOADER.get_image('missile'), MISSILE_INFO,
                           LOADER.get_sound('missile'))

    def thrust_on_off(self):
        """
        Switch activation of thrust.
        """
        self.thrust = not self.thrust

        if self.thrust:
            LOADER.get_sound('ship_thrust').play()
            # Sprite image with actif thrust
            self.image_center[0] += self.image_size[0]
        else:
            LOADER.get_sound('ship_thrust').rewind()
            # Sprite image with inactif thrust
            self.image_center[0] -= self.image_size[0]

    def turn(self, angle_move):  # pylint: disable=no-self-use
        """
        Turn the ship
        (in fact change angle_velocity).

        :param angle_move: int or float
        """
        assert isinstance(angle_move, int) or isinstance(angle_move, float), \
            type(angle_move)

        MY_SHIP.angle_velocity = angle_move

    def update(self):
        """
        Update position adding velocity (and deal exit out of the canvas),
        decrease slightly velocity,
        and angle adding angle_velocity.

        Moreover if thrust is active then increase velocity.
        """
        self.angle += self.angle_velocity

        if self.thrust:
            acceleration = angle_to_vector(self.angle)
            self.velocity[0] += acceleration[0] * 0.25
            self.velocity[1] += acceleration[1] * 0.25

        self.velocity[0] *= .98
        self.velocity[1] *= .98

        self.position = ((self.position[0] + self.velocity[0]) % SCREEN_WIDTH,
                         (self.position[1] + self.velocity[1]) % SCREEN_HEIGHT)


#
# Event handlers
#################
def draw(canvas):
    """
    Draw all stuffs.

    :param canvas: simplegui.Canvas
    """
    global TIME  # pylint: disable=global-statement

    # Draw static background
    if not SIMPLEGUICS2PYGAME:
        canvas.draw_image(LOADER.get_image('nebula'),
                          NEBULA_INFO.get_center(), NEBULA_INFO.get_size(),
                          (SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0),
                          (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Draw animated background
    TIME += 1
    wtime = (TIME / 4.0) % SCREEN_WIDTH
    center = DEBRIS_INFO.get_center()
    size_xy = DEBRIS_INFO.get_size()

    canvas.draw_image(LOADER.get_image('debris'),
                      center, size_xy,
                      (wtime - SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0),
                      (SCREEN_WIDTH, SCREEN_HEIGHT))
    canvas.draw_image(LOADER.get_image('debris'),
                      center, size_xy,
                      (wtime + SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0),
                      (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Display number of lives
    size = 30
    font = 'sans-serif'

    canvas.draw_text('Lives', (20, 20 + size * 3.0 / 4), size, 'White', font)
    canvas.draw_text(str(LIVES), (20, 20 + size * 7.0 / 4),
                     size, 'White', font)

    # Display score
    text = 'Score'
    width = FRAME.get_canvas_textwidth(text, size, font)
    canvas.draw_text(text, (SCREEN_WIDTH - 20 - width, 20 + size * 3.0 / 4),
                     size, 'White', font)

    text = str(SCORE)
    width = FRAME.get_canvas_textwidth(text, size, font)
    canvas.draw_text(text, (SCREEN_WIDTH - 20 - width, 20 + size * 7.0 / 4),
                     size, 'White', font)

    # Draw ship and sprites
    MY_SHIP.draw(canvas)

    if A_ROCK is not None:
        A_ROCK.draw(canvas)

    if A_MISSILE is not None:
        A_MISSILE.draw(canvas)

    # Update ship and sprites
    MY_SHIP.update()

    if A_ROCK is not None:
        A_ROCK.update()

    if A_MISSILE is not None:
        A_MISSILE.update()

    # Update and draw FPS (if started)
    FPS_DRAWER.draw_fct(canvas)


def fps_on_off():
    """
    Active or inactive the calculation and drawing of FPS.
    """
    if FPS_DRAWER.is_started():
        FPS_DRAWER.stop()
        button_fps.set_text('FPS on')
    else:
        FPS_DRAWER.start()
        button_fps.set_text('FPS off')


def keydown(key):
    """
    Event handler to deal key down.

    :param key: int >= 0
    """
    global KEYDOWN_LEFT  # pylint: disable=global-statement
    global KEYDOWN_RIGHT  # pylint: disable=global-statement

    if key == simplegui.KEY_MAP['left']:
        KEYDOWN_LEFT = True
        MY_SHIP.angle_velocity = -.05
    elif key == simplegui.KEY_MAP['right']:
        KEYDOWN_RIGHT = True
        MY_SHIP.angle_velocity = .05
    elif key == simplegui.KEY_MAP['up']:
        MY_SHIP.thrust_on_off()
    elif key == simplegui.KEY_MAP['space']:
        MY_SHIP.shot()


def keyup(key):
    """
    Event handler to deal key up.

    :param key: int >= 0
    """
    global KEYDOWN_LEFT  # pylint: disable=global-statement
    global KEYDOWN_RIGHT  # pylint: disable=global-statement

    if key == simplegui.KEY_MAP['left']:
        KEYDOWN_LEFT = False
        MY_SHIP.turn(0.05 if KEYDOWN_RIGHT
                     else 0)
    elif key == simplegui.KEY_MAP['right']:
        KEYDOWN_RIGHT = False
        MY_SHIP.turn(-0.05 if KEYDOWN_LEFT
                     else 0)
    elif key == simplegui.KEY_MAP['up']:
        MY_SHIP.thrust_on_off()


def quit_prog():
    """
    Stop timer and sounds, and quit.
    """
    TIMER.stop()
    LOADER.pause_sounds()
    FRAME.stop()
    if SIMPLEGUICS2PYGAME and FRAME._print_stats_cache:  # noqa  # pylint: disable=protected-access
        LOADER.print_stats_cache()


def rock_spawner():
    """
    Timer handler that spawns a rock.
    """
    global A_ROCK  # pylint: disable=global-statement

    A_ROCK = Sprite((random.randrange(SCREEN_WIDTH // 16,
                                      SCREEN_WIDTH * 15 // 16),
                     random.randrange(SCREEN_HEIGHT // 16,
                                      SCREEN_HEIGHT * 15 // 16)),
                    (random.randrange(2, 7) * random.choice((-1, 1)),
                     random.randrange(2, 7) * random.choice((-1, 1))),
                    (random.random() - 0.5) * math.pi,
                    (random.random() - 0.5) / 10.0,
                    LOADER.get_image('asteroid'), ASTEROID_INFO)


def start():
    """
    Start the game.
    """
    global TIMER  # pylint: disable=global-statement

    if SIMPLEGUICS2PYGAME:
        FRAME._set_canvas_background_image(LOADER.get_image('nebula'))  # noqa  # pylint: disable=protected-access

    FRAME.set_draw_handler(draw)

    TIMER = simplegui.create_timer(1000, rock_spawner)
    TIMER.start()
    rock_spawner()


#
# Main
#######
if __name__ == '__main__':
    # Create frame
    FRAME = simplegui.create_frame('Spaceship prototype',
                                   SCREEN_WIDTH, SCREEN_HEIGHT, 100)

    # Create FPS
    FPS_DRAWER = FPS()

    # Load medias
    LOADER = Loader(FRAME, SCREEN_WIDTH, start)

    # Images by Kim Lathrop
    LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png',  # noqa
                     'asteroid')
    LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png',  # noqa
                     'debris')
    LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png',  # noqa
                     'missile')
    LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png',  # noqa
                     'nebula')
    LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png',  # noqa
                     'ship')

    ASTEROID_INFO = ImageInfo((45, 45), (90, 90), 40)
    DEBRIS_INFO = ImageInfo((320, 240), (640, 480))
    MISSILE_INFO = ImageInfo((5, 5), (10, 10), 3, 50)
    NEBULA_INFO = ImageInfo((400, 300), (800, 600))
    SHIP_INFO = ImageInfo((45, 45), (90, 90), 35)

    # Sounds from http://www.sounddogs.com/ (not free)
    LOADER.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.ogg',  # noqa
                     'missile')
    LOADER.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.ogg',  # noqa
                     'ship_thrust')

    LOADER.load()

    # Initialize ship and rock
    MY_SHIP = Ship((0, SCREEN_HEIGHT / 2.0), (10, 0),
                   0, LOADER.get_image('ship'), SHIP_INFO)

    # Register event handlers
    FRAME.set_keydown_handler(keydown)
    FRAME.set_keyup_handler(keyup)

    button_fps = FRAME.add_button('FPS on', fps_on_off)
    FRAME.add_label('')
    FRAME.add_button('Quit', quit_prog)

    LOADER.wait_loaded()

    LOADER.get_sound('missile').set_volume(.5)

    FRAME.start()
