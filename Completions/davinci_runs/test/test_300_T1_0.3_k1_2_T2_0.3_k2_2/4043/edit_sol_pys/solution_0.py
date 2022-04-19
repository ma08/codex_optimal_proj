
import sys
import math
import heapq
import itertools
import string
import queue
import copy
import collections
import time

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def print_matrix(mat):
    for row in mat:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    n, d, k = map(int, input().split())

    print('NO')
