# -*- coding: latin-1 -*-

"""
numeric (June 16, 2014)

Replace the numeric module of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2014 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import division

from sys import float_info as _SYS_FLOAT_INFO


# Global constant
#################
_EPSILON = _SYS_FLOAT_INFO.epsilon
"""
The default epsilon value.
"""


# Class
########
class Matrix:
    """
    Matrix (m x n).

    See http://en.wikipedia.org/wiki/Matrix_%28mathematics%29 .
    """
    def __init__(self, data, _copy=True):
        """
        Create a matrix with the 2-dimensional `data`.

        If not `_copy`
        then `data` is directly used without copy.
        In this case, `data` must be a correct list of list of float.
        **(Option not available in SimpleGUI of CodeSkulptor.)**

        :param data: (not empty tuple or list) of (same size tuple or list) of (int or float)
        :param _copy: bool
        """
        assert isinstance(_copy, bool), type(_copy)
        if _copy:
            assert isinstance(data, tuple) or isinstance(data, list), \
                type(data)
            assert len(data) >= 1
            assert isinstance(data[0], tuple) or isinstance(data[0], list), \
                type(data[0])
            if __debug__:
                n = len(data[0])
                assert n >= 1
                for row in data:
                    assert isinstance(row, tuple) or isinstance(row, list), \
                        type(row)
                    assert n == len(row), (n, len(row))
                    for x in row:
                        assert isinstance(x, int) or isinstance(x, float), \
                            type(x)
        else:
            assert isinstance(data, list), type(data)
            assert len(data) >= 1
            assert isinstance(data[0], list), type(data[0])
            if __debug__:
                n = len(data[0])
                assert n >= 1
                for row in data:
                    assert isinstance(row, list), type(row)
                    assert n == len(row), (n, len(row))
                    for x in row:
                        assert isinstance(x, float), type(x)

        self._data = ([[float(x) for x in row] for row in data] if _copy
                      else data)

    def __add__(self, other):
        """
        To a matrix (m x n)
        return the matrix plus other.

        :param other: Matrix (m x n)

        :return: Matrix (m x n)
        """
        assert self._nb_lines() == other._nb_lines(), (self._nb_lines(),
                                                       other._nb_lines())
        assert self._nb_columns() == other._nb_columns(), (self._nb_columns(),
                                                           other._nb_columns())

        return Matrix([[self[i, j] + other[i, j]
                        for j in range(self._nb_columns())]
                       for i in range(self._nb_lines())],
                      _copy=False)

    def __getitem__(self, i_j):
        """
        Returns the value of the (m x n) matrix
        at row i and column j.

        :param i_j: (0 <= int < m, 0 <= int < n) or [0 <= int < m, 0 <= int < n]

        :return: float
        """
        assert isinstance(i_j, tuple) or isinstance(i_j, list), \
            type(i_j)
        assert len(i_j) == 2, len(i_j)
        assert isinstance(i_j[0], int), type(i_j[0])
        assert 0 <= i_j[0] < self._nb_lines(), (i_j[0], self._nb_lines())
        assert isinstance(i_j[1], int), type(i_j[1])
        assert 0 <= i_j[1] < self._nb_columns(), (i_j[1], self._nb_columns())

        return self._data[i_j[0]][i_j[1]]

    def __mul__(self, other):
        """
        To a matrix (m x k)
        return the matrix multiply by other.

        :param other: Matrix (k x n)

        :return: Matrix (m x n)
        """
        assert self._nb_columns() == other._nb_lines(), (self._nb_columns(),
                                                         other._nb_lines())

        return Matrix([[sum([self[i, k]*other[k, j]
                             for k in range(self._nb_columns())])
                        for j in range(other._nb_columns())]
                       for i in range(self._nb_lines())],
                      _copy=False)

    def __setitem__(self, i_j, value):
        """
        Change the value of the element at row i and column j,
        to the (m x n) matrix.

        :param i_j: (0 <= int < m, 0 <= int < n) or [0 <= int < m, 0 <= int < n]
        :param value: int or float
        """
        assert isinstance(i_j, tuple) or isinstance(i_j, list), \
            type(i_j)
        assert len(i_j) == 2, len(i_j)
        assert isinstance(i_j[0], int), type(i_j[0])
        assert 0 <= i_j[0] < self._nb_lines(), (i_j[0], self._nb_lines())
        assert isinstance(i_j[1], int), type(i_j[1])
        assert 0 <= i_j[1] < self._nb_columns(), (i_j[1], self._nb_columns())
        assert isinstance(value, int) or isinstance(value, float), type(valu)

        self._data[i_j[0]][i_j[1]] = float(value)

    def __str__(self):
        """
        Returns the string representation of the matrix.

        :return: string
        """
        return '[{}]'.format('\n '.join([str(row) for row in self._data]))

    def __sub__(self, other):
        """
        To a matrix (m x n)
        return the matrix minus other.

        :param other: Matrix (m x n)

        :return: Matrix (m x n)
        """
        assert self._nb_lines() == other._nb_lines(), (self._nb_lines(),
                                                       other._nb_lines())
        assert self._nb_columns() == other._nb_columns(), (self._nb_columns(),
                                                           other._nb_columns())

        return Matrix([[self[i, j] - other[i, j]
                        for j in range(self._nb_columns())]
                       for i in range(self._nb_lines())],
                      _copy=False)

    def _is_identity(self, epsilon=_EPSILON):
        """
        If the matrix is an identity matrix
        then return True,
        else return False.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param epsilon: 0 <= float < 1

        :return: bool
        """
        assert isinstance(epsilon, float), type(epsilon)
        assert 0 <= epsilon < 1, epsilon

        n = self._nb_lines()
        if n != self._nb_columns():
            return False

        for i in range(n):
            for j in range(n):
                if abs(self[i, j] - 1 if i == j
                       else self[i, j]) > epsilon:
                    return False

        return True

    def _is_zero(self, epsilon=_EPSILON):
        """
        If the matrix is a zeros matrix
        then return True,
        else return False.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param epsilon: 0 <= float < 1

        :return: bool
        """
        assert isinstance(epsilon, float), type(epsilon)
        assert 0 <= epsilon < 1, epsilon

        for i in range(self._nb_lines()):
            for j in range(self._nb_columns()):
                if abs(self[i, j]) > epsilon:
                    return False

        return True

    def _nb_columns(self):
        """
        Return n for a (m x n) matrix.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :return: int >= 1
        """
        return len(self._data[0])

    def _nb_lines(self):
        """
        Return m to a (m x n) matrix.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :return: int >= 1
        """
        return len(self._data)

    def abs(self):
        """
        To a matrix (m x n)
        return the matrix with each element is the absolute value.

        :return: Matrix (m x n)
        """
        return Matrix([[abs(self[i, j])
                        for j in range(self._nb_columns())]
                       for i in range(self._nb_lines())],
                      _copy=False)

    def copy(self):
        """
        Return a copy of the matrix (m x n).

        :return: Matrix (m x n)
        """
        return Matrix(self._data)

    def getcol(self, j):
        """
        Returns the (1 x m) matrix
        that is a copy of column j of the (m x n) matrix.

        :param j: 0 <= int < n

        :return: Matrix (1 x m)
        """
        assert isinstance(j, int), type(j)
        assert 0 <= j < self._nb_columns(), (j, self._nb_columns())

        return Matrix([[row[j] for row in self._data]], _copy=False)

    def getrow(self, i):
        """
        Returns the (1 x n) matrix
        that is a copy of row i of the (m x n) matrix.

        :param i: 0 <= int < m

        :return: Matrix (1 x n)
        """
        assert isinstance(i, int), type(i)
        assert 0 <= i < self._nb_lines(), (i, self._nb_lines())

        return Matrix([list(self._data[i])], _copy=False)

    def inverse(self, _epsilon=_EPSILON):
        """
        If the square matrix (n x n) is inversible
        then return the inverse,
        else raise an ValueError exception.

        Algorithm used: Gaussian elimination.
        See http://en.wikipedia.org/wiki/Gaussian_elimination .

        :param _epsilon: 0 <= float < 1 **(Option not available in SimpleGUI of CodeSkulptor.)**

        :return: Matrix (n x n)

        :raise: ValueError if the matrix is not inversible
        """
        assert self._nb_lines() == self._nb_columns(), (self._nb_lines(),
                                                        self._nb_columns())
        assert isinstance(_epsilon, float), type(_epsilon)
        assert 0 <= _epsilon < 1, _epsilon

        n = self._nb_columns()
        mat = self.copy()
        inv = identity(n)

        # Diagonalize
        for i_with_pivot in range(n):
            for i in range(n):
                if i != i_with_pivot:
                    d = mat[i_with_pivot, i_with_pivot]
                    if abs(d) <= _epsilon:
                        raise ValueError('matrix has no inverse')

                    factor = mat[i, i_with_pivot]/d
                    for j in range(n):
                        mat[i, j] -= mat[i_with_pivot, j]*factor
                    mat[i, i_with_pivot] = 0
                    for j in range(n):
                        inv[i, j] -= inv[i_with_pivot, j]*factor

        # Scale rows
        for i in range(n):
            for j in range(n):
                d = mat[i, i]
                if abs(d) <= _epsilon:
                    raise ValueError('matrix has no inverse')

                inv[i, j] /= d

        if all([abs(x) <= _epsilon for x in reversed(mat._data[-1])]):
            raise ValueError('matrix has no inverse')

        return inv

    def scale(self, factor):
        """
        To a matrix (m x n)
        return the matrix with each element multiply by factor.

        :param factor: int or float

        :return: Matrix (m x n)
        """
        assert isinstance(factor, int) or isinstance(factor, float), \
            type(factor)

        return Matrix([[self[i, j]*factor
                        for j in range(self._nb_columns())]
                       for i in range(self._nb_lines())],
                      _copy=False)

    def shape(self):
        """
        Return (m, n) to a matrix (m x n).

        :return: (int >= 1, int >= 1)
        """
        return (self._nb_lines(), self._nb_columns())

    def summation(self):
        """
        Return the sum of all the elements of the matrix.

        :return: float
        """
        return sum([sum(row) for row in self._data])

    def transpose(self):
        """
        Return the transposition of the matrix (m x n).

        :return: Matrix (n x m)
        """
        return Matrix([[self[i, j]
                        for i in range(self._nb_lines())]
                       for j in range(self._nb_columns())],
                      _copy=False)


# Private function
##################
def _zero(m, n):
    """
    Return a (`m` x `n`) zeros matrix.

    :param m: int >= 1
    :param n: int >= 1

    :return: Matrix (`m` x `n`)
    """
    assert isinstance(m, int), type(m)
    assert m >= 1, m
    assert isinstance(n, int), type(n)
    assert n >= 1, n

    return Matrix([[0.0 for j in range(n)]
                   for i in range(m)],
                  _copy=False)


# Function
##########
def identity(size):
    """
    Return a (`size` x `size`) identity matrix.

    :param size: int >= 1

    :return: Matrix (`size` x `size`)
    """
    assert isinstance(size, int), type(size)
    assert size >= 1, size

    return Matrix([[(1.0 if i == j
                     else 0.0) for j in range(size)]
                   for i in range(size)],
                  _copy=False)
