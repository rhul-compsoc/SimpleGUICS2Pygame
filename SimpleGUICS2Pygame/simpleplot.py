# -*- coding: latin-1 -*-

"""
simpleplot (September 1st, 2014)

Replace the simpleplot module of CodeSkulptor.

Require matplotlib_
(`Unofficial Windows Binaries`_)
(and must be installed separately).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/

.. _matplotlib: http://matplotlib.org/
.. _`Unofficial Windows Binaries`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
"""

try:
    import matplotlib.pyplot
except Exception as e:
    import os

    if os.environ.get('READTHEDOCS', None) != 'True':
        raise Exception('matplotlib not installed! ' + str(e))


#
# Private global constant
##########################
_COLORS = ('#edc240', '#afd8f8', '#cb4b4b', '#4da74d',
           '#9440ed', '#bd9b33', '#8cacc6', '#a23c3c',
           '#3d853d', '#7633bd', '#ffe84c', '#d2ffff',
           '#f35a5a', '#5cc85c', '#b14cff', '#8e7426',
           '#698194', '#792d2d', '#2e642e', '#58268e',
           '#ffff59', '#f4ffff', '#ff6969', '#6be96b',
           '#cf59ff', '#5e4d19', '#455663', '#511d1d',
           '#1e421e', '#3b195e', '#ffff66', '#ffffff')
"""
Color used for each graph.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# Functions
############
def _block():
    """
    If some plot windows are open
    then block the program until closing all windows.
    **(Not available in SimpleGUI of CodeSkulptor.)**
    """
    matplotlib.pyplot.show()


def plot_bars(framename, width, height, xlabel, ylabel, datasets,
              legends=None,
              _block=False, _filename=None):
    """
    Open a window titled `framename`
    and plot graphes with `datasets` data
    shown as vertical bars.

    `xlabel` and `ylabel` are labels of x-axis and y-axis.

    `datasets` must be a sequence of data.
    Each data must be:

    * Sequence (not empty) of pair x, y.
      Each point (x, y) is represented by a vertical bar of height y.

    * Or dict (not empty) x: y.
      Each point (x, y) is represented by a vertical bar of height y.

    If `legends` is not None
    then it must be a sequence of legend of each graph.

    If `_block`
    then block the program until closing the window
    else continue and close the window when program stop.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    If `_filename` is not None
    then save the image to this file.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    :param framename: str
    :param width: int > 0
    :param height: int > 0
    :param xlabel: str
    :param ylabel: str
    :param datasets: (list or tuple)
                     of (((list or tuple) of ([int or float, int or float]
                     or (int or float, int or float)))
                     or (dict (int or float): (int or float)))
    :param legends: None or ((list or tuple) of same length as datasets)
    :param _block: False
    :param _filename: None or str
    """
    assert isinstance(framename, str), type(framename)

    assert isinstance(width, int), type(width)
    assert width > 0, width

    assert isinstance(height, int), type(height)
    assert height > 0, height

    assert isinstance(xlabel, str), type(xlabel)
    assert isinstance(ylabel, str), type(ylabel)

    assert isinstance(datasets, list) or isinstance(datasets, tuple), \
        type(datasets)
    if __debug__:
        for dataset in datasets:
            assert isinstance(dataset, list) or isinstance(dataset, tuple) \
                or isinstance(dataset, dict), type(datasets)
            assert dataset
            for x, y in (dataset.items() if isinstance(dataset, dict)
                         else dataset):
                assert isinstance(x, int) or isinstance(x, float), (type(x), x)
                assert isinstance(y, int) or isinstance(y, float), (type(y), y)

    assert ((legends is None) or isinstance(legends, list)
            or isinstance(legends, tuple)), type(legends)
    assert (legends is None) or (len(legends) == len(datasets)), legends

    assert isinstance(_block, bool), type(_block)
    assert (_filename is None) or isinstance(_filename, str), type(_filename)

    fig = matplotlib.pyplot.figure()
    fig.set_size_inches(width//fig.get_dpi(), height//fig.get_dpi(),
                        forward=True)

    fig.canvas.set_window_title(framename)
    matplotlib.pyplot.title(framename)

    from os.path import sep

    icon_path = __file__.split(sep)[:-1]
    try:
        icon_path.extend(('_img', 'SimpleGUICS2Pygame_32x32.ico'))
        matplotlib.pyplot.get_current_fig_manager().window.wm_iconbitmap(
            sep.join(icon_path))
    except:
        pass

    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)

    matplotlib.pyplot.grid()

    bar_width = 0.8/len(datasets)
    for i, dataset in enumerate(datasets):
        bar_lefts, bar_heights = zip(*(sorted(dataset.items())
                                       if isinstance(dataset, dict)
                                       else dataset))
        matplotlib.pyplot.bar([x + bar_width*i for x in bar_lefts],
                              bar_heights,
                              width=bar_width,
                              color=_COLORS[i % len(_COLORS)],
                              edgecolor=_COLORS[i % len(_COLORS)],
                              figure=fig,
                              alpha=0.5)

    ymin, ymax = matplotlib.pyplot.ylim()
    matplotlib.pyplot.ylim(ymin, ymax + 1)

    if legends is not None:
        matplotlib.pyplot.legend(legends, loc='upper right')

    matplotlib.pyplot.show(block=_block)

    if _filename is not None:
        matplotlib.pyplot.savefig(_filename)


def plot_lines(framename, width, height, xlabel, ylabel, datasets,
               points=False, legends=None,
               _block=False, _filename=None):
    """
    Open a window titled `framename`
    and plot graphes with `datasets` data
    shown as connected lines.

    `xlabel` and `ylabel` are labels of x-axis and y-axis.

    `datasets` must be a sequence of data.
    Each data must be:

    * Sequence (not empty) of pair x, y.
      Each point (x, y) is plotted (in given order)
      and connected with line to previous and next points.

    * Or dict (not empty) x: y.
      Each point (x, y) is plotted (in ascending order of x value)
      and connected with line to previous and next points.

    If `points`
    then each point is highlighted by a small disc
    (a small circle in CodeSkulptor).

    If `legends` is not None
    then it must be a sequence of legend of each graph.

    If `_block`
    then block the program until closing the window
    else continue and close the window when program stop.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    If `_filename` is not None
    then save the image to this file.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    :param framename: str
    :param width: int > 0
    :param height: int > 0
    :param xlabel: str
    :param ylabel: str
    :param datasets: (list or tuple)
                     of (((list or tuple) of ([int or float, int or float]
                     or (int or float, int or float)))
                     or (dict (int or float): (int or float)))
    :param points: bool
    :param legends: None or ((list or tuple) of same length as datasets)
    :param _block: False
    :param _filename: None or str
    """
    assert isinstance(framename, str), type(framename)

    assert isinstance(width, int), type(width)
    assert width > 0, width

    assert isinstance(height, int), type(height)
    assert height > 0, height

    assert isinstance(xlabel, str), type(xlabel)
    assert isinstance(ylabel, str), type(ylabel)

    assert isinstance(datasets, list) or isinstance(datasets, tuple), \
        type(datasets)
    if __debug__:
        for dataset in datasets:
            assert isinstance(dataset, list) or isinstance(dataset, tuple) \
                or isinstance(dataset, dict), type(datasets)
            assert dataset
            for x, y in (dataset.items() if isinstance(dataset, dict)
                         else dataset):
                assert isinstance(x, int) or isinstance(x, float), (type(x), x)
                assert isinstance(y, int) or isinstance(y, float), (type(y), y)

    assert isinstance(points, bool), type(points)

    assert ((legends is None) or isinstance(legends, list)
            or isinstance(legends, tuple)), type(legends)
    assert (legends is None) or (len(legends) == len(datasets)), legends

    assert isinstance(_block, bool), type(_block)
    assert (_filename is None) or isinstance(_filename, str), type(_filename)

    fig = matplotlib.pyplot.figure()
    fig.set_size_inches(width//fig.get_dpi(), height//fig.get_dpi(),
                        forward=True)

    fig.canvas.set_window_title(framename)
    matplotlib.pyplot.title(framename)

    from os.path import sep

    icon_path = __file__.split(sep)[:-1]
    try:
        icon_path.extend(('_img', 'SimpleGUICS2Pygame_32x32.ico'))
        matplotlib.pyplot.get_current_fig_manager().window.wm_iconbitmap(
            sep.join(icon_path))
    except:
        pass

    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)

    matplotlib.pyplot.grid()

    for i, dataset in enumerate(datasets):
        matplotlib.pyplot.plot(*zip(*(sorted(dataset.items())
                                      if isinstance(dataset, dict)
                                      else dataset)),
                               color=_COLORS[i % len(_COLORS)],
                               figure=fig,
                               marker=('o' if points
                                       else None))

    ymin, ymax = matplotlib.pyplot.ylim()
    matplotlib.pyplot.ylim(ymin - 1, ymax + 1)

    if legends is not None:
        matplotlib.pyplot.legend(legends, loc='upper right')

    matplotlib.pyplot.show(block=_block)

    if _filename is not None:
        matplotlib.pyplot.savefig(_filename)


def plot_scatter(framename, width, height, xlabel, ylabel, datasets,
                 legends=None,
                 _block=False, _filename=None):
    """
    Open a window titled `framename`
    and plot graphes with `datasets` data
    shown as scattered points.

    `xlabel` and `ylabel` are labels of x-axis and y-axis.

    `datasets` must be a sequence of data.
    Each data must be:

    * Sequence (not empty) of pair x, y.
      Each point (x, y) is represented by a circle.

    * Or dict (not empty) x: y.
      Each point (x, y) is represented by a circle.

    If `legends` is not None
    then it must be a sequence of legend of each graph.

    If `_block`
    then block the program until closing the window
    else continue and close the window when program stop.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    If `_filename` is not None
    then save the image to this file.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    :param framename: str
    :param width: int > 0
    :param height: int > 0
    :param xlabel: str
    :param ylabel: str
    :param datasets: (list or tuple)
                     of (((list or tuple) of ([int or float, int or float]
                     or (int or float, int or float)))
                     or (dict (int or float): (int or float)))
    :param legends: None or ((list or tuple) of same length as datasets)
    :param _block: False
    :param _filename: None or str
    """
    assert isinstance(framename, str), type(framename)

    assert isinstance(width, int), type(width)
    assert width > 0, width

    assert isinstance(height, int), type(height)
    assert height > 0, height

    assert isinstance(xlabel, str), type(xlabel)
    assert isinstance(ylabel, str), type(ylabel)

    assert isinstance(datasets, list) or isinstance(datasets, tuple), \
        type(datasets)
    if __debug__:
        for dataset in datasets:
            assert isinstance(dataset, list) or isinstance(dataset, tuple) \
                or isinstance(dataset, dict), type(datasets)
            assert dataset
            for x, y in (dataset.items() if isinstance(dataset, dict)
                         else dataset):
                assert isinstance(x, int) or isinstance(x, float), (type(x), x)
                assert isinstance(y, int) or isinstance(y, float), (type(y), y)

    assert ((legends is None) or isinstance(legends, list)
            or isinstance(legends, tuple)), type(legends)
    assert (legends is None) or (len(legends) == len(datasets)), legends

    assert isinstance(_block, bool), type(_block)
    assert (_filename is None) or isinstance(_filename, str), type(_filename)

    fig = matplotlib.pyplot.figure()
    fig.set_size_inches(width//fig.get_dpi(), height//fig.get_dpi(),
                        forward=True)

    fig.canvas.set_window_title(framename)
    matplotlib.pyplot.title(framename)

    from os.path import sep

    icon_path = __file__.split(sep)[:-1]
    try:
        icon_path.extend(('_img', 'SimpleGUICS2Pygame_32x32.ico'))
        matplotlib.pyplot.get_current_fig_manager().window.wm_iconbitmap(
            sep.join(icon_path))
    except:
        pass

    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)

    matplotlib.pyplot.grid()

    xmin = float('inf')
    xmax = float('-inf')

    for i, dataset in enumerate(datasets):
        xs, ys = zip(*(sorted(dataset.items())
                       if isinstance(dataset, dict)
                       else dataset))
        xmin = min(xmin, min(xs))
        xmax = max(xmax, max(xs))
        matplotlib.pyplot.scatter(xs,
                                  ys,
                                  color=_COLORS[i % len(_COLORS)],
                                  edgecolor=_COLORS[i % len(_COLORS)],
                                  figure=fig)

    matplotlib.pyplot.xlim(xmin, xmax)

    if legends is not None:
        matplotlib.pyplot.legend(legends, loc='upper right')

    matplotlib.pyplot.show(block=_block)

    if _filename is not None:
        matplotlib.pyplot.savefig(_filename)
