

import itertools
import math
import collections
import functools
import heapq
import re
import numpy as np
from copy import deepcopy
from collections import deque

sys.setrecursionlimit(100000)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

def lcm(x, y): return (x * y) // math.gcd(x, y)

def sol():
    N, K = inp_list()
    h = inp_list()

    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1

    print(count)

sol()

import sys

N, K = list(map(int,sys.stdin.readline().split()))
h = list(map(int,sys.stdin.readline().split()))
