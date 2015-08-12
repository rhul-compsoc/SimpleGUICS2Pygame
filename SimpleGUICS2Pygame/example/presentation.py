#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
presentation (August 12, 2015)

Little application that draw
a short presentation of SimpleGUICS2Pygame package.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2015 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import simplegui

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True

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

        from SimpleGUICS2Pygame import _VERSION, _WEBSITE
    else:
        def open_new_tab(url):
            """
            Fake replacement of webbrowser.open_new_tab() function.
            """
            print(url)

        _VERSION = ''
        _WEBSITE = 'https://bitbucket.org/OPiMedia/simpleguics2pygame'

    WIDTH = 560
    HEIGHT = 360

    def draw_about_handler(canvas):
        """
        Draw a short presentation of this package.

        :param canvas: simplegui.Canvas
        """
        size = 40
        canvas.draw_line((0, size/2),
                         (WIDTH - 1, size/2),
                         size*1.75, '#f2f2f2')
        canvas.draw_text('SimpleGUICS2Pygame ' + _VERSION,
                         (10, size), size, 'Black')
        canvas.draw_image(logo_opi, (20.5, 17), (41, 34),
                          (30.5, HEIGHT - 27), (41, 34))
        canvas.draw_image(logo_gpl, (44, 15.5), (88, 31),
                          (WIDTH/2, HEIGHT - 25.5), (88, 31))
        canvas.draw_image(logo, (32, 32), (64, 64),
                          (WIDTH - 42, HEIGHT - 42), (64, 64))

        size = 20

        for i, line in enumerate(
            ('It is primarily a standard Python (2 and 3) module',
             'reimplementing the SimpleGUI particular module',
             'of CodeSkulptor (a browser Python interpreter).',
             None,
             'Require malplotlib for simpleplot.',
             'Require Pygame for simpleguics2pygame.',
             None,
             'GPLv3',
             'Copyright (C) 2013, 2014, 2015 Olivier Pirson',
             'Olivier Pirson OPi --- http://www.opimedia.be/',
             'olivier_pirson_opi@yahoo.fr')):
            if line is not None:
                canvas.draw_text(line, (10, 80 + size*(i + 3/4)),
                                 size, 'Black')

    if SIMPLEGUICS2PYGAME:
        from os.path import dirname, join
        from sys import argv

        logo = simplegui._load_local_image(
            join(dirname(argv[0]),
                 '../_img/SimpleGUICS2Pygame_64x64_t.png'))
        logo_opi = simplegui._load_local_image(join(dirname(argv[0]),
                                                    '../_img/OPi_t.png'))
        logo_gpl = simplegui._load_local_image(join(dirname(argv[0]),
                                                    '../_img/gplv3-88x31.png'))
    else:
        logo = simplegui.load_image('https://bytebucket.org/OPiMedia/simpleguics2pygame/raw/f14013a6fe7d1923159f4b1aad1331a483a04556/SimpleGUICS2Pygame/_img/SimpleGUICS2Pygame_64x64_t.png')
        logo_opi = simplegui.load_image('https://bytebucket.org/OPiMedia/simpleguics2pygame/raw/f14013a6fe7d1923159f4b1aad1331a483a04556/SimpleGUICS2Pygame/_img/OPi_t.png')
        logo_gpl = simplegui.load_image('https://bytebucket.org/OPiMedia/simpleguics2pygame/raw/f14013a6fe7d1923159f4b1aad1331a483a04556/SimpleGUICS2Pygame/_img/gplv3-88x31.png')

    frame = simplegui.create_frame(
        'SimpleGUICS2Pygame: short presentation of this package',
        WIDTH, HEIGHT)
    frame.set_canvas_background('White')

    frame.add_label('Go to websites:')
    frame.add_button('SimpleGUICS2Pygame',
                     lambda: open_new_tab(_WEBSITE), 180)
    frame.add_button('Olivier Pirson OPi',
                     lambda: open_new_tab('http://www.opimedia.be/'), 180)
    frame.add_button('Donate',
                     lambda: open_new_tab('http://www.opimedia.be/donate'),
                     180)

    frame.add_label('')
    frame.add_button('CodeSkulptor',
                     lambda: open_new_tab('http://www.codeskulptor.org/'), 180)
    frame.add_button('matplolib',
                     lambda: open_new_tab('http://matplotlib.org/'), 180)
    frame.add_button('Pygame',
                     lambda: open_new_tab('http://www.pygame.org/'), 180)

    frame.add_label('')
    frame.add_button('GPL',
                     lambda: open_new_tab(
                         'http://www.gnu.org/licenses/gpl.html'),
                     180)

    frame.add_label('')
    frame.add_button('Quit', frame.stop)

    if SIMPLEGUICS2PYGAME:
        frame.add_label('')
        frame.add_label('Pygame ' + simplegui._PYGAME_VERSION)
        frame.add_label('')
        frame.add_label('Python ' + version)

    frame.set_draw_handler(draw_about_handler)

    frame.start()


#
# Main
######
if __name__ == '__main__':
    if SIMPLEGUICS2PYGAME and not simplegui._PYGAME_AVAILABLE:
        print("""Pygame not available!
See http://simpleguics2pygame.readthedocs.org/en/latest/#installation""")

        exit(1)

    main()
