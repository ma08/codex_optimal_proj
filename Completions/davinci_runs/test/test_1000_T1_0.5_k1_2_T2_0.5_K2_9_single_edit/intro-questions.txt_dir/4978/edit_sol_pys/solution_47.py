
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import math
from itertools import permutations
from itertools import combinations
from itertools import product
from copy import deepcopy
from collections import deque
from collections import Counter
import heapq as hpq
from fractions import gcd
from functools import reduce
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())
MOD = 10**9+7
INF = 10**20
LMAX = 10**5
NMAX = 10**5
def main():
    s = input()
    n = len(s)
    a = [0]*n
    b = [0]*n
    for i in range(n):
        if s[i] == "R":
            a[i] = 1
        if s[i] == "L":
            b[i] = 1
    for i in range(1,n):
        a[i] += a[i-1]
        b[i] += b[i-1]
    for i in range(n-1,0,-1):
        a[i-1] += a[i]
        b[i-1] += b[i]
    #print(a)
    #print(b)
    for i in range(n):
        if s[i] == ".":
            print(a[i],b[i])
if __name__ == '__main__':
    main()
