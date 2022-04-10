

import sys
import math
import string
import random
import collections
import itertools
import re

#sys.stdin = open('input.txt')
#sys.stdout = open('output.txt', 'w')

def readline():
    return sys.stdin.readline().strip()

def readlines():
    return sys.stdin.readlines()

def read_ints():
    return [int(x) for x in readline().split()]

def print_line(x):
    print(x)
    sys.stdout.flush()

def print_lines(xs):
    print('\n'.join([str(x) for x in xs]))
    sys.stdout.flush()

def print_array(xs):
    print(' '.join([str(x) for x in xs]))
    sys.stdout.flush()

def array_to_string(arr, sep=' '):
    return sep.join([str(x) for x in arr])

def array_to_lines(arr, sep=' '):
    return '\n'.join([array_to_string(x, sep) for x in arr])

def matrix_to_lines(matrix, sep=' '):
    return '\n'.join([array_to_string(x, sep) for x in matrix])

def matrix_to_string(matrix, sep=' '):
    return '\n'.join([array_to_string(x, sep) for x in matrix])

def read_matrix(rows, columns, sep=' '):
    return [read_array(columns, sep) for _ in range(rows)]

def read_array(size, sep=' '):
    return [int(x) for x in readline().split(sep)]

def read_int():
    return int(readline())

def read_ints():
    return [int(x) for x in readline().split()]

def read_ints_array(size):
    return [int(x) for x in readline().split()]

def read_string():
    return readline().strip()

def read_strings():
    return readline().split()

def read_int_map(size):
    return {k: int(v) for k, v in itertools.zip_longest(itertools.count(), readline().split())}

def read_int_maps(size):
    return [read_int_map(size) for _ in range(size)]

def read_ints_array(size):
    return [int(x) for x in readline().split()]

def read_pair(sep=' '):
    return tuple(read_ints(sep=sep))

def read_pairs(size, sep=' '):
    return [read_pair(sep=sep) for _ in range(size)]

def read_triple(sep=' '):
    return tuple(read_ints(sep=sep))

def read_triples(size, sep=' '):
    return [read_triple(sep=sep) for _ in range(size)]

def read_quadruple(sep=' '):
    return tuple(read_ints(sep=sep))

def read_quadruples(size, sep=' '):
    return [read_quadruple(sep=sep) for _ in range(size)]

def read_quintuple(sep=' '):
    return tuple(read_ints(sep=sep))

def read_quintuples(size, sep=' '):
    return [read_quintuple(sep=sep) for _ in range(size)]

def read_sextuple(sep=' '):
    return tuple(read_ints(sep=sep))

def read_sextuples(size, sep=' '):
    return [read_sextuple(sep=sep) for _ in range(size)]

def read_int():
    return int(readline())

def read_int_array(size):
    return [int(x) for x in readline().split()]

def read_int_matrix(rows, columns):
    return [[int(x) for x in readline().split()] for _ in range(rows)]

def read_int_map(size):
    return {k: int(v) for k, v in itertools.zip_longest(itertools.count(), readline().split())}

def read_int_maps(size):
    return [read_int_map(size) for _ in range(size)]

def read_str():
    return readline().strip()

def read_str_array(size):
    return [x.strip() for x in readline().split()]

def read_str_matrix(rows, columns):
    return [read_str_array(columns) for _ in range(rows)]

def solve(n, d, k):
    if d > (n - 1):
        return False, []
    if d == 1:
        return True, [(i, i + 1) for i in range(1, n)]
    if d == 2:
        if n % 2 == 0:
            return True, [(i, i + 2) for i in range(1, n, 2)]
        else:
            return True, [(i, i + 2) for i in range(1, n - 1, 2)] + [(n - 1, n)]
    if d == 3:
        if n == 3:
            return True, [(1, 2), (2, 3)]
        if n == 4:
            return True, [(1, 2), (2, 3), (3, 4)]
        if n == 5:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5)]
        if n == 6:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        if n == 7:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
        if n == 8:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        if n == 9:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
        if n == 10:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
    if d == 4:
        if n == 4:
            return True, [(1, 2), (2, 3), (3, 4)]
        if n == 5:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5)]
        if n == 6:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        if n == 7:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
        if n == 8:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        if n == 9:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
        if n == 10:
            return True, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
    return False, []

def main():
    n, d, k = read_ints()
    ok, lines = solve(n, d, k)
    if ok:
        print('YES')
        print_lines([array_to_string(x) for x in lines])
    else:
        print('NO')

if __name__ == '__main__':
    main()