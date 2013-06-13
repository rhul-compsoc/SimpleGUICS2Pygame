#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
simpleguics2pygame

It is a standard Python_ (2 **and** 3) module
reimplementing the SimpleGUI particular module of CodeSkulptor_
(a browser Python interpreter).

Require Pygame_
(except for the Timer class)
(`Unofficial Windows Binaries`_).

| Piece of SimpleGUICS2Pygame.
| https://bitbucket.org/OPiMedia/simpleguics2pygame

| GPLv3 --- Copyright (C) 2013 Olivier Pirson
| http://www.opimedia.be/

Module started on May 21, 2013

v.00.90.00 --- June 13, 2013

.. _CodeSkulptor: http://www.codeskulptor.org/
.. _Pygame: http://www.pygame.org/
.. _Python: http://www.python.org/
.. _`Unofficial Windows Binaries`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
"""

from __future__ import division

_VERSION = '00.90.00'
"""
Version of simpleguics2pygame module.
"""

_WEBSITE = 'https://bitbucket.org/OPiMedia/simpleguics2pygame'
"""
Website of the project.
"""

#
# GPLv3
# ------
# Copyright (C) 2013 Olivier Pirson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#



try:
    from pygame.version import ver as _PYGAME_VERSION

    _PYGAME_AVAILABLE = True
    """
    `True` if Pygame is available,
    else `False`.
    """
except:
    _PYGAME_AVAILABLE = False

    _PYGAME_VERSION = None
    """
    `pygame.version` if Pygame is available,
    else `None`.
    """


if _PYGAME_AVAILABLE:
    import pygame
    import pygame.font
    import pygame.mixer
    import pygame.transform

    pygame.mixer.init(44100)

    pygame.display.init()
    pygame.font.init()



#
# Private global constants
###########################
_PYGAMEKEY_TO_SIMPLEGUIKEY = { 97: 65,  # A or a
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
                              121: 89,  # ...
                              122: 90,  # Z or z
                              256:  96,  # 0 on numeric keypad
                              257:  97,  # ...
                              258:  98,  #
                              259:  99,  #
                              260: 100,  #
                              261: 101,  #
                              262: 102,  #
                              263: 103,  #
                              264: 104,  # ...
                              265: 105,  # 9 on numeric keypad
                              273: 38,  # Up
                              274: 40,  # Down
                              275: 39,  # Right
                              276: 37,  # Left
                              303: 17,  # Shift left
                              304: 17,  # Shitt right
                              305: 16,  # Ctrl left
                              306: 16,  # Ctrl right
                              307: 18,  # Alt left
                              308: 18}  # Alt right
"""
`Dict` {`int` Pygame key code : corresponding `int` SimpleGUI key code}.

**(Don't available in SimpleGUI of CodeSkulptor.)**
"""


if _PYGAME_AVAILABLE:
    _SIMPLEGUICOLOR_TO_PYGAMECOLOR = {'aliceblue': pygame.Color('#f0f8ff'),
                                      'antiquewhite': pygame.Color('#faebd7'),
                                      'aqua': pygame.Color('#00ffff'),
                                      'aquamarine': pygame.Color('#7fffd4'),
                                      'azure': pygame.Color('#f0ffff'),
                                      'beige': pygame.Color('#f5f5dc'),
                                      'bisque': pygame.Color('#ffe4c4'),
                                      'black': pygame.Color('#000000'),
                                      'blanchedalmond': pygame.Color('#ffebcd'),
                                      'blue': pygame.Color('#0000ff'),
                                      'blueviolet': pygame.Color('#8a2be2'),
                                      'brown': pygame.Color('#a52a2a'),
                                      'burlywood': pygame.Color('#deb887'),
                                      'cadetblue': pygame.Color('#5f9ea0'),
                                      'chartreuse': pygame.Color('#7fff00'),
                                      'chocolate': pygame.Color('#d2691e'),
                                      'coral': pygame.Color('#ff7f50'),
                                      'cornflowerblue': pygame.Color('#6495ed'),
                                      'cornsilk': pygame.Color('#fff8dc'),
                                      'crimson': pygame.Color('#dc143c'),
                                      'cyan': pygame.Color('#00ffff'),
                                      'darkblue': pygame.Color('#00008b'),
                                      'darkcyan': pygame.Color('#008b8b'),
                                      'darkgoldenrod': pygame.Color('#b8860b'),
                                      'darkgray': pygame.Color('#a9a9a9'),
                                      'darkgreen': pygame.Color('#006400'),
                                      'darkkhaki': pygame.Color('#bdb76b'),
                                      'darkmagenta': pygame.Color('#8b008b'),
                                      'darkolivegreen': pygame.Color('#556b2f'),
                                      'darkorange': pygame.Color('#ff8c00'),
                                      'darkorchid': pygame.Color('#9932cc'),
                                      'darkred': pygame.Color('#8b0000'),
                                      'darksalmon': pygame.Color('#e9967a'),
                                      'darkseagreen': pygame.Color('#8fbc8f'),
                                      'darkslateblue': pygame.Color('#483d8b'),
                                      'darkslategray': pygame.Color('#2f4f4f'),
                                      'darkturquoise': pygame.Color('#00ced1'),
                                      'darkviolet': pygame.Color('#9400d3'),
                                      'deeppink': pygame.Color('#ff1493'),
                                      'deepskyblue': pygame.Color('#00bfff'),
                                      'dimgray': pygame.Color('#696969'),
                                      'dimgrey': pygame.Color('#696969'),
                                      'dodgerblue': pygame.Color('#1e90ff'),
                                      'firebrick': pygame.Color('#b22222'),
                                      'floralwhite': pygame.Color('#fffaf0'),
                                      'forestgreen': pygame.Color('#228b22'),
                                      'fuchsia': pygame.Color('#ff00ff'),
                                      'gainsboro': pygame.Color('#dcdcdc'),
                                      'ghostwhite': pygame.Color('#f8f8ff'),
                                      'gold': pygame.Color('#ffd700'),
                                      'goldenrod': pygame.Color('#daa520'),
                                      'gray': pygame.Color('#808080'),
                                      'green': pygame.Color('#008000'),
                                      'greenyellow': pygame.Color('#adff2f'),
                                      'honeydew': pygame.Color('#f0fff0'),
                                      'hotpink': pygame.Color('#ff69b4'),
                                      'indianred': pygame.Color('#cd5c5c'),
                                      'indigo': pygame.Color('#4b0082'),
                                      'ivory': pygame.Color('#fffff0'),
                                      'khaki': pygame.Color('#f0e68c'),
                                      'lavender': pygame.Color('#e6e6fa'),
                                      'lavenderblush': pygame.Color('#fff0f5'),
                                      'lawngreen': pygame.Color('#7cfc00'),
                                      'lemonchiffon': pygame.Color('#fffacd'),
                                      'lightblue': pygame.Color('#add8e6'),
                                      'lightcoral': pygame.Color('#f08080'),
                                      'lightcyan': pygame.Color('#e0ffff'),
                                      'lightgoldenrodyellow': pygame.Color('#fafad2'),
                                      'lightgray': pygame.Color('#d3d3d3'),
                                      'lightgreen': pygame.Color('#90ee90'),
                                      'lightpink': pygame.Color('#ffb6c1'),
                                      'lightsalmon': pygame.Color('#ffa07a'),
                                      'lightseagreen': pygame.Color('#20b2aa'),
                                      'lightskyblue': pygame.Color('#87cefa'),
                                      'lightslategray': pygame.Color('#778899'),
                                      'lightsteelblue': pygame.Color('#b0c4de'),
                                      'lightyellow': pygame.Color('#ffffe0'),
                                      'lime': pygame.Color('#00ff00'),
                                      'limegreen': pygame.Color('#32cd32'),
                                      'linen': pygame.Color('#faf0e6'),
                                      'magenta': pygame.Color('#ff00ff'),
                                      'maroon': pygame.Color('#800000'),
                                      'mediumaquamarine': pygame.Color('#66cdaa'),
                                      'mediumblue': pygame.Color('#0000cd'),
                                      'mediumorchid': pygame.Color('#ba55d3'),
                                      'mediumpurple': pygame.Color('#9370db'),
                                      'mediumseagreen': pygame.Color('#3cb371'),
                                      'mediumslateblue': pygame.Color('#7b68ee'),
                                      'mediumspringgreen': pygame.Color('#00fa9a'),
                                      'mediumturquoise': pygame.Color('#48d1cc'),
                                      'mediumvioletred': pygame.Color('#c71585'),
                                      'midnightblue': pygame.Color('#191970'),
                                      'mintcream': pygame.Color('#f5fffa'),
                                      'mistyrose': pygame.Color('#ffe4e1'),
                                      'moccasin': pygame.Color('#ffe4b5'),
                                      'navajowhite': pygame.Color('#ffdead'),
                                      'navy': pygame.Color('#000080'),
                                      'oldlace': pygame.Color('#fdf5e6'),
                                      'olive': pygame.Color('#808000'),
                                      'olivedrab': pygame.Color('#6b8e23'),
                                      'orange': pygame.Color('#ffa500'),
                                      'orangered': pygame.Color('#ff4500'),
                                      'orchid': pygame.Color('#da70d6'),
                                      'palegoldenrod': pygame.Color('#eee8aa'),
                                      'palegreen': pygame.Color('#98fb98'),
                                      'paleturquoise': pygame.Color('#afeeee'),
                                      'palevioletred': pygame.Color('#db7093'),
                                      'papayawhip': pygame.Color('#ffefd5'),
                                      'peachpuff': pygame.Color('#ffdab9'),
                                      'peru': pygame.Color('#cd853f'),
                                      'pink': pygame.Color('#ffc0cb'),
                                      'plum': pygame.Color('#dda0dd'),
                                      'powderblue': pygame.Color('#b0e0e6'),
                                      'purple': pygame.Color('#800080'),
                                      'red': pygame.Color('#ff0000'),
                                      'rosybrown': pygame.Color('#bc8f8f'),
                                      'royalblue': pygame.Color('#4169e1'),
                                      'saddlebrown': pygame.Color('#8b4513'),
                                      'salmon': pygame.Color('#fa8072'),
                                      'sandybrown': pygame.Color('#f4a460'),
                                      'seagreen': pygame.Color('#2e8b57'),
                                      'seashell': pygame.Color('#fff5ee'),
                                      'sienna': pygame.Color('#a0522d'),
                                      'silver': pygame.Color('#c0c0c0'),
                                      'skyblue': pygame.Color('#87ceeb'),
                                      'slateblue': pygame.Color('#6a5acd'),
                                      'slategray': pygame.Color('#708090'),
                                      'snow': pygame.Color('#fffafa'),
                                      'springgreen': pygame.Color('#00ff7f'),
                                      'steelblue': pygame.Color('#4682b4'),
                                      'tan': pygame.Color('#d2b48c'),
                                      'teal': pygame.Color('#008080'),
                                      'thistle': pygame.Color('#d8bfd8'),
                                      'tomato': pygame.Color('#ff6347'),
                                      'turquoise': pygame.Color('#40e0d0'),
                                      'violet': pygame.Color('#ee82ee'),
                                      'wheat': pygame.Color('#f5deb3'),
                                      'white': pygame.Color('#ffffff'),
                                      'whitesmoke': pygame.Color('#f5f5f5'),
                                      'yellow': pygame.Color('#ffff00'),
                                      'yellowgreen': pygame.Color('#9acd32')}
    """
    `Dict` {`str` color constant name: corresponding `pygame.Color`}.

    **(Don't available in SimpleGUI of CodeSkulptor.)**

    See http://www.opimedia.be/DS/mementos/colors.htm

    List from http://www.w3schools.com/html/html_colornames.asp
    """
else:
    _SIMPLEGUICOLOR_TO_PYGAMECOLOR = {}


_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME = {'monospace': 'courier,couriernew',
                                        'sans-serif': 'arial,tahoma',
                                        'serif': 'timesnewroman,garamond,georgia'}
"""
Font faces using by SimpleGUI
to corresponding font names list used by Pygame.

**(Don't available in SimpleGUI of CodeSkulptor.)**
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

**(Don't available in SimpleGUI of CodeSkulptor.)**
"""



#
# Global constant
##################
KEY_MAP = {'space': 32,
           'left':  37,
           'up':    38,
           'right': 39,
           'down':  40,
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
# Classes
##########
class Canvas:
    """
    Canvas similar to SimpleGUI `Canvas` of CodeSkulptor.
    """

    _background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['black'] if _PYGAME_AVAILABLE
                                else None)
    """
    Default `pygame.Color` of the background of the canvas.
    """

    def __init__(self,
                 frame,
                 canvas_width, canvas_height):
        """
        Set the canvas.

        **Don't use directly**, a canvas is created by `Frame()`
        and reachable by handler defined by `Frame.set_draw_handler()`.

        :param frame: Frame (or None)
        :param canvas_width: int >= 0
        :param canvas_height: int >= 0
        """
        assert _PYGAME_AVAILABLE
        assert (frame == None) or isinstance(frame, Frame), type(frame)

        assert isinstance(canvas_width, int), type(canvas_width)
        assert canvas_width >= 0, canvas_width

        assert isinstance(canvas_height, int), type(canvas_height)
        assert canvas_height >= 0, canvas_height

        self._frame_parent = frame

        self._width = canvas_width
        self._height = canvas_height

        self._background_pygame_color = Canvas._background_pygame_color

        self._draw_handler = None

        self._pygame_surface = pygame.Surface((canvas_width, canvas_height))

        from math import pi

        self.pi = pi


    def __repr__(self):
        """
        Return `'<Canvas object>'`.

        :return: str
        """
        return '<Canvas object>'


    def _draw(self):
        """
        If `self._draw_handler` != `None`
        then call it and update display of the canvas.

        **(Don't available in SimpleGUI of CodeSkulptor.)**
        """
        if (self._draw_handler != None) and (self._frame_parent != None):
            self._pygame_surface.fill(self._background_pygame_color)

            self._draw_handler(self)

            self._frame_parent._pygame_surface.blit(self._pygame_surface,
                                                    (self._frame_parent._canvas_x_offset,
                                                     self._frame_parent._canvas_y_offset))

            pygame.display.update((self._frame_parent._canvas_x_offset,
                                   self._frame_parent._canvas_y_offset,
                                   self._width,
                                   self._height))


    def _save(self, filename):
        """
        Save the canvas in `filename`.

        Supported formats are supported formats by Pygame to save:
        TGA, PNG, JPEG or BMP
        (see http://www.pygame.org/docs/ref/image.html#pygame.image.save ).

        If `filename` extension is not recognized
        then TGA format is used.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param filename: str
        """
        assert isinstance(filename, str), type(filename)

        pygame.image.save(self._pygame_surface, filename)


    def draw_circle(self,
                    center_point, radius,
                    line_width, line_color,
                    fill_color = None):
        """
        Draw a circle.

        If `fill_color` != `None`
        then fill with this color.

        :param center_point: (int or float, int or float) or [int or float, int or float]
        :param radius: (int or float) > 0
        :param line_width: (int or float) > 0
        :param line_color: str
        :param fill_color: None or str
        """
        assert isinstance(center_point, tuple) or isinstance(center_point, list), type(center_point)
        assert len(center_point) == 2, len(center_point)
        assert isinstance(center_point[0], int) or isinstance(center_point[0], float), type(center_point[0])
        assert isinstance(center_point[1], int) or isinstance(center_point[1], float), type(center_point[1])

        assert isinstance(radius, int) or isinstance(radius, float), type(radius)
        assert radius > 0, radius

        assert isinstance(line_width, int) or isinstance(line_width, float), type(line_width)
        assert line_width > 0, line_width

        assert isinstance(line_color, str), type(line_color)
        assert (fill_color == None) or isinstance(fill_color, str), type(fill_color)

        line_width = (1 if line_width <= 1
                      else int(round(line_width)))

        radius = int(round(radius)) + int(round(line_width//2))

        if radius > 1:
            line_color = _simpleguicolor_to_pygamecolor(line_color)
            if fill_color != None:
                fill_color = _simpleguicolor_to_pygamecolor(fill_color)

            if (line_color.a == 255) and ((fill_color == None) or (fill_color.a == 255)):  # without alpha
                if fill_color != None:
                    pygame.draw.circle(self._pygame_surface, fill_color,
                                       _pos_round(center_point), radius, 0)
                if line_color != fill_color:
                    pygame.draw.circle(self._pygame_surface, line_color,
                                       _pos_round(center_point), radius, min(line_width, radius))
            elif (line_color.a > 0) or ((fill_color != None) and (fill_color.a > 0)):      # with one or two alpha (not null)
                s_alpha = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)

                if (fill_color != None) and (fill_color.a > 0):
                    pygame.draw.circle(s_alpha, fill_color,
                                       (radius, radius), radius, 0)
                if (line_color != fill_color) and (line_color.a > 0):
                    pygame.draw.circle(s_alpha, line_color,
                                       (radius, radius), radius, min(line_width, radius))

                self._pygame_surface.blit(s_alpha, (int(round(center_point[0])) - radius,
                                                    int(round(center_point[1])) - radius))
        elif radius > 0:  # == 1
            self.draw_point(center_point, line_color)


    def draw_image(self, image,
                   center_source, width_height_source,
                   center_dest, width_height_dest,
                   rotation = 0):
        """
        Draw `image` on the canvas.

        Specify center position and size of the source (`image`)
        and center position and size of the destination (the canvas).

        Size of the source allow get a piece of `image`.
        If `width_height_source` is bigger than `image`
        then draw nothing.

        Size of the destination allow rescale the drawed image.

        `rotation` specify a clockwise rotation in radians.

        :param image: Image
        :param center_source: (int or float, int or float) or [int or float, int or float]
        :param width_height_source: ((int or float) >= 0, (int or float) >= 0) or [(int or float) >= 0, (int or float) >= 0]
        :param center_dest: (int or float, int or float) or [int or float, int or float]
        :param width_height_dest: ((int or float) >= 0, (int or float) >= 0) or [(int or float) >= 0, (int or float) >= 0]
        :param rotation: int or float
        """
        assert isinstance(image, Image), type(image)

        assert isinstance(center_source, tuple) or isinstance(center_source, list), type(center_source)
        assert len(center_source) == 2, len(center_source)
        assert isinstance(center_source[0], int) or isinstance(center_source[0], float), type(center_source[0])
        assert isinstance(center_source[1], int) or isinstance(center_source[1], float), type(center_source[1])

        assert isinstance(width_height_source, tuple) or isinstance(width_height_source, list), type(width_height_source)
        assert len(width_height_source) == 2, len(width_height_source)
        assert isinstance(width_height_source[0], int) or isinstance(width_height_source[0], float), type(width_height_source[0])
        assert width_height_source[0] >= 0, width_height_source[0]
        assert isinstance(width_height_source[1], int) or isinstance(width_height_source[1], float), type(width_height_source[1])
        assert width_height_source[1] >= 0, width_height_source[1]

        assert isinstance(center_dest, tuple) or isinstance(center_dest, list), type(center_dest)
        assert len(center_dest) == 2, len(center_dest)
        assert isinstance(center_dest[0], int) or isinstance(center_dest[0], float), type(center_dest[0])
        assert isinstance(center_dest[1], int) or isinstance(center_dest[1], float), type(center_dest[1])

        assert isinstance(width_height_dest, tuple) or isinstance(width_height_dest, list), type(width_height_dest)
        assert len(width_height_dest) == 2, len(width_height_dest)
        assert isinstance(width_height_dest[0], int) or isinstance(width_height_dest[0], float), type(width_height_dest[0])
        assert width_height_dest[0] >= 0, width_height_dest[0]
        assert isinstance(width_height_dest[1], int) or isinstance(width_height_dest[1], float), type(width_height_dest[1])
        assert width_height_dest[1] >= 0, width_height_dest[1]

        assert isinstance(rotation, int) or isinstance(rotation, float), type(rotation)

        pygame_surface_image = image._pygame_surface

        if pygame_surface_image != None:
            width_source, height_source = width_height_source

            x0_source = center_source[0] - width_source/2.0
            y0_source = center_source[1] - height_source/2.0

            if x0_source >= 0:
                x0_source = int(round(x0_source))
            elif -1 < x0_source:
                width_source -= x0_source
                x0_source = 0
            else:
                return

            if y0_source >= 0:
                y0_source = int(round(y0_source))
            elif -1 < y0_source:
                height_source -= y0_source
                y0_source = 0
            else:
                return

            width_source = int(round(width_source))
            height_source = int(round(height_source))

            if ((x0_source + width_source > image.get_width() + 1)
                or (y0_source + height_source > image.get_height() + 1)):  # bigger than image
                return

            if x0_source + width_source > image.get_width():  # keep this image (seem too big, maybe rounding error)
                width_source -= 1

            if y0_source + height_source > image.get_height():  # keep this image (seem too big, maybe rounding error)
                height_source -= 1

        if pygame_surface_image != None:

            if ((x0_source != 0)
                or (y0_source != 0)
                or (width_source != image.get_width())
                or (height_source != image.get_height())):
                # Get a piece
                pygame_surface_image = pygame_surface_image.subsurface((x0_source, y0_source,
                                                                        width_source, height_source))

            width_height_dest = _pos_round(width_height_dest)

            if (width_height_dest[0] != width_source) or (width_height_dest[1] != height_source):
                # Resize
                pygame_surface_image = pygame.transform.scale(pygame_surface_image,
                                                              width_height_dest)

            if rotation != 0:
                # Rotation
                pygame_surface_image = pygame.transform.rotate(pygame_surface_image,
                                                               -rotation*180/self.pi)


            # Draw the result
            self._pygame_surface.blit(pygame_surface_image,
                                      (int(round(center_dest[0] - pygame_surface_image.get_width()/2.0)),
                                       int(round(center_dest[1] - pygame_surface_image.get_height()/2.0))))


    def draw_line(self,
                  point1, point2,
                  line_width, line_color):
        """
        Draw a line segment from point1 to point2.

        :param point1: (int or float, int or float) or [int or float, int or float]
        :param point2: (int or float, int or float) or [int or float, int or float]
        :param line_width: (int or float) > 0
        :param line_color: str
        """
        assert isinstance(point1, tuple) or isinstance(point1, list), type(point1)
        assert len(point1) == 2, len(point1)
        assert isinstance(point1[0], int) or isinstance(point1[0], float), type(point1[0])
        assert isinstance(point1[1], int) or isinstance(point1[1], float), type(point1[1])

        assert isinstance(point2, tuple) or isinstance(point2, list), type(point2)
        assert len(point2) == 2, len(point2)
        assert isinstance(point2[0], int) or isinstance(point2[0], float), type(point2[0])
        assert isinstance(point2[1], int) or isinstance(point2[1], float), type(point2[1])

        assert isinstance(line_width, int) or isinstance(line_width, float), type(line_width)
        assert line_width > 0, line_width

        assert isinstance(line_color, str), type(line_color)

        line_color = _simpleguicolor_to_pygamecolor(line_color)

        if line_color.a == 255:  # without alpha
            pygame.draw.line(self._pygame_surface, line_color,
                             _pos_round(point1), _pos_round(point2),
                             int(round(line_width)))
        elif line_color.a > 0:   # with alpha (not null)
            x1, y1 = _pos_round(point1)
            x2, y2 = _pos_round(point2)

            width = abs(x2 - x1) + line_width*2
            height = abs(y2 - y1) + line_width*2

            x_min = min(x1, x2)
            y_min = min(y1, y2)

            s_alpha = pygame.Surface((width, height), pygame.SRCALPHA)
            pygame.draw.line(s_alpha, line_color,
                             (x1 - x_min + line_width, y1 - y_min + line_width),
                             (x2 - x_min + line_width, y2 - y_min + line_width),
                             int(round(line_width)))
            self._pygame_surface.blit(s_alpha, (x_min - line_width, y_min - line_width))


    def draw_point(self, position, color):
        """
        Draw a point.

        (Available in SimpleGUI of CodeSkulptor
        but *don't in CodeSkulptor documentation*!)

        :param position: (int or float, int or float) or [int or float, int or float]
        :param color: str
        """
        assert isinstance(position, tuple) or isinstance(position, list), type(position)
        assert len(position) == 2, len(position)
        assert isinstance(position[0], int) or isinstance(position[0], float), type(position[0])
        assert isinstance(position[1], int) or isinstance(position[1], float), type(position[1])

        assert isinstance(color, str), type(color)

        color = _simpleguicolor_to_pygamecolor(color)

        if color.a == 255:  # without alpha
            self._pygame_surface.set_at(_pos_round(position), color)
        elif color.a > 0:   # with alpha (not null)
            s_alpha = pygame.Surface((1, 1), pygame.SRCALPHA)
            s_alpha.set_at((0, 0), color)
            self._pygame_surface.blit(s_alpha, _pos_round(position))


    def draw_polygon(self,
                     point_list,
                     line_width, line_color,
                     fill_color = None):
        """
        Draw a polygon from a list of points.
        A segment is automatically drawed between the last point and the first point.

        If `fill color` != None
        then fill with this color.

        If `line_width` > 1, ends are poorly made!

        :param point_list: non empty (tuple or list) of ((int or float, int or float) or [int or float, int or float])
        :param line_width: (int or float) > 0
        :param line_color: str
        :param fill_color: None or str
        """
        assert isinstance(point_list, tuple) or isinstance(point_list, list), type(point_list)
        assert len(point_list) > 0, len(point_list)

        if __debug__:
            for point in point_list:
                assert isinstance(point, tuple) or isinstance(point, list), type(point)
                assert len(point) == 2, len(point)
                assert isinstance(point[0], int) or isinstance(point[0], float), type(point[0])
                assert isinstance(point[1], int) or isinstance(point[1], float), type(point[1])

        assert isinstance(line_width, int) or isinstance(line_width, float), type(line_width)
        assert line_width >= 0, line_width

        assert isinstance(line_color, str), type(line_color)
        assert (fill_color == None) or isinstance(fill_color, str), type(fill_color)

        if len(point_list) == 1:
            return

        line_color = _simpleguicolor_to_pygamecolor(line_color)
        if fill_color != None:
            fill_color = _simpleguicolor_to_pygamecolor(fill_color)

        point_list = [_pos_round(point) for point in point_list]

        if (line_color.a == 255) and ((fill_color == None) or (fill_color.a == 255)):  # without alpha
            if fill_color != None:
                pygame.draw.polygon(self._pygame_surface, fill_color,
                                    point_list, 0)
            if line_color != fill_color:
                pygame.draw.lines(self._pygame_surface, line_color, True,
                                  point_list, line_width)
        elif (line_color.a > 0) or ((fill_color != None) and (fill_color.a > 0)):      # with one or two alpha (not null)
            s_alpha = pygame.Surface((self._width, self._height), pygame.SRCALPHA)

            if (fill_color != None) and (fill_color.a > 0):
                pygame.draw.polygon(s_alpha, fill_color,
                                    point_list, 0)
            if (line_color != fill_color) and (line_color.a > 0):
                pygame.draw.lines(s_alpha, line_color, True,
                                  point_list, line_width)

            self._pygame_surface.blit(s_alpha, (0, 0))


    def draw_polyline(self,
                      point_list,
                      line_width, line_color):
        """
        Draw line segments between a list of points.

        If `line_width` > 1, ends are poorly made!

        :param point_list: non empty (tuple or list) of ((int or float, int or float) or [int or float, int or float])
        :param line_width: (int or float) > 0
        :param line_color: str
        """
        assert isinstance(point_list, tuple) or isinstance(point_list, list), type(point_list)
        assert len(point_list) > 0, len(point_list)

        if __debug__:
            for point in point_list:
                assert isinstance(point, tuple) or isinstance(point, list), type(point)
                assert len(point) == 2, len(point)
                assert isinstance(point[0], int) or isinstance(point[0], float), type(point[0])
                assert isinstance(point[1], int) or isinstance(point[1], float), type(point[1])

        assert isinstance(line_width, int) or isinstance(line_width, float), type(line_width)
        assert line_width > 0, line_width

        assert isinstance(line_color, str), type(line_color)

        if len(point_list) == 1:
            return

        line_color = _simpleguicolor_to_pygamecolor(line_color)

        point_list = [_pos_round(point) for point in point_list]

        if line_color.a == 255:  # without alpha
            pygame.draw.lines(self._pygame_surface, line_color, False,
                              point_list, line_width)
        elif line_color.a > 0:   # with alpha (not null)
            s_alpha = pygame.Surface((self._width, self._height), pygame.SRCALPHA)

            pygame.draw.lines(s_alpha, line_color, False,
                              point_list, line_width)

            self._pygame_surface.blit(s_alpha, (0, 0))


    def draw_text(self,
                  text, point,
                  font_size, font_color,
                  font_face = 'serif',
                  _font_size_coef = 3.0/4):
        """
        Draw the `text` string at the position `point`.

        (`point[0]` is the left of the text,
        `point[1]` is the bottom of the text.)

        If correponding font in Pygame is not founded,
        then use the default `pygame.Font`.

        `_font_size_coef` is used to adjust the vertical positioning.
        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param text: str
        :param point: (int or float, int or float) or [int or float, int or float]
        :param font_size: (int or float) >= 0
        :param font_color: str
        :param font_face: str == 'monospace', 'sans-serif', 'serif'
        :param _font_size_coef: int or float

        **(Alpha color channel don't work!!!)**
        """
        assert isinstance(text, str), type(text)

        assert isinstance(point, tuple) or isinstance(point, list), type(point)
        assert len(point) == 2, len(point)
        assert isinstance(point[0], int) or isinstance(point[0], float), type(point[0])
        assert isinstance(point[1], int) or isinstance(point[1], float), type(point[1])

        assert isinstance(font_size, int) or isinstance(font_size, float), type(font_size)
        assert font_size >= 0, font_size

        assert isinstance(font_color, str), type(font_color)

        assert isinstance(font_face, str), type(font_face)
        assert font_face in _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME, font_face

        assert isinstance(_font_size_coef, int) or isinstance(_font_size_coef, float), type(_font_size_coef)

        font_color = _simpleguicolor_to_pygamecolor(font_color)
        font_size = int(round(font_size))

        if (font_color.a > 0) and (font_size > 0):
            font = _simpleguifontface_to_pygamefont(font_face, font_size)

            pygame_surface_text = font.render(text, True, font_color)

            if font_color.a == 255:  # without alpha
                self._pygame_surface.blit(pygame_surface_text, (point[0],
                                                                point[1] - font.get_height()*_font_size_coef))
            else:                    # with alpha (not null)
                # Don't work!!!
                s_alpha = pygame.Surface((pygame_surface_text.get_width(), pygame_surface_text.get_height()), pygame.SRCALPHA)
                s_alpha.blit(pygame_surface_text, (0,0))
                self._pygame_surface.blit(s_alpha, (point[0],
                                                    point[1] - font.get_height()*_font_size_coef))


class Control:
    """
    Control similar to SimpleGUI `Control` (button and label) of CodeSkulptor.
    """

    _button_background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['silver'] if _PYGAME_AVAILABLE
                                       else None)
    """
    `pygame.Color` of the background in the button.
    """

    _button_selected_background_pygame_color = (pygame.Color('#f0f0f0') if _PYGAME_AVAILABLE
                                                else None)
    """
    `pygame.Color` of the background in the button when it has pressed.
    """

    _button_text_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['black'] if _PYGAME_AVAILABLE
                                 else None)
    """
    `pygame.Color` of text in the button.
    """

    _button_pygame_font = (pygame.font.Font(None, 20) if _PYGAME_AVAILABLE
                           else None)
    """
    `pygame.Font` of text in the button.
    """

    _button_padding_x = 5
    """
    Horizontal padding in the button.
    """

    _button_padding_y = 3
    """
    Vertical padding in the button.
    """

    _label_text_pygame_color = _button_text_pygame_color
    """
    `pygame.Color` of the label.
    """

    _label_pygame_font = _button_pygame_font
    """
    `pygame.Font` of the label.
    """

    def __init__(self,
                 frame,
                 text,
                 button_handler = None, button_width = None):
        """
        Set a button or a label in the control panel.

        **Don't use directly**, use `Frame.add_button()` or `Frame.add_label()`.

        :param frame: Frame
        :param text: str
        :param button_handler: None or (function () -> *)
        :param button_width: None or int or float
        """
        assert _PYGAME_AVAILABLE
        assert isinstance(frame, Frame), type(frame)
        assert isinstance(text, str), type(text)
        assert (button_handler == None) or callable(button_handler), type(button_handler)
        assert (button_width == None) or isinstance(button_width, int) or isinstance(button_width, float), type(button_width)

        self._frame_parent = frame

        self._text = text
        self._button_handler = button_handler  # if == None then it's a label, else it's a button
        self._button_width = (max(0, int(round(button_width))) if (button_width != None) and (button_handler != None)
                              else None)

        self._x1 = 0
        self._y1 = (frame._controls[-1]._y2 + 2 if frame._controls
                    else 0)
        self._x2 = None
        self._y2 = None


    def __repr__(self):
        """
        Return `'<Control object>'`.

        :return: str
        """
        return '<Control object>'


    def _mouse_left_button(self, pressed):
        """
        Deal a click of left mouse button on the zone of this `Control`.

        If `pressed`
        then select this Control,
        else unselect and run the button handler (if exist).

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param pressed: bool
        """
        assert isinstance(pressed, bool), type(pressed)

        self._frame_parent._control_selected = (self if pressed
                                                else None)
        self._frame_parent._draw_controlpanel()
        if (not pressed) and (self._button_handler != None):
            self._button_handler()


    def _draw(self):
        """
        Draw the control object in the control panel.

        **(Don't available in SimpleGUI of CodeSkulptor.)**
        """
        if self._button_handler == None:
            self._draw_label()
        else:
            self._draw_button()


    def _draw_button(self):
        """
        Draw the the control object as a button.

        **(Don't available in SimpleGUI of CodeSkulptor.)**
        """
        pygame_surface_text = Control._button_pygame_font.render(self._text.strip(),
                                                                 True, Control._button_text_pygame_color)

        text_width, text_height = pygame_surface_text.get_size()

        if self._button_width == None:
            width = text_width + Control._button_padding_x*2
            x = Control._button_padding_x
        else:
            width = max(self._button_width, text_width + Control._button_padding_x*2)
            x = (width - text_width)//2

        height = text_height + Control._button_padding_y*2

        self._x2 = self._x1 + width
        self._y2 = self._y1 + height

        pygame_surface_button = pygame.Surface((width, height))
        pygame_surface_button.fill(Frame._controlpanel_background_pygame_color)

        for i, color in enumerate(((Control._button_selected_background_pygame_color if self._frame_parent._control_selected == self
                                    else Control._button_background_pygame_color),
                                   Control._button_text_pygame_color)):
            pygame.draw.polygon(pygame_surface_button, color,
                                ((3, 0),
                                 (width - 4, 0),
                                 (width - 1, 3),
                                 (width - 1, height - 4),
                                 (width - 4, height - 1),
                                 (3, height - 1),
                                 (0, height - 4),
                                 (0, 3)),
                                i)  # button with rounded corners

        pygame_surface_button.blit(pygame_surface_text, (x, (height - text_height)//2))

        self._frame_parent._controlpanel_pygame_surface.blit(pygame_surface_button, (self._x1, self._y1))


    def _draw_label(self):
        """
        Draw the the control object as a label.

        **(Don't available in SimpleGUI of CodeSkulptor.)**
        """
        pygame_surface_text = Control._label_pygame_font.render(self._text.strip(),
                                                                True, Control._label_text_pygame_color)

        width, height = pygame_surface_text.get_size()
        self._x2 = self._x1 + width
        self._y2 = self._y1 + height

        self._frame_parent._controlpanel_pygame_surface.blit(pygame_surface_text, (self._x1, self._y1))


    def _pos_in(self, x, y):
        """
        If position (`x`, `y`) is on the zone of this `aControl`
        then return `True`,
        else return `False`.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param x: int or float
        :param y: int or float

        :return: bool
        """
        assert isinstance(x, int) or isinstance(x, float), type(x)
        assert isinstance(y, int) or isinstance(y, float), type(y)

        return ((self._x1 <= x <= self._x2)
                and (self._y1 <= y <= self._y2))


    def get_text(self):
        """
        Return the text of the button or the label.

        (Available in SimpleGUI of CodeSkulptor
        but *don't in CodeSkulptor documentation*!)

        :return: str
        """
        return self._text


    def set_text(self, text):
        """
        Change the text of the button or the label.

        :param text: str
        """
        assert isinstance(text, str), type(text)

        self._text = text
        self._frame_parent._draw_controlpanel()



class Frame:
    """
    Frame similar to SimpleGUI `Frame` of CodeSkulptor.
    """

    _already_frame = False
    """
    Become `True` when instantiate the first frame.
    """

    _background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
                                else None)
    """
    Default background color of frame.
    """

    _canvas_border_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['black'] if _PYGAME_AVAILABLE
                                   else None)
    """
    Border color of canvas.
    """

    _controlpanel_background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
                                             else None)
    """
    Background color of control panel.
    """

    _fps = 60
    """
    Frames per second drawed (frequency of draw and check events)
    """

    _hide_controlpanel = False
    """
    If `True`
    then hide control panel (and status box).
    """

    _hide_status = False
    """
    If `True`
    then hide status box.
    """

    _pygame_mode_flags = 0
    """
    Default options of graphic mode.

    See http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    """

    _pygame_mode_depth = 0
    """
    Default number of bits used to represent color.

    See http://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    """

    _save_canvas_requests = []
    """
    List of filenames in which to save canvas image.
    """

    _statuskey_background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
                                          else None)
    """
    `pygame.Color` of background in status key box.
    """

    _statuskey_height = 20
    """
    Height of the status key box.
    """

    _statuskey_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['black'] if _PYGAME_AVAILABLE
                               else None)
    """
    `pygame.Color` of status key box (text and rectangle).
    """

    _statuskey_pygame_font = (pygame.font.Font(None, _statuskey_height) if _PYGAME_AVAILABLE
                              else None)
    """
    `pygame.Font` of status key box.
    """

    _statusmouse_background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
                                            else None)
    """
    `pygame.Color` of background in status mouse box.
    """

    _statusmouse_height = _statuskey_height
    """
    Height of the status mouse box.
    """

    _statusmouse_pygame_color = _statuskey_pygame_color
    """
    `pygame.Color` of status mouse box (text and rectangle).
    """

    _statusmouse_pygame_font = (pygame.font.Font(None, _statusmouse_height) if _PYGAME_AVAILABLE
                                else None)
    """
    `pygame.Font` of status mouse box..
    """

    _keep_timers = None
    """
    If `None`
    then ask if it should be stop timers when stop frame.

    If `True`
    then timers keep running when stop frame.

    If `False`
    then stop all timers when stop frame.
    """

    def __init__(self,
                 title,
                 canvas_width, canvas_height,
                 control_width = 200):
        """
        Set the frame.

        **Don't use directly**, use create_frame().

        :param title: str
        :param canvas_width: (int or float) >= 0
        :param canvas_height: (int or float) >= 0
        :param control_width: (int or float) >= 0
        """
        assert _PYGAME_AVAILABLE
        assert not Frame._already_frame

        assert isinstance(title, str), type(title)

        assert isinstance(canvas_width, int) or isinstance(canvas_width, float), type(canvas_width)
        assert canvas_width >= 0, canvas_width

        assert isinstance(canvas_height, int) or isinstance(canvas_height, float), type(canvas_height)
        assert canvas_height >= 0, canvas_height

        assert isinstance(control_width, int) or isinstance(control_width, float), type(control_width)
        assert control_width >= 0, control_width

        Frame._already_frame = True

        self._control_width = (0 if Frame._hide_controlpanel
                               else int(round(control_width)))

        self._border_size = (0 if Frame._hide_controlpanel
                             else 25)
        self._canvas_border_size = 2

        self._canvas_x_offset = self._border_size + self._control_width + self._border_size + self._canvas_border_size
        self._canvas_y_offset = self._border_size + self._canvas_border_size

        self._controls = []
        self._control_next_y = 10
        self._control_selected = None

        self._fps_average = 0

        self._keydown_handler = None
        self._keyup_handler = None

        self._mouseclic_handler = None
        self._mousedrag_handler = None

        self._running = False


        canvas_width = int(round(canvas_width))
        canvas_height = int(round(canvas_height))


        self._statusmouse_x_offset = 0
        self._statusmouse_y_offset = self._canvas_y_offset + canvas_height - Frame._statusmouse_height

        self._statuskey_x_offset = self._statusmouse_x_offset
        self._statuskey_y_offset = self._statusmouse_y_offset - 5 - Frame._statuskey_height


        # Create the window
        from os.path import sep

        icon_path = __file__.split(sep)[:-1]
        try:
            icon_path.extend(('_img', 'SimpleGUICS2Pygame_cartoon_64x64_t.png'))
            pygame.display.set_icon(pygame.image.load(sep.join(icon_path)))
        except:
            pass

        self._pygame_surface = pygame.display.set_mode((self._canvas_x_offset + canvas_width + self._canvas_border_size + self._border_size,
                                                        self._canvas_y_offset + canvas_height + self._canvas_border_size + self._border_size),
                                                       Frame._pygame_mode_flags,
                                                       Frame._pygame_mode_depth)
        pygame.display.set_caption(title)
        self._pygame_surface.fill(Frame._background_pygame_color)


        for i in range(1, self._canvas_border_size + 1):
            pygame.draw.rect(self._pygame_surface, Frame._canvas_border_pygame_color,
                             (self._canvas_x_offset - i,
                              self._canvas_y_offset - i,
                              canvas_width + 2*i,
                              canvas_height + 2*i),
                             1)


        # Create the canvas
        self._canvas = Canvas(self, canvas_width, canvas_height)


        # Create the status boxes: key and mouse
        self._statuskey_pygame_surface = pygame.Surface((self._control_width, Frame._statuskey_height))
        self._statusmouse_pygame_surface = pygame.Surface((self._control_width, Frame._statusmouse_height))
        # will be drawn by self._draw_controlpanel()


        # Create the control panel
        self._controlpanel_pygame_surface = pygame.Surface((self._control_width, canvas_height))
        self._draw_controlpanel()


        # Display all
        pygame.display.update()



    def __repr__(self):
        """
        Return '<Frame object>'.

        :return: str
        """
        return '<Frame object>'


    def _draw_controlpanel(self):
        """
        Draw the control panel
        and two status boxes.

        **(Don't available in SimpleGUI of CodeSkulptor.)**
        """
        self._controlpanel_pygame_surface.fill(Frame._controlpanel_background_pygame_color)

        for control in self._controls:
            control._draw()

        if Frame._hide_controlpanel:
            return

        self._pygame_surface.blit(self._controlpanel_pygame_surface,
                                  (self._border_size,
                                   self._canvas_y_offset))

        self._draw_statuskey()
        self._draw_statusmouse()

        pygame.display.update((self._border_size,
                               self._canvas_y_offset,
                               self._control_width,
                               self._canvas._height))


    def _draw_statuskey(self, key = 0, pressed = None):
        """
        Draw the status box of key.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param key: int
        :param pressed: None or bool
        """
        assert isinstance(key, int), type(key)
        assert (pressed == None) or isinstance(pressed, bool), type(pressed)

        if Frame._hide_status or Frame._hide_controlpanel:
            return

        self._statuskey_pygame_surface.fill(Frame._statuskey_background_pygame_color)
        pygame.draw.rect(self._statuskey_pygame_surface, Frame._statuskey_pygame_color,
                         (0, 0, self._control_width, Frame._statuskey_height), 1)

        if pressed != None:
            key = _SIMPLEGUIKEY_TO_STATUSKEY.get(key, key)
            s = 'Key: {} {}'.format(('Down' if pressed
                                     else 'Up'), (key if isinstance(key, str)
                                                  else '<{}>'.format(key)))
        else:
            s = 'Key:'

        pygame_surface_text = Frame._statuskey_pygame_font.render(s,
                                                                  True, Frame._statuskey_pygame_color)
        self._statuskey_pygame_surface.blit(pygame_surface_text,
                                            (5,
                                             (Frame._statuskey_height - pygame_surface_text.get_height())/2))

        self._pygame_surface.blit(self._statuskey_pygame_surface,
                                  (self._border_size + self._statuskey_x_offset,
                                   self._statuskey_y_offset))

        pygame.display.update((self._border_size + self._statuskey_x_offset,
                               self._statuskey_y_offset,
                               self._control_width,
                               Frame._statuskey_height))


    def _draw_statusmouse(self, position = (0, 0), pressed = None):
        """
        Draw the status box of mouse.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param position: (int or float, int or float) or [int or float, int or float]
        :param pressed: bool
        """
        assert isinstance(position, tuple) or isinstance(position, list), type(position)
        assert len(position) == 2, len(position)
        assert isinstance(position[0], int) or isinstance(position[0], float), type(position[0])
        assert isinstance(position[1], int) or isinstance(position[1], float), type(position[1])

        assert (pressed == None) or isinstance(pressed, bool), type(pressed)

        if Frame._hide_status or Frame._hide_controlpanel:
            return

        self._statusmouse_pygame_surface.fill(Frame._statusmouse_background_pygame_color)
        pygame.draw.rect(self._statusmouse_pygame_surface, Frame._statusmouse_pygame_color,
                         (0, 0, self._control_width, Frame._statusmouse_height), 1)

        s = ('Mouse: {} {}, {}'.format(('Move' if pressed
                                        else 'Click'), position[0], position[1]) if pressed != None
             else 'Mouse:')

        pygame_surface_text = Frame._statusmouse_pygame_font.render(s,
                                                                    True, Frame._statusmouse_pygame_color)
        self._statusmouse_pygame_surface.blit(pygame_surface_text,
                                              (5,
                                               (Frame._statusmouse_height - pygame_surface_text.get_height())/2))

        self._pygame_surface.blit(self._statusmouse_pygame_surface,
                                  (self._border_size + self._statusmouse_x_offset,
                                   self._statusmouse_y_offset))

        pygame.display.update((self._border_size + self._statusmouse_x_offset,
                               self._statusmouse_y_offset,
                               self._control_width,
                               Frame._statusmouse_height))


    def _get_fps_average(self):
        """
        Return the framerate average (in frame per second) computed by Pygame.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :return: float
        """
        return float(self._fps_average)


    def _pos_in_control(self, x, y):
        """
        If position (`x`, `y`) is on the zone of one `Control` or `TextAreaControl`
        then return it
        else return `None`.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param x: int or float
        :param y: int or float

        :return: None or Control or TextAreaControl
        """
        assert isinstance(x, int) or isinstance(x, float), type(x)
        assert isinstance(y, int) or isinstance(y, float), type(y)

        if self._controls and (self._controls[0]._y1 <= y <= self._controls[-1]._y2):
            for control in self._controls:
                if control._pos_in(x, y):
                    return control

        return None


    def _save_canvas_request(self, filename):
        """
        Request to save the canvas image in a file.

        (The images are saved on each cycle fixed by `Frame._fps_average`.)

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param filemane: str
        """
        assert isinstance(filename, str), type(filename)

        Frame._save_canvas_requests.append(filename)


    def _save_canvas_and_stop(self, filename, after = 1000):
        """
        Wait after ms (first wait until the frame is started),
        then save the canvas in a file
        and stop the program.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param filemane: str
        :param after: int or float >= 0
        """
        assert isinstance(filename, str), type(filename)
        assert isinstance(after, int) or isinstance(after, float), type(after)
        assert after >= 0, after

        def save_canvas_and_stop():
            if self._running:
                self._save_canvas_request(filename)

                Timer._stop_all()
                self.stop()


        if after == 0:
            save_canvas_and_stop()
        else:
            timer = create_timer(after, save_canvas_and_stop)
            timer.start()


    def add_button(self,
                   text,
                   button_handler,
                   width = 0):
        """
        Add a button in the control panel.

        When the button are pressed and released,
        `button_handler` are executed.

        :frame text: str
        :frame button_handler: function () -> *
        :frame width: int or float

        :return: Control
        """
        assert isinstance(text, str), type(text)
        assert callable(button_handler), type(button_handler)
        assert isinstance(width, int) or isinstance(width, float), type(width)

        button = Control(self, text, button_handler, width)
        self._controls.append(button)

        self._draw_controlpanel()

        return button


    def add_input(self,
                  text,
                  input_handler,
                  width):
        """
        Add a "label" with an input box in the control panel.

        When click with left button of mouse on the "label" or input box,
        the focus is give to this input box.

        When press Tab,
        the focus is give to the next input box (if exist).

        When press Enter,
        this input box lost the focus
        and `input_handler` are executed with the input text.

        :frame text: str
        :frame input_handler: function (str) -> *
        :frame width: int or float

        :return: Control
        """
        assert isinstance(text, str), type(text)
        assert callable(input_handler), type(input_handler)
        assert isinstance(width, int) or isinstance(width, float), type(width)

        input = TextAreaControl(self, text, input_handler, width)
        self._controls.append(input)

        self._draw_controlpanel()

        return input


    def add_label(self, text):
        """
        Add a label in the control panel.

        :frame text: str

        :return: Control
        """
        assert isinstance(text, str), type(text)

        label = Control(self, text)
        self._controls.append(label)

        self._draw_controlpanel()

        return label


    def get_canvas_image(self):
        """
        Available in SimpleGUI of CodeSkulptor
        but *don't in CodeSkulptor documentation*!

        It is a special method in CodeSkulptor,
        **never execute this method**.

        :raise: Exception if called ;-)
        """
        raise Exception('Never execute this method!')


    def get_canvas_textwidth(self,
                             text,
                             font_size,
                             font_face = 'serif'):
        """
        Return the width needed to draw `text` by `Frame.draw_text()`.

        :param text: str
        :param font_size: (int or float) >= 0
        :param font_face: str == 'monospace', 'sans-serif', 'serif'

        :return: int or float >= 0
        """
        assert isinstance(text, str), type(text)

        assert isinstance(font_size, int) or isinstance(font_size, float), type(font_size)
        assert font_size >= 0, font_size

        assert isinstance(font_face, str), type(font_face)
        assert font_face in _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME, font_face

        font_size = int(round(font_size))

        return (_simpleguifontface_to_pygamefont(font_face, font_size).size(text)[0] if font_size > 0
                else 0)


    def set_canvas_background(self,
                              color):
        """
        Set the background color of the canvas.

        :param color: str
        """
        assert isinstance(color, str), type(color)

        self._canvas._background_pygame_color = _simpleguicolor_to_pygamecolor(color)


    def set_draw_handler(self,
                         draw_handler):
        """
        Set the function handler
        that will be executed each cycle fixed by `Frame._fps_average`.

        :param timer_handler: function (Canvas) -> *
        """
        assert callable(draw_handler), type(draw_handler)

        self._canvas._draw_handler = draw_handler


    def set_keydown_handler(self,
                            key_handler):
        """
        Set the function handler
        that will be executed (with the key code) when a key is released.

        (The events are checked on each cycle fixed by `Frame._fps_average`.)

        :param timer_handler: function (int >= 0) -> *
        """
        assert callable(key_handler), type(key_handler)

        self._keydown_handler = key_handler


    def set_keyup_handler(self,
                          key_handler):
        """
        Set the function handler
        that will be executed (with the key code) when a key is pressed.

        (The events are checked on each cycle fixed by `Frame._fps_average`.)

        :param timer_handler: function (int >= 0) -> *
        """
        assert callable(key_handler), type(key_handler)

        self._keyup_handler = key_handler


    def set_mouseclick_handler(self,
                               mouse_handler):
        """
        Set the function handler
        that will be executed (with the position of the mouse)
        when the left button of mouse is **released**.

        (The events are checked on each cycle fixed by `Frame._fps_average`.)

        :param timer_handler: function ((int >= 0, int >= 0)) -> *
        """
        assert callable(mouse_handler), type(mouse_handler)

        self._mouseclic_handler = mouse_handler


    def set_mousedrag_handler(self,
                              mouse_handler):
        """
        Set the function handler
        that will be executed  (with the position of the mouse)
        **for each** new mouse position
        when the left button of mouse is pressed.

        (The events are checked on each cycle fixed by `Frame._fps_average`.)

        :param timer_handler: function ((int >= 0, int >= 0)) -> *
        """
        assert callable(mouse_handler), type(mouse_handler)

        self._mousedrag_handler = mouse_handler


    def start(self):
        """
        Start the frame and these handler events.

        **This function is blocking
        until `Frame.stop()` execution or closing window.**
        """
        self._running = True

        mouse_drag_out_of_canvas = None

        clock = pygame.time.Clock()

        # Core of the drawing canvas and dealing events
        while self._running:
            # Draw canvas
            self._canvas._draw()


            # Save canvas images
            while Frame._save_canvas_requests:
                self._canvas._save(Frame._save_canvas_requests.pop(0))


            # Check events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:        # mouse moved
                    if self._mousedrag_handler != None:
                        x = event.pos[0] - self._canvas_x_offset
                        y = event.pos[1] - self._canvas_y_offset
                        if pygame.mouse.get_pressed()[0]:  # left clic
                            if not (0 <= x < self._canvas._width) or not (0 <= y < self._canvas._height):  # out of canvas
                                mouse_drag_out_of_canvas = True

                            if not mouse_drag_out_of_canvas:  # in canvas and not out of canvas since last mouse left button pressed
                                self._draw_statusmouse((x, y), True)
                                self._mousedrag_handler((x, y))
                elif event.type == pygame.MOUSEBUTTONDOWN:  # mouse button pressed
                    if event.button == 1:  # left clic
                        if ((0 <= event.pos[0] - self._canvas_x_offset < self._canvas._width)
                            and (0 <= event.pos[1] - self._canvas_y_offset < self._canvas._height)):  # in canvas
                            mouse_drag_out_of_canvas = False

                        if event.pos[0] < self._canvas_x_offset:  # in control panel
                            control = self._pos_in_control(event.pos[0] - self._border_size, event.pos[1] - self._canvas_y_offset)
                            if control != None:
                                control._mouse_left_button(True)
                            elif self._control_selected != None:
                                self._control_selected = None
                                self._draw_controlpanel()
                        elif self._control_selected != None:
                            self._control_selected = None
                            self._draw_controlpanel()
                elif event.type == pygame.MOUSEBUTTONUP:    # mouse button released
                    if event.button == 1:  # left clic
                        x = event.pos[0] - self._canvas_x_offset
                        y = event.pos[1] - self._canvas_y_offset
                        if (0 <= x < self._canvas._width) and (0 <= y < self._canvas._height):  # in canvas
                            if self._mouseclic_handler != None:
                                self._draw_statusmouse((x, y), False)
                                self._mouseclic_handler((x, y))
                        elif x < 0:                                                             # in control panel
                            control = self._pos_in_control(event.pos[0] - self._border_size, y)
                            if control != None:
                                control._mouse_left_button(False)
                elif event.type == pygame.KEYDOWN:          # key pressed
                    if (self._control_selected != None) and isinstance(self._control_selected, TextAreaControl):
                        self._control_selected._key(event, True)
                    elif self._keydown_handler != None:
                        key = _pygamekey_to_simpleguikey(event.key)
                        self._draw_statuskey(key, True)
                        self._keydown_handler(key)
                elif event.type == pygame.KEYUP:            # key released
                    if (self._control_selected != None) and isinstance(self._control_selected, TextAreaControl):
                        self._control_selected._key(event, False)
                    elif self._keyup_handler != None:
                        key = _pygamekey_to_simpleguikey(event.key)
                        self._draw_statuskey(key, False)
                        self._keyup_handler(key)
                elif event.type == pygame.QUIT:             # quit
                    self.stop()


            # Wait (if necessary) next cycle
            self._fps_average = clock.get_fps()
            clock.tick(Frame._fps)
            #clock.tick_busy_loop(Frame._fps)


        self.stop()

        while Frame._save_canvas_requests:
            self._canvas._save(Frame._save_canvas_requests.pop(0))

        Frame._already_frame = False

        pygame.display.quit()


    def stop(self):
        """
        Stop frame activities.

        If Frame._keep_timers and there is still running timers
        then ask in the canvas if they must be stopped.

        (Available in SimpleGUI of CodeSkulptor
        but *don't in CodeSkulptor documentation*!)
        """
        if (Frame._keep_timers == True) or (Frame._keep_timers == False) or not Timer._timers_running:
            if Frame._keep_timers == False:
                Timer._stop_all()

            self._running = False
        else:
            def check_key(key):
                """
                If key is 'Y'
                then stop all timers and stop the frame.

                If key is 'N'
                then stop the frame.

                :param key: int >= 0
                """
                if key == KEY_MAP['Y']:
                    Timer._stop_all()
                    self._running = False
                elif key == KEY_MAP['N']:
                    self._running = False


            def draw_ask(canvas):
                """
                Draw request about running timers.

                :param canvas: simpleguics2pygame.Canvas
                """
                nb = len(Timer._timers_running)
                if nb == 0:
                    self._running = False

                size = 20
                canvas.draw_text('Stop {} running timer{}?'.format(nb, ('s' if nb >= 2
                                                                        else '')),
                                 (10, 10 + size*3/4), size, 'Black')
                canvas.draw_text('(Yes/No)',
                                 (10, 10 + size*7/4), size, 'Black')


            self._keydown_handler = None
            self._keyup_handler = None

            self._mouseclic_handler = None
            self._mousedrag_handler = None

            Frame._hide_status = True
            self._controls = []
            self._draw_controlpanel()

            self.set_draw_handler(draw_ask)
            self.set_canvas_background('White')

            self.set_keyup_handler(check_key)



class Image:
    """
    Image similar to SimpleGUI `Image` of CodeSkulptor.
    """

    _dir_search_first = '_img/'
    """
    `load_image()` try **first** to loading image from this directory,
    and next if failed, try to loading from URL.
    """

    def __init__(self, url):
        """
        Set an image.

        **Don't use directly**, use `load_image()`.

        :param url: str
        """
        assert _PYGAME_AVAILABLE
        assert isinstance(url, str), type(url)

        self._pygame_surface = None

        if url == '':
            return

        if Image._dir_search_first != None:
            assert Image._dir_search_first[-1] == '/'

            from os.path import isfile

            filename = Image._dir_search_first + url.split('/')[-1]

            if isfile(filename):
                self._pygame_surface = pygame.image.load(filename)

                return

        from io import BytesIO
        from sys import version_info

        if version_info[0] >= 3:
            from urllib.request import urlopen
        else:
            from urllib2 import urlopen

        try:
            url = urlopen(url)
            url = BytesIO(url.read())
        except Exception as e:
            pass

        try:
            self._pygame_surface = pygame.image.load(url)
        except Exception as e:
            pass


    def __repr__(self):
        """
        Return `'<Image object>'`.

        :return: str
        """
        return '<Image object>'


    def get_height(self):
        """
        Return the height ot this image.

        (If initialization of this image was failed
        then return `0`.)

        :return: int
        """
        return (self._pygame_surface.get_height() if self._pygame_surface != None
                else 0)


    def get_width(self):
        """
        Return the width ot this image.

        (If initialization of this image was failed
        then return `0`.)

        :return: int
        """
        return (self._pygame_surface.get_width() if self._pygame_surface != None
                else 0)



class Sound:
    """
    Sound similar to SimpleGUI `Sound` of CodeSkulptor.
    """

    _load_disabled = False
    """
    If `True`
    then load sounds are disabled.
    """

    _dir_search_first = '_snd/'
    """
    `load_sound()` try **first** to loading sound from this directory,
    and next if failed, try to loading from URL.
    """

    def __init__(self, url):
        """
        Set a sound.

        **Don't use directly**, use `load_sound()`.

        :param url: str
        """
        assert _PYGAME_AVAILABLE
        assert isinstance(url, str), type(url)

        self._pygame_channel = None
        self._pygame_sound = None

        if Sound._load_disabled or (url[-4:].lower() not in ('.ogg', '.wav')):
            return

        if Sound._dir_search_first != None:
            assert Sound._dir_search_first[-1] == '/'

            from os.path import isfile

            filename = Image._dir_search_first + url.split('/')[-1]

            if isfile(filename):
                self._pygame_sound = pygame.mixer.Sound(filename)

                return

        from io import BytesIO
        from sys import version_info

        if version_info[0] >= 3:
            from urllib.request import urlopen
        else:
            from urllib2 import urlopen

        try:
            url = urlopen(url)
            url = BytesIO(url.read())
        except Exception as e:
            pass

        try:
            self._pygame_sound = pygame.mixer.Sound(url)
        except Exception as e:
            pass


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

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :return: int or float
        """
        return (self._pygame_sound.get_length() if (self._pygame_sound != None)
                else 0)


    def pause(self):
        """
        Pause this sound.
        (Use `Sound.play()` to resume.)
        """
        if (self._pygame_channel != None) and (self._pygame_channel.get_sound() == self._pygame_sound):
            self._pygame_channel.pause()


    def play(self):
        """
        If this sound is paused
        then resume the sound,
        else start the sound.
        """
        if self._pygame_channel != None:
            if self._pygame_channel.get_sound() == self._pygame_sound:
                self._pygame_channel.unpause()
            else:
                self._pygame_channel = self._pygame_sound.play()
        elif self._pygame_sound != None:
            self._pygame_channel = self._pygame_sound.play()


    def rewind(self):
        """
        If this sound has already been started
        then stop the sound and rewind to the begining.
        """
        if (self._pygame_channel != None) and (self._pygame_channel.get_sound() == self._pygame_sound):
            self._pygame_sound.stop()


    def set_volume(self, volume):
        """
        Change the volume of this sound.
        The default volume is `1` (maximum).

        :param volume: 0 <= int or float <= 1
        """
        assert isinstance(volume, int) or isinstance(volume, float), type(volume)
        assert 0 <= volume <= 1, volume

        if self._pygame_sound != None:
            self._pygame_sound.set_volume(volume)



class TextAreaControl:
    """
    TextAreaControl similar to SimpleGUI `TextAreaControl` (input) of CodeSkulptor.
    """

    _input_background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
                                      else None)
    """
    `pygame.Color` of the background in the input box.
    """

    _input_mark_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['lime'] if _PYGAME_AVAILABLE
                                else None)
    """
    `pygame.Color` of the end mark of text in the input box.
    """

    _input_padding_x = 5
    """
    Horizontal padding in the input box.
    """

    _input_padding_y = 3
    """
    Vertical padding in the input box.
    """

    _input_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['black'] if _PYGAME_AVAILABLE
                           else None)
    """
    `pygame.Color` of the text in the input box.
    """

    _input_pygame_font = Control._label_pygame_font
    """
    `pygame.Font` of the text in the input box.
    """

    _input_selected_background_pygame_color = (_SIMPLEGUICOLOR_TO_PYGAMECOLOR['white'] if _PYGAME_AVAILABLE
                                               else None)
    """
    `pygame.Color` of the background in the input box when it has focus.
    """

    _label_text_pygame_color = Control._label_text_pygame_color
    """
    `pygame.Color` of the label of the input box.
    """

    _label_pygame_font = _input_pygame_font
    """
    `pygame.Font` of the label of the input box.
    """

    def __init__(self,
                 frame,
                 text,
                 input_handler, input_width):
        """
        Set a input box in the control panel.

        **Don't use directly**, use `Frame.add_input()`.

        :param frame: Frame
        :param text: str
        :param input_handler: function (str) -> *
        :param input_width: int or float
        """
        assert _PYGAME_AVAILABLE
        assert isinstance(frame, Frame), type(frame)
        assert isinstance(text, str), type(text)
        assert callable(input_handler), type(input_handler)
        assert isinstance(input_width, int) or isinstance(input_width, float), type(input_width)

        self._frame_parent = frame

        self._text = text
        self._input_handler = input_handler
        self._width = (int(round(input_width)) if input_width >= 0
                       else frame._control_width)

        self._x1 = 0
        self._y1 = (frame._controls[-1]._y2 + 2 if frame._controls
                    else 0)
        self._x2 = None
        self._y2 = None

        self._text_input = ''


    def __repr__(self):
        """
        Return `'<TextAreaControl object>'`.

        :return: str
        """
        return '<TextAreaControl object>'


    def _draw(self):
        """
        Draw the input box and his label.

        **(Don't available in SimpleGUI of CodeSkulptor.)**
        """
        # Display the label
        pygame_surface_text = TextAreaControl._label_pygame_font.render(self._text.strip(),
                                                                        True,
                                                                        TextAreaControl._label_text_pygame_color)

        label_width, label_height = pygame_surface_text.get_size()

        self._frame_parent._controlpanel_pygame_surface.blit(pygame_surface_text,
                                                             (self._x1, self._y1))


        # Display the input text in the input box
        selected = (self._frame_parent._control_selected == self)

        pygame_surface_text = TextAreaControl._input_pygame_font.render(self._text_input,
                                                                        True,
                                                                        TextAreaControl._input_pygame_color)

        text_width, text_height = pygame_surface_text.get_size()

        rect_y = self._y1 + label_height + 2
        rect_height = text_height + 2 + TextAreaControl._input_padding_y*2

        pygame.draw.rect(self._frame_parent._controlpanel_pygame_surface,
                         (TextAreaControl._input_selected_background_pygame_color if selected
                          else TextAreaControl._input_background_pygame_color),
                         (self._x1, rect_y,
                          self._width, rect_height),
                         0)
        pygame.draw.rect(self._frame_parent._controlpanel_pygame_surface,
                         TextAreaControl._input_pygame_color,
                         (self._x1, rect_y,
                          self._width, rect_height),
                         1)

        text_x = self._x1 + 1 + TextAreaControl._input_padding_x
        text_y = rect_y + 1 + TextAreaControl._input_padding_y

        max_text_width = self._width - 2 - TextAreaControl._input_padding_x*2
        offset_text_x = max(0, text_width - max_text_width)
        text_width = min(text_width, max_text_width)

        self._frame_parent._controlpanel_pygame_surface.blit(pygame_surface_text,
                                                             (text_x, text_y),
                                                             (offset_text_x, 0,
                                                              text_width, text_height))

        if selected:
            text_x += text_width + 1
            pygame.draw.line(self._frame_parent._controlpanel_pygame_surface,
                             self._input_mark_pygame_color,
                             (text_x, text_y),
                             (text_x, text_y + text_height), 2)


        # Set bottom-right position
        self._x2 = self._x1 + max(label_width, self._width)
        self._y2 = rect_y + rect_height


    def _key(self, pygame_event, pressed):
        """
        Deal key pressed
        when this `TextAreaControl` have focus.

        If `pressed`
        then add character to text in the input box.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param pygame_event: pygame.Event KEYDOWN or KEYUP
        :param pressed: bool
        """
        assert isinstance(pressed, bool), type(pressed)

        if pressed:
            old = self._text_input
            if (pygame_event.key == pygame.K_RETURN) or (pygame_event.key == 271):  # Return
                # Valid text and run handler
                self._frame_parent._control_selected = None
                self._frame_parent._draw_controlpanel()
                self._input_handler(self._text_input)

                return
            elif pygame_event.key == pygame.K_BACKSPACE:                            # Backspace
                # Delete last character
                self._text_input = self._text_input[:(self._text_input.rstrip().rfind(' ') + 1
                                                      if pygame_event.mod & pygame.KMOD_CTRL
                                                      else -1)]
            elif pygame_event.key == pygame.K_TAB:                                  # Tab
                # Give focus to the next input box (if exist)
                i = 0
                while self._frame_parent._controls[i] != self:
                    i += 1
                i += 1
                while ((i < len(self._frame_parent._controls))
                       and not isinstance(self._frame_parent._controls[i], TextAreaControl)):
                    i += 1

                self._frame_parent._control_selected = (self._frame_parent._controls[i]
                                                        if i < len(self._frame_parent._controls)
                                                        else None)
                self._frame_parent._draw_controlpanel()

                return
            else:                                                                   # other key
                # Add character
                self._text_input += pygame_event.unicode

            if self._text_input != old:
                try:
                    # Maybe self._text_input is unicode, try to convert to str
                    self._text_input = str(self._text_input)
                except:
                    pass

                self._frame_parent._draw_controlpanel()


    def _mouse_left_button(self, pressed):
        """
        Deal a click of left mouse button on the zone of this `TextAreaControl`.

        If `pressed`
        then give it the focus.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param pressed: bool
        """
        assert isinstance(pressed, bool), type(pressed)

        if pressed:
            self._frame_parent._control_selected = self
            self._frame_parent._draw_controlpanel()


    def _pos_in(self, x, y):
        """
        If position (`x`, `y`) is on the zone of this `TextAreaControl`
        then return `True`,
        else return `False`.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        :param x: int or float
        :param y: int or float

        :return: bool
        """
        assert isinstance(x, int) or isinstance(x, float), type(x)
        assert isinstance(y, int) or isinstance(y, float), type(y)

        return ((self._x1 <= x <= self._x2)
                and (self._y1 <= y <= self._y2))


    def get_text(self):
        """
        Return the text of the input box.

        (Available in SimpleGUI of CodeSkulptor
        but *don't in CodeSkulptor documentation*!)

        :return: str (or unicode in Python 2)
        """
        return self._text_input


    def set_text(self, text):
        """
        Change the text in the input box.

        :param text: str
        """
        assert isinstance(text, str), type(text)

        self._text_input = text
        self._frame_parent._draw_controlpanel()



class Timer:
    """
    Timer similar to SimpleGUI `Timer` of CodeSkulptor.

    **Don't require Pygame.**
    """

    _timers_running = {}
    """
    `Dict` {(Timer id): `Timer`} of all timers are running.
    """

    @classmethod
    def _stop_all(cls):
        """
        Stop all timers.

        **(Don't available in SimpleGUI of CodeSkulptor.)**

        Side effect: Empty `Timer._timers_running`.
        """
        for timer in tuple(Timer._timers_running.values()):
            timer.stop()


    def __init__(self, interval, timer_handler):
        """
        Set a time.

        **Don't use directly**, use `create_timer()`.

        :param interval: int or float > 0
        :param timer_handler: function () -> *
        """
        assert isinstance(interval, int) or isinstance(interval, float), type(interval)
        assert interval > 0, interval
        assert callable(timer_handler), type(timer_handler)

        import threading

        def repeat_handler():
            Timer._timers_running[id(self)] = self
            self._timer = threading.Timer(self._interval/1000, self._handler)
            self._timer.start()
            timer_handler()


        self._interval = interval
        self._handler = repeat_handler

        self._is_running = False
        self._timer = None


    def __repr__(self):
        """
        Return `'<Timer object>'`.

        :return: str
        """
        return '<Timer object>'


    def get_interval(self):
        """
        Return the interval of this timer.

        (Available in SimpleGUI of CodeSkulptor
        but *don't in CodeSkulptor documentation*!)

        :return: (int or float) > 0
        """
        return self._interval


    def is_running(self):
        """
        If this timer is running
        then return `True`,
        else return `False`.

        :return: bool
        """
        return self._timer != None


    def start(self):
        """
        Start this timer.

        (Side effect: Add `id(self)`: `self` in `Timer._timers_running`.)
        """
        if self._timer == None:
            import threading

            Timer._timers_running[id(self)] = self
            self._timer = threading.Timer(self._interval/1000, self._handler)
            self._timer.start()


    def stop(self):
        """
        Stop this timer.

        (Side effect: Remove `id(self)` of `Timer. _timers_running`.)
        """
        if self._timer != None:
            self._timer.cancel()
            self._timer = None

            del Timer._timers_running[id(self)]



#
# Private function
###################
def _pos_round(position):
    """
    Returns the rounded `position`.

    **Don't require Pygame.**

    **(Don't available in SimpleGUI of CodeSkulptor.)**

    :param position: (int or float, int or float) or [int or float, int or float]

    :return: (int, int)
    """
    assert isinstance(position, tuple) or isinstance(position, list), type(position)
    assert len(position) == 2, len(position)
    assert isinstance(position[0], int) or isinstance(position[0], float), type(position[0])
    assert isinstance(position[1], int) or isinstance(position[1], float), type(position[1])

    return (int(round(position[0])), int(round(position[1])))


def _pygamekey_to_simpleguikey(key):
    """
    Return the code use by SimpleGUI to representing
    the `key` expressed by Pygame.

    If `key` not in _PYGAMEKEY_TO_SIMPLEGUIKEY
    then return `key`.

    **(Don't available in SimpleGUI of CodeSkulptor.)**

    :param key: int >= 0

    :return: int >= 0
    """
    assert _PYGAME_AVAILABLE
    assert isinstance(key, int), type(key)
    assert key >= 0, key

    return _PYGAMEKEY_TO_SIMPLEGUIKEY.get(key, key)


def _set_option_from_argv():
    """
    Read arguments in sys.argv
    and set options.

    * ``--fullscreen```: Fullscreen mode.
    * ``--keep-timers``: Keep running timers when close frame without ask.
    * ``--no-border``: Window without border.
    * ``--no-controlpanel``: Hide the control panel (and status boxes).
    * ``--no-load-sound``: Don't load any sound.
    * ``--no-status``: Hide two status boxes.
    * ``--stop-timers``: Stop all timers when close frame.

    If an argument not in this list
    then next argument are ignored.

    This function is executed when the module is imported.

    **(Don't available in SimpleGUI of CodeSkulptor.)**
    """
    from sys import argv

    for arg in argv[1:]:
        if arg == '--fullscreen':
            Frame._pygame_mode_flags |= pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
        elif arg == '--keep-timers':
            Frame._keep_timers = True
        elif arg == '--no-border':
            Frame._pygame_mode_flags |= pygame.NOFRAME
        elif arg == '--no-controlpanel':
            Frame._hide_controlpanel = True
        elif arg == '--no-load-sound':
            Sound._load_disabled = True
        elif arg == '--no-status':
            Frame._hide_status = True
        elif arg == '--stop-timers':
            Frame._keep_timers = False
        else:
            break


def _simpleguicolor_to_pygamecolor(color,
                                   default_pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR['red']):
    """
    Return a `pygame.Color` object
    corresponding to the SimpleGUI string `color` in format:

    * '#rrggbb',
    * '#rgb',
    * 'rbg(red,blue,green)',
    * 'rgba(red,blue,green,alpha)'
    * or constant name in `_SIMPLEGUICOLOR_TO_PYGAMECOLOR` \
      (`default_pygame_color` if the constant name are not founded).

    See http://www.opimedia.be/DS/mementos/colors.htm

    :param color: str
    :param default_pygame_color: pygame.Color

    :return: pygame.Color

    **(Don't available in SimpleGUI of CodeSkulptor.)**
    """
    assert _PYGAME_AVAILABLE
    assert isinstance(color, str), type(color)
    assert len(color) > 0
    #assert (((color[0] == '#') and ((len(color) == 4) or (len(color) == 7)))
    #        or (color[:4] == 'rgb(')
    #        or (color[:5] == 'rgba(')
    #        or (color.lower() in _SIMPLEGUICOLOR_TO_PYGAMECOLOR)), color

    if color[0] == '#':        # format #rrggbb or #rgb
        return pygame.Color(color if len(color) == 7
                            else '#' + color[1]*2 + color[2]*2 + color[3]*2)
    elif color[:4] == 'rgb(':  # format rbg(red,blue,green)
        assert color[-1] == ')', color

        color = color[4:-1].split(',')

        assert len(color) == 3, color

        return pygame.Color(max(0, min(255, int(color[0]))),
                            max(0, min(255, int(color[1]))),
                            max(0, min(255, int(color[2]))))
    elif color[:5] == 'rgba(':  # format rbga(red,blue,green,alpha)
        assert color[-1] == ')', color

        color = color[5:-1].split(',')

        assert len(color) == 4, color

        return pygame.Color(max(0, min(255, int(color[0]))),
                            max(0, min(255, int(color[1]))),
                            max(0, min(255, int(color[2]))),
                            max(0, min(255, int(round(float(color[3])*255)))))
    else:                       # constant name
        return _SIMPLEGUICOLOR_TO_PYGAMECOLOR.get(color.lower(),
                                                  default_pygame_color)


def _simpleguifontface_to_pygamefont(font_face, font_size):
    """
    Return a `pygame.Font` object
    corresponding to the SimpleGUI `font_face` name
    by using the `_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME` dictionary.

    If correponding font is not founded,
    then return the default `pygame.Font`.

    **(Don't available in SimpleGUI of CodeSkulptor.)**

    :param font_face: str == key of _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME
    :param size: int > 0

    :return: pygame.Font
    """
    assert isinstance(font_face, str), type(font_face)
    assert font_face in _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME, font_face

    assert isinstance(font_size, int), type(font_size)
    assert font_size > 0, font_size

    try:
        return pygame.font.SysFont(_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME[font_face], font_size)
    except:
        return pygame.font.SysFont(None, font_size)



#
# SimpleGUI functions
######################
def create_frame(title,
                 canvas_width, canvas_height,
                 control_width = 200):
    """
    Create and return an interactive window. ::

    | +-------+
    | | title |
    | +---------+--------------+
    | | control |              |
    | | panel   |    canvas    |
    | |         |              |
    | +---------+--------------+

    | `title`: title of the window.
    | `canvas_width`, canvas_height: dimensions of the canvas.
    | `control_width`: width of the control panel.

    (The frame is inactive until the execution of `Frame.start()`.)

    **Don't run twice!**

    :param title: str
    :param canvas_width: (int or float) >= 0
    :param canvas_height: (int or float) >= 0
    :param control_width: (int or float) >= 0

    :return: Frame
    """
    assert _PYGAME_AVAILABLE
    assert isinstance(title, str), type(title)

    assert isinstance(canvas_width, int) or isinstance(canvas_width, float), type(canvas_width)
    assert canvas_width >= 0, canvas_width

    assert isinstance(canvas_height, int) or isinstance(canvas_height, float), type(canvas_height)
    assert canvas_height >= 0, canvas_height

    assert isinstance(control_width, int) or isinstance(control_width, float), type(control_width)
    assert control_width >= 0, control_width

    return Frame(title, canvas_width, canvas_height, control_width)


def create_invisible_canvas(width, height):
    """
    NOT IMPLEMENTED!
    (Return a "weak" `Canvas`.)

    (Available in SimpleGUI of CodeSkulptor
    but *don't in CodeSkulptor documentation*!)

    :param width: int >= 0
    :param height: int >= 0

    :return: Canvas
    """
    assert isinstance(width, int), type(width)
    assert width >= 0, width

    assert isinstance(height, int), type(height)
    assert height >= 0, height

    return Canvas(None, width, height)


def create_sound(sound_data, sample_rate = 8000, num_channels = 1):
    """
    NOT YET IMPLEMENTED! (Return an empty `Sound`.)

    (Available in SimpleGUI of CodeSkulptor
    but *don't in CodeSkulptor documentation*!)

    :param sound_data: (tuple or list) of (0 <= int < 256)
    :param sample_rate: int >= 0
    :param num_channels: int >= 0

    :return: Sound
    """
    assert _PYGAME_AVAILABLE
    assert isinstance(sound_data, tuple) or isinstance(sound_data, list), type(sound_data)
    if __debug__:
        for data in sound_data:
            assert isinstance(data, int), type(data)
            assert 0 <= data < 256, data

    assert isinstance(sample_rate, int), type(sample_rate)
    assert sample_rate >= 0, sample_rate

    assert isinstance(num_channels, int), type(num_channels)
    assert num_channels >= 0, num_channels

    return Sound('')


def create_timer(interval, timer_handler):
    """
    Create and return a timer
    that will execute the function `timer_handler`
    every `interval` milliseconds.

    The first execution of `time_handler` will take place after the first period.

    (The timer can be started by `Timer.start()`.)

    :param interval: int or float > 0
    :param timer_handler: function () -> *

    :return: Timer
    """
    assert isinstance(interval, int) or isinstance(interval, float), type(interval)
    assert interval > 0, interval
    assert callable(timer_handler), type(timer_handler)

    return Timer(interval, timer_handler)


def load_image(url):
    """
    Create and return an image by loading a file from `url`.
    Not founded file and errors are ignored.

    **Warning**:
    In SimpleGUICS2Pygame:

    * `url` may be also a path of a local file.
      **(In SimpleGUI of CodeSkulptor `url` must be an URL.)**
    * SimpleGUICS2Pygame try **first** to loading image \
        from `Image._dir_search_first` directory, \
        and next if failed, try to loading from `url`.

    Supported formats are supported formats by Pygame to load:
    PNG, JPG, GIF (non animated), ...
    (see http://www.pygame.org/docs/ref/image.html ).

    (CodeSkulptor may supported other formats,
    dependant on browser support.)

    :param url: str

    :return: Image
    """
    assert _PYGAME_AVAILABLE
    assert isinstance(url, str), type(url)

    return Image(url)


def load_sound(url):
    """
    Create and return a sound by loading a file from `url`.
    Not founded file and errors are ignored.

    **Warning**:
    In SimpleGUICS2Pygame:

    * `url` may be also a path of a local file.
      **(In SimpleGUI of CodeSkulptor `url` must be an URL.)**
    * SimpleGUICS2Pygame try **first** to loading sound \
        from `Sound._dir_search_first` directory, \
        and next if failed, try to loading from `url`.

    Supported formats are supported formats by Pygame:
    OGG and uncompressed WAV
    (see http://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound ).

    (CodeSkulptor may supported also MP3,
    dependant on browser support.)

    (The sound can be started by `Sound.play()`.)

    :param url: str

    :return: Sound
    """
    assert _PYGAME_AVAILABLE
    assert isinstance(url, str), type(url)

    return Sound(url)



#
# Set options
##############
_set_option_from_argv()



#
# Main
#######
if __name__ == '__main__':
    from webbrowser import open_new_tab

    WIDTH = 500
    HEIGHT = 260

    def draw_about(canvas):
        """
        Draw a short presentation of this module.

        :param canvas: simpleguics2pygame.Canvas
        """
        size = 40
        canvas.draw_line((0, size/2),
                         (WIDTH - 1, size/2),
                         size*1.3, '#f2f2f2')
        canvas.draw_text('simpleguics2pygame', (10, size*3/4), size, 'Black')
        canvas.draw_image(logo, (32, 32), (64, 64), (WIDTH - 42, HEIGHT - 42), (64, 64))

        size = 20

        for i, line in enumerate(('It is a standard Python (2 and 3) module',
                                  'reimplementing the SimpleGUI particular module',
                                  'of CodeSkulptor (a browser Python interpreter).',
                                  None,
                                  'Require Pygame.',
                                  None,
                                  'GPLv3',
                                  'Copyright (C) 2013 Olivier Pirson',
                                  'Olivier Pirson OPi --- http://www.opimedia.be/',
                                  'olivier_pirson_opi@yahoo.fr')):
            if line != None:
                canvas.draw_text(line, (10, 50 + size*(i + 3/4)), size, 'Black')


    logo = load_image('https://bitbucket-assetroot.s3.amazonaws.com/c/photos/2013/Jun/09/simpleguics2pygame-logo-4079748489-6_avatar.png')

    frame = create_frame('SimpleGUICS2Pygame: short presentation of this module', WIDTH, HEIGHT, 160)
    frame.set_canvas_background('White')

    frame.add_label('Go to websites:')
    frame.add_button('SimpleGUICS2Pygame', lambda: open_new_tab(_WEBSITE), 160)
    frame.add_button('Olivier Pirson OPi', lambda: open_new_tab('http://www.opimedia.be/'), 160)

    frame.add_label('')
    frame.add_button('CodeSkulptor', lambda: open_new_tab('http://www.codeskulptor.org/'), 160)
    frame.add_button('Pygame', lambda: open_new_tab('http://www.pygame.org/'), 160)

    frame.add_label('')
    frame.add_button('GPL', lambda: open_new_tab('http://www.gnu.org/licenses/gpl.html'), 160)

    frame.add_label('')
    frame.add_label('')
    frame.add_button('Quit', lambda: frame.stop())

    frame.set_draw_handler(draw_about)

    frame.start()
