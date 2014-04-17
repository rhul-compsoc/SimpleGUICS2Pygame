# -*- coding: latin-1 -*-

"""
simplegui_lib_keys (April 17, 2014)

A class to help manage keyboard handling
in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2014 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# Class
########
class Keys:
    """
    Keys handler.

    Set and catch keys handlers of SimpleGUICS2Pygame (and CodeSkulptor)
    to help.

    General note:
    Some keyboards can't handle more
    than two or three keys pressed simultaneously.
    See `Keyboard Ghosting Explained!`_
    and `Keyboard Ghosting Demonstration`_.

    .. _`Keyboard Ghosting Explained!`: http://www.microsoft.com/appliedsciences/antighostingexplained.mspx
    .. _`Keyboard Ghosting Demonstration`: http://www.microsoft.com/appliedsciences/content/projects/KeyboardGhostingDemo.aspx
    """

    def __init__(self, frame, keys=None):
        """
        If keys is None
        then set an empty keys handler,
        else set a keys handler with key up and key down functions of keys.

        `active_handlers()`,
        `active_keydown_handler()` or `active_keyup_handler()`
        must be called to activate.

        :param frame: simplegui.Frame
        :param keys: None or Keys
        """
        assert isinstance(frame, simplegui.Frame), type(frame)
        assert (keys is None) or isinstance(keys, Keys), type(keys)

        self._frame = frame
        self._pressed_keys = {}

        if keys is None:
            self._keydown_fct = {}
            self._keyup_fct = {}
        else:
            self._keydown_fct = dict(self._keydown_fct)
            self._keyup_fct = dict(self._keyup_fct)

    def active_handlers(self):
        """
        Active key down and key up handlers.
        """
        self.active_keydown_handler()
        self.active_keyup_handler()

    def active_keydown_handler(self):
        """
        Active the key down handler.
        """
        def keydown(key_code):
            self._pressed_keys[key_code] = True

            fct = self._keydown_fct.get(key_code)
            if fct is not None:
                fct(key_code)

        self._frame.set_keydown_handler(keydown)

    def active_keyup_handler(self):
        """
        Active the key up handler.
        """
        def keyup(key_code):
            if key_code in self._pressed_keys:
                del self._pressed_keys[key_code]

            fct = self._keyup_fct.get(key_code)
            if fct is not None:
                fct(key_code)

        self._frame.set_keyup_handler(keyup)

    def is_pressed(self, key_code):
        """
        If the key is pressed
        then return True,
        else return False.

        :param key_code: int >= 0

        :return: bool
        """
        assert isinstance(key_code, int), type(key_code)
        assert key_code >= 0, key_code

        return self._pressed_keys.get(key_code, False)

    def is_pressed_key_map(self, key_str):
        """
        If the key is pressed
        then return True,
        else return False.

        :param key_str: str in `simplegui.KEY_MAP`

        :return: bool
        """
        assert isinstance(key_str, str), type(key_str)
        assert key_str in simplegui.KEY_MAP, key_str

        return self._pressed_keys.get(simplegui.KEY_MAP[key_str], False)

    def pressed_keys(self):
        """
        Return a sorted list with code of all pressed keys.

        :return: list of (int >= 0)
        """
        return list(self._pressed_keys.keys())

    def set_keydown_fct(self, key_code, fct=None):
        """
        If fct is None
        then erase the function key down handler to the specified key,
        else set the function key down handler to the specified key.

        :param key_code: int >= 0
        """
        assert isinstance(key_code, int), type(key_code)
        assert key_code >= 0, key_code

        if fct is None:
            if key_code in self._keydown_fct:
                del self._keydown_fct.pop[key_code]
        else:
            self._keydown_fct[key_code] = fct

    def set_keydown_fct_key_map(self, key_str, fct=None):
        """
        If fct is None
        then erase the function key down handler to the specified key,
        else set the function key down handler to the specified key.

        :param key_str: str in `simplegui.KEY_MAP`

        :param key_code: int >= 0
        """
        assert isinstance(key_str, str), type(key_str)
        assert key_str in simplegui.KEY_MAP, key_str

        self.set_keydown_fct(simplegui.KEY_MAP[key_str], fct=fct)

    def set_keyup_fct(self, key_code, fct=None):
        """
        If fct is None
        then erase the function key up handler to the specified key,
        else set the function key up handler to the specified key.

        :param key_code: int >= 0
        """
        assert isinstance(key_code, int), type(key_code)
        assert key_code >= 0, key_code

        if fct is None:
            if key_code in self._keyup_fct:
                del self._keyup_fct.pop[key_code]
        else:
            self._keyup_fct[key_code] = fct

    def set_keyup_fct_key_map(self, key_str, fct=None):
        """
        If fct is None
        then erase the function key up handler to the specified key,
        else set the function key up handler to the specified key.

        :param key_str: str in `simplegui.KEY_MAP`

        :param key_code: int >= 0
        """
        assert isinstance(key_str, str), type(key_str)
        assert key_str in simplegui.KEY_MAP, key_str

        self.set_keyup_fct(simplegui.KEY_MAP[key_str], fct=fct)
