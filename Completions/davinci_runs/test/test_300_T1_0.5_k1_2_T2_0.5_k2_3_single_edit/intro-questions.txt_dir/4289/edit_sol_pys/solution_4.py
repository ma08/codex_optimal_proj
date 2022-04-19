

import os
# === import ======================================================================================================================================================
import re
import math
import itertools
from collections import deque
from collections import defaultdict
from collections import Counter
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd
from functools import reduce
import sys

inf = float("inf")
mod = 1000000007
sys.setrecursionlimit(200000)

# === functions ===================================================================================================================================================
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())
# === const =======================================================================================================================================================

# === classes =====================================================================================================================================================
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
 
    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())
 

# === main ========================================================================================================================================================
def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))

    dif = [abs(t - h[i] * 0.006 - a) for i in range(n)]
    ans = dif.index(min(dif)) + 1
    print(ans)

# ==================================================================================
if __name__ == "__main__":
    main()
