
import sys
from collections import Counter
import heapq
import math
import itertools
import collections
from collections import deque
import numpy as np
sys.setrecursionlimit(10000)


def I(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LMI(): return list(map(int, sys.stdin.readline().split()))


MOD = 10 ** 9 + 7
INF = float('inf')


def main():
    N, M = MI()
    A = LMI()
    A.sort()
    B = LMI()
    B.sort()
    C = LMI()
    C.sort()
    ans = 0
    for b in B:
        a = bisect.bisect_left(A, b)
        c = bisect.bisect_right(C, b)
        ans += a * (N - c)
    print(ans)


if __name__ == "__main__":
    main()
