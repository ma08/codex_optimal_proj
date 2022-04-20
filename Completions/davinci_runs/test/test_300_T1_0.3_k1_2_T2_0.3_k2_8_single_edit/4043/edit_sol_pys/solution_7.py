

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
                print(1, 4)
                print(2, 4)
                print(3, 4)
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
                print(1, 4)
                print(2, 4)
                print(3, 4)
                print(5, 6)
                print(5, 7)
                print(5, 8)
                print(6, 9)
                print(6, 10)
                print(7, 11)
                print(7, 12)
                print(8, 13)
                print(8, 14)
                print(9, 15)
                print(10, 16)
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
                print(1, 4)
                print(2, 4)
                print(3, 4)
                print(5, 6)
                print(5, 7)
                print(5, 8)
                print(6, 9)
                print(6, 10)
                print(7, 11)
                print(7, 12)
                print(8, 13)
                print(8, 14)
                print(9, 15)
                print(10, 16)
                print(11, 17)
                print(11, 18)
                print(11, 19)
                print(12, 20)
                print(12, 21)
                print(13, 22)
                print(13, 23)
                print(14, 24)
                print(14, 25)
                print(15, 26)
                print(16, 27)
                print(17, 28)
                print(18, 29)
                print(19, 30)
                print(20, 31)
                print(21, 32)
                print(22, 33)
                print(23, 34)
                print(24, 35)
                print(25, 36)
                print(26, 37)
                print(27, 38)
                print(28, 39)
                print(29, 40)
                print(30, 41)
                print(31, 42)
                print(32, 43)
                print(33, 44)
                print(34, 45)
                print(35, 46)
                print(36, 47)
                print(37, 48)
                print(38, 49)
                print(39, 50)
                print(40, 51)
                print(41, 52)
                print(42, 53)
                print(43, 54)
                print(44, 55)
                print(45, 56)
                print(46, 57)
                print(47, 58)
                print(48, 59)
                print(49, 60)
                print(50, 61)
                print(51, 62)
                print(52, 63)
                print(53, 64)
                print(54, 65)
                print(55, 66)
                print(56, 67)
                print(57, 68)
                print(58, 69)
                print(59, 70)
                print(60, 71)
                print(61, 72)
                print(62, 73)
                print(63, 74)
                print(64, 75)
                print(65, 76)
                print(66, 77)
                print(67, 78)
                print(68, 79)
                print(69, 80)
                print(70, 81)
                print(71, 82)
                print(72, 83)
                print(73, 84)
                print(74, 85)
                print(75, 86)
                print(76, 87)
                print(77, 88)
                print(78, 89)
                print(79, 90)
                print(80, 91)
                print(81, 92)
                print(82, 93)
                print(83, 94)
                print(84, 95)
                print(85, 96)
                print(86, 97)
                print(87, 98)
                print(88, 99)
                print(89, 100)
    else:
        print('NO')
