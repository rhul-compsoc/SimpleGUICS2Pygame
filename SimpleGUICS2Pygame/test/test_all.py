#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test all other test_*.py. (March 10, 2020)

Require Pillow (PIL)
https://python-pillow.org/

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014, 2016, 2020 Olivier Pirson
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

    TO_COMPARE_IMGS = True
except ImportError:
    TO_COMPARE_IMGS = False

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

try:
    from html import escape  # for Python 3
except ImportError:
    from cgi import escape   # for Python 2


RUN_TEST = True
if len(sys.argv) == 2:  # to only compare images et make reports
    RUN_TEST = False

PYTHON_VERSION = sys.version_info[0]
print('Python {}: test all simpleguics2pygame'.format(PYTHON_VERSION),
      file=sys.stderr)
if not TO_COMPARE_IMGS:
    print('!PIL module not available: images comparaison impossible',
          file=sys.stderr)

try:
    from SimpleGUICS2Pygame import _VERSION as SIMPLEGUICS2PYGAME_VERSION
    from SimpleGUICS2Pygame import _WEBSITE as SIMPLEGUICS2PYGAME_WEBSITE
    from SimpleGUICS2Pygame import _WEBSITE_DOC as SIMPLEGUICS2PYGAME_WEBSITE_DOC  # noqa
    PYGAME_VERSION = simplegui._PYGAME_VERSION  # noqa  # pylint: disable=no-member,protected-access
except ImportError:
    SIMPLEGUICS2PYGAME_VERSION = '?'
    SIMPLEGUICS2PYGAME_WEBSITE = 'https://bitbucket.org/OPiMedia/simpleguics2pygame/'  # noqa
    SIMPLEGUICS2PYGAME_WEBSITE_DOC = 'https://simpleguics2pygame.readthedocs.io/'  # noqa
    PYGAME_VERSION = '?'


DIR_RESULTS = 'results_py' + str(PYTHON_VERSION)


#
# Main
######
def main():
    """Execute all test_*.py programs and build HTML report."""
    filenames = sorted(glob.glob('*.py'))
    filenames.remove('test_all.py')
    filenames.insert(0, 'SimpleGUICS2Pygame_check.py')
    filenames = [filename[:-3] for filename in filenames]

    # Run each test_*.py
    errors = {}
    if TO_COMPARE_IMGS:
        imgs_diff = {}

    for i, filename in enumerate(filenames):
        print('{}/{} - {}... '.format(i + 1, len(filenames), filename),
              end='', file=sys.stderr)
        sys.stderr.flush()

        if RUN_TEST:
            errors[filename] = os.system(
                'python{0} {1}{2}.py {3}/{2}.png > {3}/{2}.log'
                .format(PYTHON_VERSION,
                        ('../script/'
                         if filename == 'SimpleGUICS2Pygame_check'
                         else ''),
                        filename,
                        DIR_RESULTS))
        else:
            errors[filename] = 'skip running'

        sys.stdout.flush()
        sys.stderr.flush()

        if TO_COMPARE_IMGS:
            good_path = 'results_good/{}.png'.format(filename)
            src_path = '{}/{}.png'.format(DIR_RESULTS, filename)
            if os.path.exists(src_path) or os.path.exists(good_path):
                if os.path.exists(good_path) and os.path.exists(src_path):
                    good_img = PIL.Image.open(good_path).convert('RGB')
                    src_img = PIL.Image.open(src_path).convert('RGB')
                    diff_img = PIL.ImageChops.difference(good_img, src_img)
                    imgs_diff[filename] = int(round(
                        PIL.ImageStat.Stat(diff_img).rms[0]))
                    if imgs_diff[filename] <= 25:
                        imgs_diff[filename] = 0
                    diff_img.save('{}/{}_diff.png'
                                  .format(DIR_RESULTS, filename),
                                  'PNG')
                else:
                    imgs_diff[filename] = ('{} missing'
                                           .format(
                                               good_path
                                               if not os.path.exists(good_path)
                                               else src_path))

        print((errors[filename] if errors[filename]
               else 'ok'),
              (imgs_diff[filename] if imgs_diff.get(filename)
               else ''),
              file=sys.stderr)
        sys.stderr.flush()

    # Make HTLM report
    outfile = open(DIR_RESULTS + '/log.html', 'w')

    print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, itial-scale=1">
  <meta name="author" content="SimpleGUICS2Pygame &ndash; test_all">
  <title>SimpleGUICS2Pygame {2} &ndash; test report &ndash; Python {3} &ndash; Pygame {4}</title>
  <link rel="stylesheet" type="text/css" href="../_css/log.css">
</head>
<body>
<main>
  <header>
    <a href="{0}" target="_blank">SimpleGUICS2Pygame</a> {2}
    (<a href="{1}" target="_blank">online documentation</a>)
    <h1>test report &ndash; Python {3} &ndash; Pygame {4} &ndash; {5}</h1>
  </header>
  <ol>""".format(SIMPLEGUICS2PYGAME_WEBSITE,  # noqa
                 SIMPLEGUICS2PYGAME_WEBSITE_DOC,
                 SIMPLEGUICS2PYGAME_VERSION,
                 PYTHON_VERSION,
                 PYGAME_VERSION,
                 datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
          file=outfile)

    for i, filename in enumerate(filenames):
        print("""<li>
  <h2 {}>{}{}{}</h2>"""
              .format((' class="error"' if errors[filename]
                       else ''),
                      filename,
                      ('<span class="error">Error: {}!</span>'
                       .format(errors[filename])
                       if errors[filename]
                       else ''),
                      ('<span class="imgs_diff">Images different: {}!</span>'
                       .format(imgs_diff[filename])
                       if imgs_diff.get(filename)
                       else '')),
              file=outfile)

        f_log = open('{}/{}.log'.format(DIR_RESULTS,
                                        filename))

        log = f_log.read().strip()

        if imgs_diff.get(filename):
            print("""<img src="../{0}" alt="[{0}]" title="Comparative result.">
<img src="../{1}" alt="[{1}]" title="Result of test.">
<img src="../{2}" alt="[{2}]" title="Difference images.">"""
                  .format('results_good/{}.png'.format(filename),
                          '{}/{}.png'.format(DIR_RESULTS, filename),
                          '{}/{}_diff.png'.format(DIR_RESULTS, filename)),
                  file=outfile)

        if len(log) > 0:
            print("""<pre class="log">{}</pre>""".format(escape(log)),  # noqa  # pylint: disable=deprecated-method
                  file=outfile)

        f_log.close()

        print('</li>',
              file=outfile)

    print("""  </ol>
</main>
</body>
</html>""",
          file=outfile)

    outfile.close()


if __name__ == '__main__':
    main()
