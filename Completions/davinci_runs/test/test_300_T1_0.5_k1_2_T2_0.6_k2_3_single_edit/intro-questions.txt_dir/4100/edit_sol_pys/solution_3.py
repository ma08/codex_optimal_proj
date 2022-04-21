

import sys
import os
from collections import deque
from collections import Counter

def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()


INF = float('inf')


n, m = LI()
a = LI()


def main():
    a.sort()
    b = []
    for i in range(n-1):
        b.append(a[i+1] - a[i])
    b.sort()
    print(sum(b[:n-m]))


main()
