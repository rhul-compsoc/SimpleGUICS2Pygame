#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Memory (December 13, 2013)
  8 x (2 indentical cards)
  or 4 x (4 indentical cards)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

import random

try:
    import simplegui

    from user27_5LlszPPJxQHFMbk import assert_position
    from user23_HY71NDvHu7WKaMa import draw_rect
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    from SimpleGUICS2Pygame.codeskulptor_lib import assert_position
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_rect

    simplegui.Frame._hide_status = True


USE_IMAGES = True  # change to False to avoid images


# Globals variables
if USE_IMAGES:
    card_images = [
        simplegui.load_image(
            'http://www.opimedia.be/DS/SimpleGUICS2Pygame/stuff/Memory/img/'
            + filename)
        for filename in ('Guido_van_Rossum.jpg',
                         'Python.jpg',
                         'Joe_Warren.jpg',
                         'Scott_Rixner.jpg',
                         'John_Greiner.jpg',
                         'Stephen_Wong.jpg',
                         'CodeSkulptor.jpg',
                         'OPi.jpg',
                         'Memory.jpg')]
else:
    card_images = [simplegui.load_image('')]*9  # 9 failed images

memory = None  # the principal variable, instance of Memory

nb_images_loaded = 0
nb_test_images_loaded = 20


# Helper function
def draw_border(canvas, pos, size, line_width, color, shift=4):
    """
    Draw a rounded rectangle.

    :param canvas: simplegui.Canvas
    :param pos: (int or float, int or float) or [int or float, int or float]
    :param size: (int or float, int or float) or [int or float, int or float]
    :param line_width: int >= 0
    :param color: str
    :param shift: int
    """
    assert_position(pos)
    assert_position(size)
    assert isinstance(line_width, int) or isinstance(line_width, float), \
        type(line_width)
    assert line_width >= 0, line_width
    assert isinstance(color, str), type(str)
    assert isinstance(shift, int), type(shift)

    x0 = pos[0]
    y0 = pos[1]

    width = size[0] - 1
    height = size[1] - 1

    canvas.draw_polygon(((x0, y0 + shift),
                         (x0 + shift, y0),
                         (x0 + width - shift, y0),
                         (x0 + width, y0 + shift),
                         (x0 + width, y0 + height - shift),
                         (x0 + width - shift, y0 + height),
                         (x0 + shift, y0 + height),
                         (x0, y0 + height - shift)),
                        line_width, color)


# Classes
class Card:
    """
    A card (with an identification number and a drawing position).
    """
    WIDTH = 50
    HEIGHT = 100

    def __init__(self, num, image):
        """
        Initialize the card.

        :param num: int >= 0
        :param image: simplegui.Image
        """
        assert isinstance(num, int), type(num)
        assert num >= 0, num

        self.num = num
        self.image = image

        self.pos_x = 0
        self.pos_y = 0
        self.exposed = False
        self.selected = False

    def draw(self, canvas):
        """
        Draw the card.

        :param canvas: simplegui.canvas
        """
        if self.exposed:
            self.draw_recto(canvas)
        else:
            self.draw_verso(canvas)

    def draw_recto(self, canvas):
        """
        Draw recto of the card
        (card_images[self.num] images if loaded).

        :param canvas: simplegui.canvas
        """
        if self.image.get_width() > 0:  # draw image
            canvas.draw_image(self.image,
                              (self.image.get_width()/2.0,
                               self.image.get_height()/2.0),
                              (self.image.get_width(),
                               self.image.get_height()),
                              (self.pos_x + self.image.get_width()/2.0,
                               self.pos_y + self.image.get_height()/2.0),
                              (self.image.get_width(),
                               self.image.get_height()))
        else:                           # draw text number
            size = 50
            text = str(self.num)
            width = frame.get_canvas_textwidth(text, 50)
            canvas.draw_text(text,
                             (self.pos_x + (Card.WIDTH - width)//2,
                              self.pos_y + (Card.HEIGHT - size)/2.0
                              + size*3.0/4),
                             size, 'White')

        if self.selected or (self.image.get_width() == 0):
            draw_border(canvas,
                        (self.pos_x, self.pos_y), (Card.WIDTH, Card.HEIGHT),
                        3, ('Yellow' if self.selected
                            else 'White'))

    def draw_verso(self, canvas):
        """
        Draw verso of the card
        (card_images[-1] images if loaded).

        :param canvas: simplegui.canvas
        """
        img = card_images[-1]

        if img.get_width() > 0:  # draw image
            canvas.draw_image(img,
                              (img.get_width()/2.0, img.get_height()/2.0),
                              (img.get_width(), img.get_height()),
                              (self.pos_x + img.get_width()/2.0,
                               self.pos_y + img.get_height()/2.0),
                              (img.get_width(), img.get_height()))
        else:                    # draw simple rectangle
            canvas.draw_line((self.pos_x + Card.WIDTH/2.0 - 1,
                              self.pos_y),
                             (self.pos_x + Card.WIDTH/2.0 - 1,
                              self.pos_y + Card.HEIGHT - 1),
                             Card.WIDTH, 'Green')
            draw_rect(canvas,
                      (self.pos_x + 3, self.pos_y + 3),
                      (Card.WIDTH - 6, Card.HEIGHT - 6),
                      1, 'Red')

    def in_pos(self, pos):
        """
        If pos is in this card
        then return True,
        else return False.

        :param pos: (int or float, int or float)
                      or [int or float, int or float]

        :return: bool
        """
        assert_position(pos)

        return ((self.pos_x <= pos[0] < self.pos_x + Card.WIDTH)
                and (self.pos_y <= pos[1] < self.pos_y + Card.HEIGHT))


class Memory:
    """
    Memory game (list of cards)
    """
    def __init__(self, nb_different_cards=8, nb_repeat_cards=2):
        """
        Initialize the game.

        :param nb_different_cards: 0 < int <= len(card_images) - 2
        :param nb_repeat_cards: int > 0
        """
        assert isinstance(nb_different_cards, int), type(nb_different_cards)
        assert nb_different_cards > 0, nb_different_cards

        assert isinstance(nb_repeat_cards, int), type(nb_repeat_cards)
        assert 0 < nb_repeat_cards <= len(card_images) - 2, nb_repeat_cards

        assert nb_different_cards*nb_repeat_cards == 16, \
            (nb_different_cards, nb_repeat_cards)

        self.nb_different_cards = nb_different_cards
        self.nb_repeat_cards = nb_repeat_cards

        self.nb_moves = 0
        self.nb_founded = 0
        self.new_founded = False

        self.deck = [Card(i % nb_different_cards,
                          card_images[i % nb_different_cards])
                     for i in range(nb_different_cards*nb_repeat_cards)]
        random.shuffle(self.deck)

        for i, card in enumerate(self.deck):
            card.pos_x = 10 + \
                (i % (nb_different_cards*nb_repeat_cards//2))*(Card.WIDTH + 10)
            card.pos_y = 10 + \
                (i//(nb_different_cards*nb_repeat_cards//2))*(Card.HEIGHT + 10)

        self.selected_cards = []

        label_moves.set_text('Nb moves: 0')

    def draw(self, canvas):
        """
        Draw all cards.

        :param canvas: simplegui.canvas
        """
        for card in self.deck:
            card.draw(canvas)

    def expose(self, pos):
        """
        Expose the card pointed by position pos,
        and check if good cards are exposed.

        :param pos: (int or float, int or float)
                      or [int or float, int or float]
        """
        assert_position(pos)

        for card in self.deck:
            if card.in_pos(pos):  # this is the pointed card
                if not card.exposed:
                    if len(self.selected_cards) == self.nb_repeat_cards:
                        # Good number of exposed cards
                        # Reinit exposed cards
                        for c in self.selected_cards:
                            c.selected = False
                            if not self.new_founded:  # but not good cards
                                c.exposed = False

                        self.selected_cards = []

                    # Expose the pointed card
                    card.exposed = True
                    card.selected = True
                    self.selected_cards.append(card)

                    if len(self.selected_cards) == self.nb_repeat_cards:
                        # Good number of exposed cards
                        # Update the moves counter
                        self.nb_moves += 1
                        label_moves.set_text('Nb moves: ' + str(self.nb_moves))

                        # If all exposed cards and pointed card are the same
                        self.new_founded = all(
                            [c.num == self.selected_cards[0].num
                             for c in self.selected_cards[1:]])
                        if self.new_founded:  # good cards are exposed
                            self.nb_founded += 1
                            if self.nb_founded == self.nb_different_cards:
                                # Completed game
                                for c in self.selected_cards:
                                    c.selected = False

                break


# Event handlers
def draw(canvas):
    """
    Event handler to draw all cards.
    """
    memory.draw(canvas)


def draw_wait_images(canvas):
    """
    Draw waiting message when images loading.
    """
    percent = nb_images_loaded*100.0/len(card_images)

    canvas.draw_line((0, 150), (490, 150), 20, 'White')
    canvas.draw_line((0, 150), (490*percent/100.0, 150), 20, 'Green')

    size = 50
    canvas.draw_text('Loading... %d%%' % int(percent),
                     (10, 80 + size*30.0/4),
                     size, 'White')


def mouseclick(pos):
    """
    Event handler to deal clic on a card.
    """
    memory.expose(pos)


def restart_4x4():
    """
    Event handler to deal click on restart 4x4 button.

    Global change: memory
    """
    global memory

    label_game.set_text('4 x (4 indentical cards)')
    memory = Memory(4, 4)


def restart_8x2():
    """
    Event handler to deal click on restart 8x2 button.

    Global change: memory
    """
    global memory

    label_game.set_text('8 x (2 indentical cards)')
    memory = Memory(8, 2)


def start():
    """
    Event handler to deal start after loading images.
    """
    restart_8x2()

    frame.set_mouseclick_handler(mouseclick)
    frame.set_draw_handler(draw)


def test_images_loaded():
    """
    Check the number of images already loaded.

    Global change: nb_images_loaded
                   nb_test_images_loaded
    """
    global nb_images_loaded
    global nb_test_images_loaded

    nb_images_loaded = sum([1 for img in card_images if img.get_width() > 0])

    if (nb_test_images_loaded <= 0) or (nb_images_loaded == len(card_images)):
        timer.stop()
        start()

    nb_test_images_loaded -= 1


# Create frame
frame = simplegui.create_frame('Memory', 490, 230, 160)

# Control panel
label_game = frame.add_label('8x2 game')
label_moves = frame.add_label('Nb moves: 0')
frame.add_label('')
frame.add_button('Restart 8x2', restart_8x2)
frame.add_button('Restart 4x4', restart_4x4)
frame.add_label('')
frame.add_button('Quit', frame.stop)

# Register event handlers
frame.set_draw_handler(draw_wait_images)

timer = simplegui.create_timer(100, test_images_loaded)
timer.start()

test_images_loaded()


# Main
frame.start()
