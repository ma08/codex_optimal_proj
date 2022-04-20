

import sys
import numpy as np
import math
import collections
import copy
import decimal
import itertools
import fractions
import heapq
from collections import deque
from functools import reduce
from itertools import product
from itertools import combinations
input = sys.stdin.readline
# np.set_printoptions(suppress=True)
# np.set_printoptions(precision=3)
# sys.exit()

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LLIL(n): return [LI() for _ in range(n)]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def DP(N, M, first): return [[first] * M for n in range(N)]
def DP3(N, M, L, first): return [[[first] * L for n in range(M)] for _ in range(N)]

def main():
    d, t, s = LI()

    if d/s <= t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
