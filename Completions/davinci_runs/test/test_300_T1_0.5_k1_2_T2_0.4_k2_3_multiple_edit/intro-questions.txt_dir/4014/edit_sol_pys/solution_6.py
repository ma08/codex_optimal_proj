
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
    N, K = MAP()
    A = LIST()

    d = defaultdict(int)
    for a in A:
        d[a] += 1

    if len(d) <= K:
        print(0)
        return

    ans = 0
    for k, v in sorted(d.items(), key=itemgetter(1), reverse=True)[K:]:
        ans += v

    print(ans)



if __name__ == "__main__":
    main()
