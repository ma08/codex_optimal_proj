import math
import heapq
import bisect
import random
import numpy as np
from collections import Counter, deque
from itertools import combinations, permutations, accumulate, product, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left, bisect_right
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline 
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []
def main():
    n = i_input()
    num_list = i_list()
    num_list.sort()
    print(num_list[0])
if __name__ == '__main__':
    main()

import sys

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    for z in range(x + 1, y):
        if all(z > x_i for x_i in x_list) and all(z <= y_i for y_i in y_list):
            print("No War")
            sys.exit()

    print("War")

if __name__ == '__main__':
    main()
