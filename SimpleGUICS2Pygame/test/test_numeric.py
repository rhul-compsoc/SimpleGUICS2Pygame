#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test numeric. (March 4, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2020 Olivier Pirson
http://www.opimedia.be/
"""

try:
    import numeric

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.numeric as numeric

    SIMPLEGUICS2PYGAME = True


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
else:
    PYTHON_VERSION = 'CodeSkulptor'  # http://www.codeskulptor.org/


def m_eq(a, b, exact=True):
    """
    If each element of a == each element of b
    then return True,
    else return False.

    If exact
    then comparaison of each element must be exact,
    else the absolute difference must be <= 1e-5

    :param a: numeric.Matrix
    :param b: numeric.Matrix
    :param exact: bool
    """
    assert isinstance(a, numeric.Matrix), type(a)
    assert isinstance(b, numeric.Matrix), type(b)
    assert isinstance(exact, bool), type(exact)

    if a.shape() != b.shape():
        return False

    if exact:
        return m_to_l(a) == m_to_l(b)
    else:
        m, n = a.shape()

        for i in range(m):
            for j in range(n):
                if abs(a[i, j] - b[i, j]) > 1e-5:
                    return False

        return True


def m_to_l(m):
    """
    Return the list of list corresponding to the matrix m.

    :param m: numeric.Matrix

    :return: list of list of float
    """
    assert isinstance(m, numeric.Matrix), type(m)

    return [[m[i, j] for j in range(m.shape()[1])]
            for i in range(m.shape()[0])]


if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) != 2:
        print('Test numeric.Matrix ...\n')
else:
        print('Test numeric.Matrix ...\n')


nb_errors = 0

dz5_3 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

dz3_5 = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

di1 = [[1]]

di5 = [[1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1]]

d5_3 = [[0, -1, 2],
        [-3, 4, -5],
        [6, -7, 8],
        [-9, 10, -11],
        [12, -13, 14]]

d5_3t = [[0, -3, 6, -9, 12],
         [-1, 4, -7, 10, -13],
         [2, -5, 8, -11, 14]]

d3_5 = [[0, -1, 2, -3, 4],
        [-5, 6, -7, 8, -9],
        [10, -11, 12, -13, 14]]

d3_5t = [[0, -5, 10],
         [-1, 6, -11],
         [2, -7, 12],
         [-3, 8, -13],
         [4, -9, 14]]

d2_2 = [[1, 2],
        [3, 4]]

d2_2i = [[-2, 1],
         [1.5, -0.5]]

d3_3 = [[2, -1, 0],
        [-1, 2, -1],
        [0, -1, 2]]

d3_3i = [[0.75, 0.5, 0.25],
         [0.5, 1, 0.5],
         [0.25, 0.5, 0.75]]

datas = (dz5_3, dz3_5,
         di1, di5,
         d5_3, d5_3t, d3_5, d3_5t,
         d2_2, d2_2i, d3_3, d3_3i)


# Matrix(), shape()
for data in datas:
    m = numeric.Matrix(data)
    if m.shape() != (len(data), len(data[0])):
        nb_errors += 1
        print('error: constructor size: %s' % data)
    if m_to_l(m) != data:
        nb_errors += 1
        print('error: constructor value: %s' % data)


# indentity()
mi1 = numeric.identity(1)
if mi1.shape() != (1, 1):
    nb_errors += 1
    print('error: identity size')

if m_to_l(mi1) != di1:
    nb_errors += 1
    print('error: identity value')

mi5 = numeric.identity(5)
if mi5.shape() != (5, 5):
    nb_errors += 1
    print('error: identity size')

if m_to_l(mi5) != di5:
    nb_errors += 1
    print('error: identity value')


# []
for data in datas:
    m = numeric.Matrix(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if m[i, j] != data[i][j]:
                nb_errors += 1
                print('error: [%i, %i]: %s' % (i, j, data))


# set []
for data in datas:
    m = numeric.Matrix(data)
    m2 = numeric.Matrix(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            m2[i, j] = 666
            if not isinstance(m2[i, j], float) or (m2[i, j] != 666):
                nb_errors += 1
                print('error: [%i, %i] = 666: %s' % (i, j, data))
                print(m2)

            m2[i, j] = m[i, j]
            if not m_eq(m, m2):
                nb_errors += 1
                print('error: [%i, %i] = old: %s' % (i, j, data))
                print(m2)


# copy()
for data in datas:
    m = numeric.Matrix(data)
    m2 = m.copy()

    if not m_eq(m, m2):
        nb_errors += 1
        print('error: [%i, %i] = old: %s' % (i, j, data))
        print(m)
        print(m2)

    m2[0, 0] = 666
    if m_eq(m, m2) or (m[0, 0] == 666):
        nb_errors += 1
        print('error: [%i, %i] = old: %s' % (i, j, data))
        print(m)
        print(m2)


# getrow()
for data in datas:
    m = numeric.Matrix(data)

    for i in range(len(data)):
        row = m_to_l(m.getrow(i))[0]

        if len(row) != len(data[0]):
            nb_errors += 1
            print('error: getrow size %i %s %s' % (i, row, data[i]))

        if row != data[i]:
            nb_errors += 1
            print('error: getrow %i %s %s' % (i, row, data[i]))

        for j in range(len(data[0])):
            if row[j] != data[i][j]:
                nb_errors += 1
                print('error: getrow != [%i, %i]' % (i, j))

# getcol()
for data in datas:
    m = numeric.Matrix(data)

    for j in range(len(data[0])):
        col = m_to_l(m.getcol(j))[0]
        if len(col) != len(data):
            nb_errors += 1
            print('error: getcol size %i %s %s' % (i, col, data))

        for i in range(len(data)):
            if col[i] != data[i][j]:
                nb_errors += 1
                print('error: getcol != [%i, %i]' % (i, j))


# scale(), +, -
for data in datas:
    m = numeric.Matrix(data)
    adds = numeric.Matrix(data)
    subs = numeric.Matrix(data).scale(-1)
    for k in range(1, 10):
        ms = m.scale(k)
        if not m_eq(ms, adds):
            nb_errors += 1
            print('error: scale != +: %i %s' % (k, data))
            print(ms)
            print(adds)
        adds = adds + m

        ms = m.scale(-k)
        if not m_eq(ms, subs):
            nb_errors += 1
            print('error: scale != -: %i %s' % (k, data))
            print(ms)
            print(subs)
        subs = subs - m

# *
m = numeric.Matrix(d5_3) * numeric.Matrix(d3_5)
if m_to_l(m) != [[25, -28, 31, -34, 37],
                 [-70, 82, -94, 106, -118],
                 [115, -136, 157, -178, 199],
                 [-160, 190, -220, 250, -280],
                 [205, -244, 283, -322, 361]]:
    nb_errors += 1
    print('error: (5, 3) * (3, 5)')
    print(m)

m = numeric.Matrix(d3_5) * numeric.Matrix(d5_3)
if m_to_l(m) != [[90, -100, 110],
                 [-240, 275, -310],
                 [390, -450, 510]]:
    nb_errors += 1
    print('error: (3, 5) * (5, 3)')
    print(m)

for data in datas:
    m = numeric.Matrix(data)
    m2 = m * numeric.identity(len(data[0]))
    if not m_eq(m, m2):
        nb_errors += 1
        print('error: *: %s' % data)
        print(m2)

    m2 = numeric.identity(len(data)) * m
    if not m_eq(m, m2):
        nb_errors += 1
        print('error: *: %s' % data)
        print(m2)

a = numeric.Matrix(d2_2)
b = numeric.Matrix(d2_2i)
if not m_eq(a * b, numeric.identity(2)):
    nb_errors += 1
    print('error: a * a^(-1)')
    print(a * b)
if not m_eq(b * a, numeric.identity(2)):
    nb_errors += 1
    print('error: a^(-1) * a')
    print(b * a)

a = numeric.Matrix(d3_3)
b = numeric.Matrix(d3_3i)
if not m_eq(a * b, numeric.identity(3)):
    nb_errors += 1
    print('error: a * a^(-1)')
    print(a * b)
if not m_eq(b * a, numeric.identity(3)):
    nb_errors += 1
    print('error: a^(-1) * a')
    print(b * a)


# summation()
for k in range(1, 10):
    m = numeric.identity(k)
    if m.summation() != k:
        nb_errors += 1
        print('error: sum %i %f' % (k, m.summation()))

m = numeric.Matrix(dz5_3)
if m.summation() != 0:
    nb_errors += 1
    print('error: sum %f' % m.summation())

m = numeric.Matrix(d5_3)
if m.summation() != 7:
    nb_errors += 1
    print('error: sum %f' % m.summation())

m = numeric.Matrix(d3_5)
if m.summation() != 7:
    nb_errors += 1
    print('error: sum %f' % m.summation())


# abs()
m = numeric.Matrix(dz5_3).abs()
if not m_eq(m, numeric.Matrix(dz5_3)):
    nb_errors += 1
    print('error: abs(0)')
    print(m)

for k in range(1, 10):
    m = numeric.identity(k).abs()
    if not m_eq(m, numeric.identity(k)):
        print('error: abs(identity(%i))' % k)
        print(m)

m = numeric.Matrix(d5_3).abs()
if m.summation() != 105:
    nb_errors += 1
    print('error: abs')
    print(m)

m = numeric.Matrix(d3_5).abs()
if m.summation() != 105:
    nb_errors += 1
    print('error: abs')
    print(m)


# transpose()
m = numeric.Matrix(dz5_3).transpose()
if not m_eq(m, numeric.Matrix(dz3_5)):
    nb_errors += 1
    print('error: transpose(0)')
    print(m)

for k in range(1, 10):
    m = numeric.identity(k).transpose()
    if not m_eq(m, numeric.identity(k)):
        print('error: transpose(identity(%i))' % k)
        print(m)

m = numeric.Matrix(d5_3).transpose()
if not m_eq(m, numeric.Matrix(d5_3t)):
    nb_errors += 1
    print('error: transpose')
    print(numeric.Matrix(d5_3))
    print(m)

m = numeric.Matrix(d3_5).transpose()
if not m_eq(m, numeric.Matrix(d3_5t)):
    nb_errors += 1
    print('error: transpose')
    print(numeric.Matrix(d3_5))
    print(m)


# inverse()
for k in range(1, 10):
    m = numeric.identity(k).inverse()
    if not m_eq(m, numeric.identity(k)):
        print('error: inverse(identity(%i))' % k)
        print(m)

    m = numeric.identity(k).scale(5).inverse()
    if not m_eq(m, numeric.identity(k).scale(1.0 / 5)):
        print('error: inverse(identity(%i)*5)' % k)
        print(m)

    m = numeric.identity(k)
    m[0, 0] = 0
    try:
        m = m.inverse()
        print('error: not inversible first: %i' % k)
        print(m)
    except ValueError:
        pass

    m = numeric.identity(k)
    m[k - 1, k - 1] = 0
    try:
        m = m.inverse()
        print('error: not inversible last: %i' % k)
        print(m)
    except ValueError:
        pass

mi = numeric.Matrix(d2_2).inverse()
if not m_eq(mi, numeric.Matrix(d2_2i), False):
    print('error: inverse 1')
    print(mi)
    print(numeric.Matrix(d2_2i))

mi = numeric.Matrix(d2_2i).inverse()
if not m_eq(mi, numeric.Matrix(d2_2), False):
    print('error: inverse 2')
    print(mi)
    print(numeric.Matrix(d2_2))


# Result
if nb_errors == 0:
    if not SIMPLEGUICS2PYGAME or (len(argv) != 2):
        print('Ok')
else:
    print('\n%i errors founded' % nb_errors)

    exit(nb_errors)
