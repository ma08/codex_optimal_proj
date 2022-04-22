# -*- coding: utf-8 -*-
import math
import random

import collections
import bisect
import heapq
import time
inf = 10**9
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
import sys

def can_eq(s, t):
    if len(s) != len(t):
        return False
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    return s_list == t_list

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

if can_eq(s, t):
    print('Yes')
else:
    print('No')
