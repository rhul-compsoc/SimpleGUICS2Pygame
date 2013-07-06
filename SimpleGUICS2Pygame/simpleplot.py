# -*- coding: latin-1 -*-

"""
simpleplot (July 6, 2013)

Replace the simpleplot module of CodeSkulptor.

Require matplotlib_
(`Unofficial Windows Binaries`_).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013 Olivier Pirson
http://www.opimedia.be/

.. _matplotlib: http://matplotlib.org/
.. _`Unofficial Windows Binaries`: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib
"""

try:
    import matplotlib.pyplot
except Exception as e:
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
def plot_lines(framename, width, height, xlabel, ylabel, datasets,
               points=False, legends=None):
    """
    Open a window titled `framename`
    and plot graphes with `datasets` data.

    `xlabel` and `ylabel` are labels of x-axis and y-axis.

    `datasets` must be a sequence of data.
    Each data must be:

    * Sequence of pair x, y.
      Each point (x, y) is plotted (in given order)
      and connected with line to previous and next points.

    * Or dict x: y.
      Each point (x, y) is plotted (in ascending order of x value)
      and connected with line to previous and next points.

    If `points`
    then each point is highlighted by a small disc
    (a small circle in CodeSkulptor).

    If `legends` is not None
    then it must be a sequence of legend of each graph.

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
            for x, y in (dataset.items() if isinstance(dataset, dict)
                         else dataset):
                assert isinstance(x, int) or isinstance(x, float), (type(x), x)
                assert isinstance(y, int) or isinstance(y, float), (type(y), y)

    assert isinstance(points, bool), type(points)

    assert ((legends is None) or isinstance(legends, list)
            or isinstance(legends, tuple)), type(legends)
    assert (legends is None) or (len(legends) == len(datasets)), legends

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

    matplotlib.pyplot.show()
