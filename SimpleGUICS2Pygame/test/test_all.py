#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test all other test_*.py. (December 13, 2013)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import print_function

import datetime
import glob
import os
import os.path
import sys

try:
    import PIL.Image
    import PIL.ImageChops
    import PIL.ImageStat

    to_compare_imgs = True
except ImportError:
    to_compare_imgs = False

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

try:
    from html import escape
except ImportError:
    from cgi import escape


# Main
run_test = True
if len(sys.argv) == 2:  # to only compare images et make reports
    run_test = False

PYTHON_VERSION = sys.version_info[0]
print('Python {}: test all simpleguics2pygame'.format(PYTHON_VERSION),
      file=sys.stderr)
if not to_compare_imgs:
    print('!PIL module not available: images comparaison impossible',
          file=sys.stderr)

try:
    from SimpleGUICS2Pygame import _VERSION as SIMPLEGUICS2PYGAME_VERSION
    from SimpleGUICS2Pygame import _WEBSITE as SIMPLEGUICS2PYGAME_WEBSITE
    PYGAME_VERSION = simplegui._PYGAME_VERSION
except ImportError:
    SIMPLEGUICS2PYGAME_VERSION = '?'
    SIMPLEGUICS2PYGAME_WEBSITE = 'http://www.opimedia.be/DS/SimpleGUICS2Pygame/'
    PYGAME_VERSION = '?'

filenames = sorted(glob.glob('*.py'))
dir_results = 'results_py' + str(PYTHON_VERSION)

filenames.remove('test_all.py')

filenames.insert(0, 'SimpleGUICS2Pygame_check.py')

filenames = [filename[:-3] for filename in filenames]


nb = len(filenames)

# Run each test_*.py
errors = {}
if to_compare_imgs:
    imgs_diff = {}

for i, filename in enumerate(filenames):
    print('{}/{} - {}... '.format(i + 1, nb, filename),
          end='', file=sys.stderr)
    sys.stderr.flush()

    if run_test:
        errors[filename] = os.system(
            'python{0} {1}{2}.py {3}/{2}.png > {3}/{2}.log'
            .format(PYTHON_VERSION,
                    ('../script/'
                     if filename == 'SimpleGUICS2Pygame_check'
                     else ''),
                    filename,
                    dir_results))
    else:
        errors[filename] = 'skip running'

    sys.stdout.flush()
    sys.stderr.flush()

    if to_compare_imgs:
        good_path = 'results_good/{}.png'.format(filename)
        src_path = '{}/{}.png'.format(dir_results, filename)
        if os.path.exists(src_path) or os.path.exists(good_path):
            if os.path.exists(good_path) and os.path.exists(src_path):
                good_img = PIL.Image.open(good_path)
                src_img = PIL.Image.open(src_path)
                diff_img = PIL.ImageChops.difference(good_img, src_img)
                imgs_diff[filename] = int(round(
                    PIL.ImageStat.Stat(diff_img).rms[0]))
                if (filename in ('test_simpleplot_bars',
                                 'test_simpleplot_lines')
                        and (imgs_diff[filename] < 15)):
                    imgs_diff[filename] = 0
            else:
                imgs_diff[filename] = ('{} missing'
                                       .format(good_path
                                               if not os.path.exists(good_path)
                                               else src_path))

    print((errors[filename] if errors[filename]
           else 'ok'),
          (imgs_diff[filename] if imgs_diff.get(filename)
           else ''),
          file=sys.stderr)
    sys.stderr.flush()


# Make HTLM report
f = open(dir_results + '/log.htm', 'w')

print("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
  <title>SimpleGUICS2Pygame {1} &ndash; test report &ndash; Python {2} &ndash; Pygame {3}</title>
  <link rel="stylesheet" type="text/css" href="../_css/log.css">
</head>

<body>
  <h1><a href="{0}" target="_blank">SimpleGUICS2Pygame</a> <span class="infos">{1} &ndash; test report &ndash; Python {2} &ndash; Pygame {3} &ndash; {4}</span></h1>
  <ol>""".format(SIMPLEGUICS2PYGAME_WEBSITE,
                 SIMPLEGUICS2PYGAME_VERSION,
                 PYTHON_VERSION,
                 PYGAME_VERSION,
                 datetime.datetime.now()),
      file=f)


for i, filename in enumerate(filenames):
    print("""<li>
  <h2 {}>{}{}{}</h2>""".format(
        (' class="error"' if errors[filename]
         else ''),
        filename,
        ('<span class="error">Error: {}!</span>'.format(errors[filename])
         if errors[filename]
         else ''),
        ('<span class="imgs_diff">Images different: {}!</span>'
         .format(imgs_diff[filename])
         if imgs_diff.get(filename)
         else '')),
        file=f)

    f_log = open('{}/{}.log'.format(dir_results,
                                    filename))

    log = f_log.read().strip()

    if imgs_diff.get(filename):
        print("""<img src="../{0}" alt="[{0}]">
<img src="../{1}" alt="[{1}]">""".format(
            'results_good/{}.png'.format(filename),
            '{}/{}.png'.format(dir_results, filename)),
            file=f)

    if len(log) > 0:
        print("""<pre class="log">{}</pre>""".format(escape(log)),
              file=f)

    f_log.close()

    print('</li>',
          file=f)


print("""  </ol>
</body>
</html>""",
      file=f)

f.close()
