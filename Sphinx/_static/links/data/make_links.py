#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Module
  to make_img_snd_links.py
  and make_prog_links.py .
(June 22, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import print_function


import os.path


def print_html_list_img(data, dest_file):
    """
    Print data as HTML <ul> in dest_file.

    :param data: List as builded by read_txt()
    :param file: file open in writing
    """
    assert isinstance(data, list), type(data)

    print('<ul>', file=dest_file)

    for items in data:
        assert isinstance(items, list), type(items)
        assert len(items) > 0

        if len(items) == 0:
            continue

        assert isinstance(items[0], str), type(items[0])

        print("""  <li>
    {}
    <div class="images">""".format(items[0]), file=dest_file)

        for url, info, info2 in items[1:]:
            assert isinstance(url, str), type(url)
            assert isinstance(info, str), type(info)

            if info == '':
                info = '<tt>{}</tt>'.format(os.path.basename(url))

            print("""      <a class="image" href="{0}" target="_blank" onmouseover="img_load(this, '{0}');"><img src="#" alt="[Loading&hellip;]"><span class="size"><span></span></span>
        {1}
      </a>""".format(url, info), file=dest_file)

        print("""    </div>
  </li>""", file=dest_file)

    print('</ul>', file=dest_file)


def print_html_list_link(data, dest_file):
    """
    Print data as HTML <ul> in dest_file.

    :param data: List as builded by read_txt()
    :param dest_file: file open in writing
    """
    assert isinstance(data, list), type(data)

    print('<ul>', file=dest_file)

    for items in data:
        assert isinstance(items, list), type(items)
        assert len(items) > 0

        if len(items) == 0:
            continue

        assert isinstance(items[0], str), type(items[0])

        print("""  <li>
    {}
    <div class="progs">""".format(items[0]), file=dest_file)

        for url, info, info2 in items[1:]:
            assert isinstance(url, str), type(url)
            assert isinstance(info, str), type(info)

            if info == '':
                info = '<tt>{}</tt>'.format(os.path.basename(url))

            print("""      <div class="prog">
        <a href="{0}" target="_blank">{1}</a>{2}
      </div>""".format(url, info, ('<span class="info2-attention">&hellip;</span> <div class="info2">{}</div>'.format(info2) if info2 != ''
                                   else '')), file=dest_file)

        print("""    </div>
  </li>""", file=dest_file)

    print('</ul>', file=dest_file)


def print_html_list_snd(data, dest_file):
    """
    Print data as HTML <ul> in dest_file.

    :param data: List as builded by read_txt()
    :param dest_file: file open in writing
    """
    assert isinstance(data, list), type(data)

    print('<ul>', file=dest_file)

    for items in data:
        assert isinstance(items, list), type(items)
        assert len(items) > 0

        if len(items) == 0:
            continue

        assert isinstance(items[0], str), type(items[0])

        print("""  <li>
    {}
    <div class="sounds">""".format(items[0]), file=dest_file)

        for url, info, info2 in items[1:]:
            assert isinstance(url, str), type(url)
            assert isinstance(info, str), type(info)

            if info == '':
                info = '<tt>{}</tt>'.format(os.path.basename(url))

            print("""      <div class="sound">
        <a href="{0}" target="_blank">{1}</a>
        <audio src="{0}" controls="controls"></audio>
      </div>""".format(url, info), file=dest_file)

        print("""    </div>
  </li>""", file=dest_file)

    print('</ul>', file=dest_file)


def read_txt(filename):
    """
    Read filename and build a list to use with print_html_list_*().

    :param filename: str

    :returns: List of [str, [str, str, str]*]
    """
    assert isinstance(filename, str), type(filename)

    data = []

    f = open(filename)
    lines = [line.strip() for line in f]
    f.close()

    acc = []

    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1

        if line == '':
            continue

        if line[:2] == '+ ':
            line = line[2:]
            if len(acc) > 0:
                data.append(acc)
            acc = [line]
        else:
            triplet = [line, '', '']

            if i < len(lines):
                triplet[1] = lines[i]
                i += 1

            if (i < len(lines)) and (triplet[1] != ''):
                triplet[2] = lines[i]
                i += 1

            acc.append(triplet)

    if len(acc) > 0:
        data.append(acc)

    return data
