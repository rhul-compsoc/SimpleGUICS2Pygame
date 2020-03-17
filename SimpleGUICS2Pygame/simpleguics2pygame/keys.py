# -*- coding: latin-1 -*-

"""
simpleguics2pygame/keys

Keys helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 17, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = ['KEY_MAP']


#
# Private global constants
##########################
__PYGAMEKEY_TO_SIMPLEGUIKEY = {97: 65,  # A or a
                               98: 66,  # ...
                               99: 67,
                               100: 68,
                               101: 69,
                               102: 70,
                               103: 71,
                               104: 72,
                               105: 73,
                               106: 74,
                               107: 75,
                               108: 76,
                               109: 77,
                               110: 78,
                               111: 79,
                               112: 80,
                               113: 81,
                               114: 82,
                               115: 83,
                               116: 84,
                               117: 85,
                               118: 86,
                               119: 87,
                               120: 88,
                               121: 89,   # ...
                               122: 90,   # Z or z
                               256: 96,   # 0 on numeric keypad
                               257: 97,   # ...
                               258: 98,   #
                               259: 99,   #
                               260: 100,  #
                               261: 101,  #
                               262: 102,  #
                               263: 103,  #
                               264: 104,  # ...
                               265: 105,  # 9 on numeric keypad
                               273: 38,   # Up
                               274: 40,   # Down
                               275: 39,   # Right
                               276: 37,   # Left
                               303: 17,   # Shift left
                               304: 17,   # Shitt right
                               305: 16,   # Ctrl left
                               306: 16,   # Ctrl right
                               307: 18,   # Alt left
                               308: 18}   # Alt right
"""
`Dict` {`int` Pygame key code : corresponding `int` SimpleGUI key code}.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


_SIMPLEGUIKEY_TO_STATUSKEY = {32: 'space',
                              37: 'Left',
                              38: 'Up',
                              39: 'Right',
                              40: 'Down',
                              48: '0',
                              49: '1',
                              50: '2',
                              51: '3',
                              52: '4',
                              53: '5',
                              54: '6',
                              55: '7',
                              56: '8',
                              57: '9',
                              65: 'a',
                              66: 'b',
                              67: 'c',
                              68: 'd',
                              69: 'e',
                              70: 'f',
                              71: 'g',
                              72: 'h',
                              73: 'i',
                              74: 'j',
                              75: 'k',
                              76: 'l',
                              77: 'm',
                              78: 'n',
                              79: 'o',
                              80: 'p',
                              81: 'q',
                              82: 'r',
                              83: 's',
                              84: 't',
                              85: 'u',
                              86: 'v',
                              87: 'w',
                              88: 'x',
                              89: 'y',
                              90: 'z'}
"""
`Dict` {`int` SimpleGUI key code : corresponding `str` status key}.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# Global constant
#################
KEY_MAP = {'space': 32,
           'left': 37,
           'up': 38,
           'right': 39,
           'down': 40,
           '0': 48,
           '1': 49,
           '2': 50,
           '3': 51,
           '4': 52,
           '5': 53,
           '6': 54,
           '7': 55,
           '8': 56,
           '9': 57,
           'A': 65,
           'B': 66,
           'C': 67,
           'D': 68,
           'E': 69,
           'F': 70,
           'G': 71,
           'H': 72,
           'I': 73,
           'J': 74,
           'K': 75,
           'L': 76,
           'M': 77,
           'N': 78,
           'O': 79,
           'P': 80,
           'Q': 81,
           'R': 82,
           'S': 83,
           'T': 84,
           'U': 85,
           'V': 86,
           'W': 87,
           'X': 88,
           'Y': 89,
           'Z': 90,
           'a': 65,
           'b': 66,
           'c': 67,
           'd': 68,
           'e': 69,
           'f': 70,
           'g': 71,
           'h': 72,
           'i': 73,
           'j': 74,
           'k': 75,
           'l': 76,
           'm': 77,
           'n': 78,
           'o': 79,
           'p': 80,
           'q': 81,
           'r': 82,
           's': 83,
           't': 84,
           'u': 85,
           'v': 86,
           'w': 87,
           'x': 88,
           'y': 89,
           'z': 90}
"""
SimpleGUI keyboard characters contants.
"""


#
# "Private" function
####################
def _pygamekey_to_simpleguikey(key):
    """
    Return the code use by SimpleGUI to representing
    the `key` expressed by Pygame.

    If `key` not in `__PYGAMEKEY_TO_SIMPLEGUIKEY`
    then return `key`.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param key: int >= 0

    :return: int >= 0
    """
    assert isinstance(key, int), type(key)
    assert key >= 0, key

    return __PYGAMEKEY_TO_SIMPLEGUIKEY.get(key, key)
