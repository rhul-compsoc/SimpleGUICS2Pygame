#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Blackjack (December 7, 2013)

My solution (slightly retouched) of the mini-project #6 of the course
https://www.coursera.org/course/interactivepython (Coursera 2013).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

import random

try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True


# Cards sprite 949x392 (source: www.jfitz.com/cards/ )
cards_image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png')
card_back = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png')


# Global constants
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)

CARD_SPACE = 5

FONT_SIZE = 40

FRAME_WIDTH = 800
FRAME_HEIGHT = 600

DEALER_POS = ((FRAME_WIDTH - CARD_SPACE)/2.0 - CARD_SIZE[0], 100)
PLAYER_POS = (DEALER_POS[0], 400)

GREEN = 'Green'
GREEN_LIGHT = '#40d040'
GREEN_DARK = '#007000'


# Global variables
deck = None

in_play = False

max_test_images_loaded = 20
nb_images_loaded = 0
nb_images_to_load = 2

outcome = None

score_dealer = 0
score_player = 0


# Helper functions
def assert_pos(pos):
    """
    Assertions to check valid position:
    (int or float, int or float) or [int or float, int or float]
    """
    assert isinstance(pos, tuple) or isinstance(pos, list), type(pos)
    assert len(pos) > 0, len(pos)

    assert isinstance(pos[0], int) or isinstance(pos[0], float), type(pos[0])
    assert pos[0] >= 0, pos

    assert isinstance(pos[1], int) or isinstance(pos[1], float), type(pos[1])
    assert pos[1] >= 0, pos


def draw_rect(canvas, pos, size, line_width, line_color, fill_color=None):
    """
    Draw a rectangle.

    :param canvas: simplegui.Canvas
    :param pos: (int or float, int or float) or [int or float, int or float]
    :param size: (int or float, int or float) or [int or float, int or float]
    :param line_width: int >= 0
    :param line_color: str
    :param fill_color: str
    """
    assert_pos(pos)
    assert_pos(size)
    assert isinstance(line_width, int) or isinstance(line_width, float), \
        type(line_width)
    assert line_width >= 0, line_width
    assert isinstance(line_color, str), type(str)
    assert (fill_color is None) or isinstance(fill_color, str), type(str)

    x0 = pos[0]
    y0 = pos[1]

    width = size[0] - 1
    height = size[1] - 1

    canvas.draw_polygon(((x0, y0),
                         (x0 + width, y0),
                         (x0 + width, y0 + height),
                         (x0, y0 + height)),
                        line_width, line_color, fill_color)


# Classes
class Card:
    """
    Card.
    """
    _VALUES = {'A': 1,
               '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'T': 10,
               'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, suit, rank):
        """
        Set a card.

        :param suit: str in Deck._SUITS
        :param rank: str in Deck._RANKS
        """
        assert isinstance(suit, str), type(suit)
        assert suit in Deck._SUITS, suit
        assert isinstance(rank, str), type(rank)
        assert rank in Deck._RANKS, rank

        self._suit = suit
        self._rank = rank

    def __str__(self):
        """
        Return a representation of card.

        :return: str
        """
        return self._suit + self._rank

    def draw(self, canvas, pos, hide):
        """
        Draw the card at the position.

        If hide
        then the first card are drawed face down.

        If the images cards_image or card_back are not loaded
        then draw rectangle instead.

        :param canvas: simplegui.Canvas
        :param pos: (int or float, int or float)
                      or [int or float, int or float]
        :param hide: bool
        """
        assert_pos(pos)
        assert isinstance(hide, bool), type(hide)

        drawed = False

        if hide:
            if card_back.get_width() > 0:
                canvas.draw_image(card_back,
                                  CARD_BACK_CENTER, CARD_BACK_SIZE,
                                  (pos[0] + CARD_BACK_CENTER[0],
                                   pos[1] + CARD_BACK_CENTER[1]), CARD_SIZE)
                drawed = True
        else:
            if cards_image.get_width() > 0:
                canvas.draw_image(
                    cards_image,
                    (CARD_CENTER[0]
                     + CARD_SIZE[0]*Deck._RANKS.index(self._rank),
                     CARD_CENTER[1]
                     + CARD_SIZE[1]*Deck._SUITS.index(self._suit)),
                    CARD_SIZE,
                    (pos[0] + CARD_CENTER[0],
                     pos[1] + CARD_CENTER[1]), CARD_SIZE)
                drawed = True

        if not drawed:
            draw_rect(canvas, pos, CARD_SIZE, 3, 'Black', ('Maroon' if hide
                                                           else 'White'))
            if not hide:
                s = str(self)
                canvas.draw_text(
                    s,
                    (pos[0] + (CARD_SIZE[0]
                               - frame.get_canvas_textwidth(s, size))/2.0,
                     pos[1] + CARD_SIZE[1]/2.0 + FONT_SIZE/4.0),
                    FONT_SIZE, ('Red' if self.get_suit() in ('H', 'D')
                                else 'Black'))

    def get_rank(self):
        """
        Return the rank of the card.

        :return: str
        """
        return self._rank

    def get_suit(self):
        """
        Return the suit of the card.

        :return: str
        """
        return self._suit

    def get_value(self):
        """
        Return the value of the card.

        :return: 1 <= int <= 10
        """
        return Card._VALUES[self._rank]


class Deck:
    """
    Deck.
    """
    _SUITS = ('C',  # Clubs (trèfle en français)
              'S',  # Spades (pique)
              'H',  # Heart (coeur)
              'D')  # Diamond (carreau)

    _RANKS = ('A',
              '2', '3', '4', '5', '6', '7', '8', '9',
              'T',  # ten
              'J',  # Jack (valet)
              'Q',  # Queen (dame)
              'K')  # King (roi)

    def __init__(self):
        """
        Set a deck, list of 52 classic cards.
        """
        self._cards = []

        for suit in Deck._SUITS:
            for rank in Deck._RANKS:
                self._cards.append(Card(suit, rank))

    def __str__(self):
        """
        Return the sequence of cards.

        :return: str
        """
        return ' '.join([str(card) for card in self._cards])

    def deal_card(self):
        """
        Return a card and remove of the deck.

        :return: Card
        """
        assert len(self._cards) > 0

        return self._cards.pop()

    def shuffle(self):
        """
        Shuffle the deck.
        """
        random.shuffle(self._cards)


class Hand:
    """
    Hand (of dealer or player).
    """
    def __init__(self, is_dealer=False):
        """
        Set an empty hand.

        :param is_dealer: bool
        """
        assert isinstance(is_dealer, bool), type(is_dealer)

        self._is_dealer = is_dealer
        self._cards = []

    def __str__(self):
        """
        Return the sequence of cards.

        :return: str
        """
        return ' '.join([str(card) for card in self._cards])

    def add_card(self, card):
        """
        Add the card in the hand.

        :param card: Card
        """
        assert isinstance(card, Card), type(card)

        self._cards.append(card)

    def draw(self, canvas, pos):
        """
        Draw all cards of the hand.

        :param canvas: simplegui.Canvas
        :param pos: (int or float, int or float)
                      or [int or float, int or float]
        """
        assert_pos(pos)

        if False:  # to debug
            canvas.draw_text(str(self.get_value()),
                             (pos[0] - 50, pos[1] + FONT_SIZE),
                             FONT_SIZE, 'Black')

        for i, card in enumerate(self._cards):
            card.draw(canvas, [pos[0] + i*(CARD_SIZE[0] + CARD_SPACE), pos[1]],
                      (i == 0) and self._is_dealer and in_play)

    def get_value(self):
        """
        Return value of the hand.

        :return: int >= 0
        """
        ace_founded = False

        v = 0
        for card in self._cards:
            v += card.get_value()
            if card.get_rank() == 'A':
                ace_founded = True

        return (v + 10 if ace_founded and (v + 10 <= 21)
                else v)


# Event handlers
def deal():
    """
    Start a new round.
    """
    global deck
    global hand_dealer
    global hand_player
    global in_play
    global outcome
    global score_dealer

    if in_play:
        score_dealer += 1
        outcome = 'YOU LOOSE!'
    else:
        in_play = True
        outcome = None

    deck = Deck()
    deck.shuffle()

    hand_dealer = Hand(True)
    hand_player = Hand()

    for i in range(2):
        hand_player.add_card(deck.deal_card())
        hand_dealer.add_card(deck.deal_card())


def draw(canvas):
    """
    Draw all the game.
    """
    canvas.draw_circle((FRAME_WIDTH/2.0,
                        FRAME_HEIGHT - FRAME_WIDTH*3/2.0 - 25),
                       FRAME_WIDTH*3/2.0, 50, '#803020', GREEN)

    canvas.draw_text('DEALER', (DEALER_POS[0], DEALER_POS[1] - 10),
                     FONT_SIZE, GREEN_LIGHT)

    canvas.draw_text('PLAYER', (PLAYER_POS[0], PLAYER_POS[1] - 10),
                     FONT_SIZE, GREEN_LIGHT)
    draw_rect(canvas,
              (PLAYER_POS[0] - CARD_SPACE, PLAYER_POS[1] - CARD_SPACE),
              (CARD_SIZE[0]*2 + CARD_SPACE*3, CARD_SIZE[1] + CARD_SPACE*2),
              2, GREEN_LIGHT, GREEN_DARK)

    canvas.draw_text('BLACKJACK', (20, 20 + FONT_SIZE*3/4.0), FONT_SIZE, 'Red')
    canvas.draw_text('BLACK', (20, 20 + FONT_SIZE*3/4.0), FONT_SIZE, 'Black')

    y = PLAYER_POS[1] - 70
    canvas.draw_line((20, y - FONT_SIZE - 10),
                     (FRAME_WIDTH - 20, y - FONT_SIZE - 10), 3, GREEN_LIGHT)
    canvas.draw_line((20, y), (FRAME_WIDTH - 20, y), 3, GREEN_LIGHT)

    s = ('HIT OR STAND?' if in_play
         else 'NEW DEAL?')
    canvas.draw_text(s,
                     ((FRAME_WIDTH
                       - frame.get_canvas_textwidth(s, FONT_SIZE))/2.0,
                      y - FONT_SIZE/4.0 - 3),
                     FONT_SIZE, GREEN_LIGHT)

    if outcome is not None:
        canvas.draw_text(
            outcome,
            ((FRAME_WIDTH
              - frame.get_canvas_textwidth(outcome, FONT_SIZE))/2.0,
             250), FONT_SIZE, 'WHITE')

    if deck is not None:
        s = 'SCORE: %d | %d' % (score_dealer, score_player)
        canvas.draw_text(s,
                         (FRAME_WIDTH
                          - frame.get_canvas_textwidth(s, FONT_SIZE)
                          - 20, 20 + FONT_SIZE*3/4.0),
                         FONT_SIZE, 'Black')

        hand_dealer.draw(canvas, DEALER_POS)
        hand_player.draw(canvas, PLAYER_POS)


def draw_wait_images(canvas):
    """
    Draw waiting message when images loading.
    """
    percent = nb_images_loaded*100.0/nb_images_to_load

    canvas.draw_line((0, 150), (FRAME_WIDTH, 150), 20, 'White')
    if percent > 0:
        canvas.draw_line((0, 150), (FRAME_WIDTH*percent/100.0, 150),
                         20, 'Green')

    size = 50
    canvas.draw_text('Loading... %d%%' % int(percent),
                     (10, 80 + size*3/4.0),
                     size, 'White')


def hit():
    """
    Give a new card to the player
    and deal his value.
    """
    global in_play
    global outcome
    global score_dealer

    outcome = None

    if in_play:
        hand_player.add_card(deck.deal_card())

        if hand_player.get_value() > 21:
            in_play = False
            outcome = 'YOU HAVE BUSTED'
            score_dealer += 1
    elif (deck is not None) and (hand_player.get_value() > 21):
        outcome = 'YOU HAVE BUSTED'


def stand():
    """
    The player stand.
    Deal the dealer logic and test who win.
    """
    global in_play
    global outcome
    global score_dealer
    global score_player

    outcome = None

    if in_play:
        while hand_dealer.get_value() < 17:
            hand_dealer.add_card(deck.deal_card())

        in_play = False

        if hand_player.get_value() <= hand_dealer.get_value() <= 21:
            outcome = 'YOU LOOSE'
            score_dealer += 1
        else:
            outcome = 'YOU WIN'
            score_player += 1
    elif (deck is not None) and (hand_player.get_value() > 21):
        outcome = 'YOU HAVE BUSTED'


def test_images_loaded():
    """
    Check the number of images already loaded.

    Global change: nb_images_loaded
                   nb_images_to_load
    """
    global max_test_images_loaded
    global nb_images_loaded
    global nb_images_to_load

    nb_images_loaded = sum([1 for img in [card_back, cards_image]
                            if img.get_width() > 0])

    if ((nb_images_loaded == nb_images_to_load)
            or (max_test_images_loaded <= 0)):
        timer.stop()
        frame.set_draw_handler(draw)

    max_test_images_loaded -= 1


# Main
if __name__ == '__main__':
    # Create frame
    frame = simplegui.create_frame('Blackjack', FRAME_WIDTH, FRAME_HEIGHT)

    # Control panel
    frame.add_button('Deal', deal, 200)
    frame.add_label('')
    frame.add_button('Hit',  hit, 200)
    frame.add_label('')
    frame.add_button('Stand', stand, 200)
    frame.add_label('')
    frame.add_label('')
    frame.add_button('Quit', frame.stop)

    # Register event handlers
    frame.set_draw_handler(draw_wait_images)

    timer = simplegui.create_timer(100, test_images_loaded)
    timer.start()
    test_images_loaded()

    frame.start()
