#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test dir() content. (December 13, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

from sys import argv

try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    SIMPLEGUICS2PYGAME = True


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version
    from pygame.version import ver as pygame_version
    from SimpleGUICS2Pygame import _VERSION as GUI_VERSION

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    PYGAME_VERSION = 'Pygame ' + pygame_version
    GUI_VERSION = 'SimpleGUICS2Pygame ' + GUI_VERSION
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/
    PYGAME_VERSION = ''
    GUI_VERSION = 'simplegui'


TEST = 'test dir'


"""
Results of dir() in CodeSkulptor
"""
CODESKULPTOR_DIRS = {
    'simplegui': ('__name__',
                  'KEY_MAP',
                  'Canvas', 'Control', 'Frame', 'Image',
                  'Sound', 'TextAreaControl', 'Timer',
                  'create_frame', 'create_invisible_canvas',
                  'create_sound', 'create_timer',
                  'load_image', 'load_sound'),
    'Canvas': ('__init__', '__module__',
               'draw_circle', 'draw_image', 'draw_line',
               'draw_point', 'draw_polygon', 'draw_polyline', 'draw_text'),
    'Control': ('__init__', '__module__',
                'get_text', 'set_text'),
    'Frame': ('__init__', '__module__',
              'add_button', 'add_input', 'add_label',
              'get_canvas_image', 'get_canvas_textwidth',
              'set_canvas_background', 'set_draw_handler',
              'set_keydown_handler', 'set_keyup_handler',
              'set_mouseclick_handler', 'set_mousedrag_handler',
              'start', 'stop'),
    'Image': ('__init__', '__module__',
              'get_height', 'get_width'),
    'Sound': ('__init__', '__module__',
              'pause', 'play', 'rewind', 'set_volume'),
    'TextAreaControl': ('__init__', '__module__',
                        'get_text', 'set_text'),
    'Timer': ('__init__', '__module__',
              'get_interval', 'is_running', 'start', 'stop')}

"""
Results of dir() in this environment
"""
DIRS = {
    'simplegui': dir(simplegui),
    'Canvas': dir(simplegui.Canvas),
    'Control': dir(simplegui.Control),
    'Frame': dir(simplegui.Frame),
    'Image': dir(simplegui.Image),
    'Sound': dir(simplegui.Sound),
    'TextAreaControl': dir(simplegui.TextAreaControl),
    'Timer': dir(simplegui.Timer)}

"""
Sequence of elements to compare.
"""
LIST = ('simplegui',
        'Canvas', 'Control', 'Frame', 'Image',
        'Sound', 'TextAreaControl', 'Timer')


def print_cmp_seq(a, title_a,
                  b, title_b):
    """
    Compare two sequences and print difference.

    :param a: list or tuple
    :param title_a: str
    :param b: list or tuple
    :param title_b: str
    """
    assert isinstance(a, list) or isinstance(a, tuple), type(a)
    assert isinstance(title_a, str), title_a
    assert isinstance(b, list) or isinstance(b, tuple), type(b)
    assert isinstance(title_b, str), title_b

    ab = list(set(a).union(b))
    ab.sort()

    a_b = set(a).difference(b)
    b_a = set(b).difference(a)

    indent = max(max([len(i) for i in a]), len(title_a))

    head = ((title_a + ' '*indent)[:indent]
            + '\t!= ' + title_b + '\n' + '-'*(indent + 11 + len(title_b)))
    for i in ab:
        if (i[:2] == '__') and (i[-2:] == '__') and (i != '__init__'):
            continue
        if (len(argv) == 2) and (i[0] == '_'):
            continue

        if i in a_b:
            if head:
                print(head)
                head = None
            print(i)
        elif i in b_a:
            if head:
                print(head)
                head = None
            print(' '*indent + '\t   ' + i)

    if not head:
        print('')


# Main
print('List dir() differences between CodeSkulptor and this "Python":\n')

for k in LIST:
    print_cmp_seq(CODESKULPTOR_DIRS[k], 'CodeSkulptor ' + k,
                  DIRS[k], PYTHON_VERSION + ' ' + k)
