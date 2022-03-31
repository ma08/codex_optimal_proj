

import sys
import heapq
import math
from collections import Counter, deque
from itertools import combinations, permutations, product

sys.setrecursionlimit(10000)

def read_list_int():
    return list(map(int, input().split(' ')))

def read_single_int():
    return int(input())

def read_single_str():
    return input()

def solve(n, s):
    c = [0] * n
    c[0] = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            c[i] = c[i - 1] + 1
        else:
            c[i] = c[i - 1]
    return c

def main():
    n = read_single_int()
    s = read_single_str()
    c = solve(n, s)
    print(max(c))
    print(' '.join(map(str, c)))

if __name__ == '__main__':
    main()