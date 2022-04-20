
import random
import math
import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split(' '))

def solve(n, a, b):
    zeroes = 0
    neg = 0
    pos = 0
    for i in range(n):
        if a[i] == 0 and b[i] == 0:
            zeroes += 1
        elif a[i] < 0:
            neg += 1
        elif a[i] > 0:
            pos += 1
    return zeroes + min(neg, pos)

if __name__ == '__main__':
    n = read_int()
    a = read_ints()
    b = read_ints()
    print(solve(n, a, b))