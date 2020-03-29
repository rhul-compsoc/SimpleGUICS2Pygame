#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Setup of SimpleGUICS2Pygame package (March 29, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2016, 2018, 2020 Olivier Pirson
http://www.opimedia.be/
"""

import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


from SimpleGUICS2Pygame import _VERSION, _WEBSITE, _WEBSITE_DOC


def parse_requirements_file():
    """
    Parse file "requirements.txt" and return the requirements list.

    :return: list of str
    """
    with open('requirements.txt') as fin:
        requirements = fin.readlines()

    return list(requirement.strip() for requirement in requirements)


setup(name='SimpleGUICS2Pygame',
      version=_VERSION,
      description='Primarily a standard Python (2 and 3) module reimplementing the SimpleGUI particular module of CodeSkulptor (a Python browser environment). In fact a package also with other modules adapted from CodeSkulptor.',  # noqa
      long_description=io.open('README.rst', encoding='utf-8').read(),

      author='Olivier Pirson',
      author_email='olivier.pirson.opi@gmail.com',
      url=_WEBSITE_DOC,
      project_urls={'Documentation': _WEBSITE_DOC,
                    'Source Code': _WEBSITE},

      packages=['SimpleGUICS2Pygame'],
      license='GPLv3',
      platforms='any',
      include_package_data=True,

      scripts=['SimpleGUICS2Pygame/script/cs2both.py',
               'SimpleGUICS2Pygame/script/pygame_check.py',
               'SimpleGUICS2Pygame/script/SimpleGUICS2Pygame_check.py'],

      install_requires=parse_requirements_file(),

      keywords='CodeSkulptor SimpleGUI Pygame game education',
      classifiers=[
          'Development Status :: 5 - Production/Stable',

          'Environment :: MacOS X',
          'Environment :: Win32 (MS Windows)',
          'Environment :: X11 Applications',

          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Other Audience',

          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

          'Natural Language :: English',

          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: OS Independent',
          'Operating System :: POSIX',
          'Operating System :: Unix',

          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',

          'Topic :: Education',
          'Topic :: Games/Entertainment',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Multimedia :: Sound/Audio',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: pygame',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: Software Development :: Widget Sets'])
