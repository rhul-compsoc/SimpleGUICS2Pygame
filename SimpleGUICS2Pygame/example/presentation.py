#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
presentation.

Little application that draw
a short presentation of SimpleGUICS2Pygame package.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2016, 2018, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: March 24, 2020
"""

try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access

    SIMPLEGUICS2PYGAME = True


#
# Main function
###############
def main():
    """
    Main function.
    """
    if SIMPLEGUICS2PYGAME:
        from sys import version
        from webbrowser import open_new_tab

        from SimpleGUICS2Pygame import _VERSION, _WEBSITE, _WEBSITE_DOC
    else:
        def open_new_tab(url):
            """
            Fake replacement of webbrowser.open_new_tab() function.
            """
            print(url)

        _VERSION = ''  # pylint: disable=invalid-name
        _WEBSITE = 'https://bitbucket.org/OPiMedia/simpleguics2pygame/'  # noqa  # pylint: disable=invalid-name
        _WEBSITE_DOC = 'https://simpleguics2pygame.readthedocs.io/'  # noqa  # pylint: disable=invalid-name

    width = 560
    height = 490

    def draw_about_handler(canvas):
        """
        Draw a short presentation of this package.

        :param canvas: simplegui.Canvas
        """
        size = 40
        canvas.draw_line((0, size / 2),
                         (width - 1, size / 2),
                         size * 1.75, '#f2f2f2')
        canvas.draw_text('SimpleGUICS2Pygame ' + _VERSION,
                         (10, size), size, 'Black')
        canvas.draw_image(logo_opi, (20.5, 17), (41, 34),
                          (30.5, height - 27), (41, 34))
        canvas.draw_image(logo_gpl, (44, 15.5), (88, 31),
                          (width / 2, height - 25.5), (88, 31))
        canvas.draw_image(logo, (32, 32), (64, 64),
                          (width - 42, height - 42), (64, 64))

        size = 20

        for i, line in enumerate(
                ('It is primarily a standard Python (2 and 3) module',
                 'reimplementing the SimpleGUI particular module',
                 'of CodeSkulptor (a Python browser environment).',
                 'This is in fact a package also with other modules',
                 'adapted from CodeSkulptor.',
                 None,
                 'Require malplotlib for simpleplot.',
                 'Require Pygame for simpleguics2pygame.',
                 None,
                 'GPLv3',
                 'Copyright (C) 2013 - 2020 Olivier Pirson',
                 'Olivier Pirson OPi --- http://www.opimedia.be/',
                 'olivier.pirson.opi@gmail.com')):
            if line is not None:
                canvas.draw_text(line, (10, 80 + size * (i + 3 / 4)),
                                 size, 'Black')

    if SIMPLEGUICS2PYGAME:
        from os.path import dirname, join
        from sys import argv

        logo = simplegui._load_local_image(  # noqa  # pylint: disable=protected-access,no-member
            join(dirname(argv[0]),
                 '../_img/SimpleGUICS2Pygame_64x64_t.png'))
        logo_opi = simplegui._load_local_image(join(dirname(argv[0]),  # noqa  # pylint: disable=protected-access,no-member
                                                    '../_img/OPi_t.png'))
        logo_gpl = simplegui._load_local_image(join(dirname(argv[0]),  # noqa  # pylint: disable=protected-access,no-member
                                                    '../_img/gplv3-88x31.png'))
    else:
        logo = simplegui.load_image('https://bitbucket.org/OPiMedia/simpleguics2pygame/raw/42359d3aa63aa0b6ea2c663652a60579c7ba80f8/SimpleGUICS2Pygame/_img/SimpleGUICS2Pygame_64x64_t.png')  # noqa
        logo_opi = simplegui.load_image('https://bitbucket.org/OPiMedia/simpleguics2pygame/raw/42359d3aa63aa0b6ea2c663652a60579c7ba80f8/SimpleGUICS2Pygame/_img/OPi_t.png')  # noqa
        logo_gpl = simplegui.load_image('https://bitbucket.org/OPiMedia/simpleguics2pygame/raw/42359d3aa63aa0b6ea2c663652a60579c7ba80f8/SimpleGUICS2Pygame/_img/gplv3-88x31.png')  # noqa

    frame = simplegui.create_frame(
        'SimpleGUICS2Pygame: short presentation of this package',
        width, height)
    frame.set_canvas_background('White')

    frame.add_label('Go to websites:')
    frame.add_button('SimpleGUICS2Pygame',
                     lambda: open_new_tab(_WEBSITE), 180)
    frame.add_button('online documentation',
                     lambda: open_new_tab(_WEBSITE_DOC), 180)
    frame.add_button('Olivier Pirson OPi',
                     lambda: open_new_tab('http://www.opimedia.be/'), 180)
    frame.add_button('Donate',
                     lambda: open_new_tab('http://www.opimedia.be/donate'),
                     180)

    frame.add_label('')
    frame.add_button('CodeSkulptor',
                     lambda: open_new_tab('http://www.codeskulptor.org/'), 180)
    frame.add_button('CodeSkulptor3',
                     lambda: open_new_tab('https://py3.codeskulptor.org/'),
                     180)

    frame.add_label('')
    frame.add_button('Pygame',
                     lambda: open_new_tab('https://www.pygame.org/'), 180)
    frame.add_button('audioread',
                     lambda: open_new_tab(
                         'https://github.com/beetbox/audioread'),
                     180)
    frame.add_button('matplolib',
                     lambda: open_new_tab('https://matplotlib.org/'), 180)

    frame.add_label('')
    frame.add_button('GPL',
                     lambda: open_new_tab(
                         'https://www.gnu.org/licenses/gpl-3.0.html'),
                     180)

    frame.add_label('')
    frame.add_button('Quit', frame.stop)

    if SIMPLEGUICS2PYGAME:
        frame.add_label('')
        frame.add_label('Pygame ' + simplegui._PYGAME_VERSION)  # noqa  # pylint: disable=protected-access,no-member
        frame.add_label('')
        frame.add_label('Python ' + version)

    frame.set_draw_handler(draw_about_handler)

    frame.start()


#
# Main
######
if __name__ == '__main__':
    if SIMPLEGUICS2PYGAME and not simplegui._PYGAME_AVAILABLE:  # noqa  # pylint: disable=protected-access,no-member
        print("""Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation""")

        exit(1)

    main()
