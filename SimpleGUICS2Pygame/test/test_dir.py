#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test dir() content. (March 5, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2015, 2020 Olivier Pirson
http://www.opimedia.be/
"""

from sys import argv

try:
    import simplegui
    import codeskulptor
    import numeric
    import simpleplot

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
    import SimpleGUICS2Pygame.numeric as numeric
    import SimpleGUICS2Pygame.simpleplot as simpleplot

    SIMPLEGUICS2PYGAME = True


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/


TEST = 'test dir'


CODESKULPTOR_DIRS = {
    'codeskulptor': ('__name__',
                     'file2url', 'set_timeout'),

    'numeric': ('__name__',
                'identity',
                'Matrix'),
    'numeric.Matrix': ('__init__',
                       '__add__', '__getitem__', '__module__', '__mul__',
                       '__setitem__', '__str__', '__sub__',
                       'abs', 'copy', 'getcol', 'getrow', 'inverse', 'scale',
                       'shape', 'summation', 'transpose'),

    'simplegui': ('__name__',
                  'KEY_MAP',
                  'Canvas', 'Control', 'Frame', 'Image',
                  'Sound', 'TextAreaControl', 'Timer',
                  'create_frame', 'create_invisible_canvas',
                  'create_sound', 'create_timer',
                  'load_image', 'load_sound'),
    'simplegui.Canvas': ('__init__', '__module__',
                         'draw_circle', 'draw_image', 'draw_line',
                         'draw_point', 'draw_polygon', 'draw_polyline',
                         'draw_text'),
    'simplegui.Control': ('__init__', '__module__',
                          'get_text', 'set_text'),
    'simplegui.Frame': ('__init__', '__module__',
                        'add_button', 'add_input', 'add_label',
                        'get_canvas_image', 'get_canvas_textwidth',
                        'set_canvas_background', 'set_draw_handler',
                        'set_keydown_handler', 'set_keyup_handler',
                        'set_mouseclick_handler', 'set_mousedrag_handler',
                        'start', 'stop'),
    'simplegui.Image': ('__init__', '__module__',
                        'get_height', 'get_width'),
    'simplegui.Sound': ('__init__', '__module__',
                        'pause', 'play', 'rewind', 'set_volume'),
    'simplegui.TextAreaControl': ('__init__', '__module__',
                                  'get_text', 'set_text'),
    'simplegui.Timer': ('__init__', '__module__',
                        'get_interval', 'is_running', 'start', 'stop'),

    'simpleplot': ('__name__',
                   'plot_bars', 'plot_lines', 'plot_scatter')}
"""
Results of dir() in CodeSkulptor
"""

DIRS = {
    'codeskulptor': dir(codeskulptor),

    'numeric': dir(numeric),
    'numeric.Matrix': dir(numeric.Matrix),

    'simplegui': dir(simplegui),
    'simplegui.Canvas': dir(simplegui.Canvas),
    'simplegui.Control': dir(simplegui.Control),
    'simplegui.Frame': dir(simplegui.Frame),
    'simplegui.Image': dir(simplegui.Image),
    'simplegui.Sound': dir(simplegui.Sound),
    'simplegui.TextAreaControl': dir(simplegui.TextAreaControl),
    'simplegui.Timer': dir(simplegui.Timer),

    'simpleplot': dir(simpleplot)}
"""
Results of dir() in this environment
"""

assert set(CODESKULPTOR_DIRS.keys()) == set(DIRS.keys())


different = False
"""
`True` if founded a difference,
else `False`.
"""


def print_cmp_seq(a, title_a,
                  b, title_b):
    """
    Compare two sequences and print difference.

    :param a: list or tuple
    :param title_a: str
    :param b: list or tuple
    :param title_b: str
    """
    global different

    assert isinstance(a, list) or isinstance(a, tuple), type(a)
    assert isinstance(title_a, str), title_a
    assert isinstance(b, list) or isinstance(b, tuple), type(b)
    assert isinstance(title_b, str), title_b

    ab = list(set(a).union(b))
    ab.sort()

    a_b = set(a).difference(b)
    b_a = set(b).difference(a)

    indent = max(max([len(i) for i in a]), len(title_a))

    head = ((title_a + ' ' * indent)[:indent] +
            '\t!= ' + title_b + '\n' + '-' * (indent + 11 + len(title_b)))
    for name in ab:
        if name in a_b:
            if head:
                print(head)
                head = None
            print(name)
            different = True
        elif name in b_a:
            if ((name != '__init__') and
                    (name[:2] == '__') and (name[-2:] == '__')):
                # Exclude additional special functions
                continue

            if ((len(argv) == 2) and
                    ((name[0] == '_') or
                     (name in ('division', 'matplotlib',
                               'print_function', 'pygame')))):
                # Exclude additional private functions and local directives
                continue

            if head:
                print(head)
                head = None
            print(' ' * indent + '\t   ' + name)
            different = True

    if not head:
        print('')


# Main
print('List dir() differences between CodeSkulptor (January 2015) and this "Python":\n')  # noqa

for k in sorted(CODESKULPTOR_DIRS.keys()):
    print_cmp_seq(CODESKULPTOR_DIRS[k], 'CodeSkulptor ' + k,
                  DIRS[k], PYTHON_VERSION + ' ' + k)

if not different:
    print('No difference.')
