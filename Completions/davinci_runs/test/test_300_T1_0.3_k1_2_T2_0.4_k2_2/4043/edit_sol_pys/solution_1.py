
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

    if d == 1:
        print('YES')
        for i in range(1, n):
            print(i, i+1)
    elif d == 2:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            print('NO')
    elif d == 3:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            if n == 3:
                print('NO')
            else:
                print('YES')
                print(1, 2)
                print(1, 3)
                print(2, 4)
                print(3, 5)
                print(3, 6)
                print(4, 7)
                print(4, 8)
                print(5, 9)
                print(5, 10)
    elif d == 4:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            if n == 4:
                print('NO')
            else:
                print('YES')
                print(1, 2)
                print(1, 3)
                print(1, 5)
                print(2, 6)
                print(2, 7)
                print(3, 8)
                print(3, 9)
                print(4, 10)
                print(4, 11)
                print(5, 12)
                print(6, 13)
                print(7, 14)
                print(8, 15)
                print(9, 16)
                print(10, 17)
    elif d == 5:
        if k >= n - 1:
            print('YES')
            for i in range(1, n):
                print(i, i+1)
        else:
            if n == 5:
                print('NO')
            else:
                print('YES')
                print(1, 2)
                print(1, 3)
                print(1, 5)
                print(2, 6)
                print(2, 7)
                print(3, 8)
                print(3, 9)
                print(4, 10)
                print(4, 11)
                print(5, 12)
                print(6, 13)
                print(7, 14)
                print(8, 15)
                print(9, 16)
                print(10, 17)
                print(11, 18)
                print(12, 19)
                print(13, 20)
                print(14, 21)
                print(15, 22)
                print(16, 23)
    else:
        print('NO')
