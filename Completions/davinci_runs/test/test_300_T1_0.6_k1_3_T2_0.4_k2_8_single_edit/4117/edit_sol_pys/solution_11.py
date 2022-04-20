

import fractions
import itertools
import math
import sys

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()

INF = float('inf')


n = I()
L = LI()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                if L[i] + L[j] > L[k] and L[k] + L[j] > L[i] and L[i] + L[k] > L[j]:
                    ans += 1
print(ans)

"""
import fractions
import itertools
import math
import sys

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return sys.stdin.readline().rstrip()
def LS(): return sys.stdin.readline().split()

INF = float('inf')


n = I()
L = LI()
L.sort()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                if L[i] + L[j] > L[k] and L[k] + L[j] > L[i] and L[i] + L[k] > L[j]:
                    ans += 1
print(ans)
"""
