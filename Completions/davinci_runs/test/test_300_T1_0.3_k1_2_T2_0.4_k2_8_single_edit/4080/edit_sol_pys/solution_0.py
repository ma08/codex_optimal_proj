

import sys
import math
import heapq
import bisect
import random
import itertools
import collections
import fractions
import re
import functools

def solve(n, k, s):
    return 0

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    segs = []
    for i in range(m):
        l, r = map(int, input().split())
        segs.append((l, r))
    ans, q, c = solve(n, a, m, segs)
    print(ans)
    print(q)
    print(' '.join(map(str, c)))

if __name__ == '__main__':
    main()
