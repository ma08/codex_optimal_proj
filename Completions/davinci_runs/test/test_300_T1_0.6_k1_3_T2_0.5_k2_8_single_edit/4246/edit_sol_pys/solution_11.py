import sys
import math
import collections
import itertools
import array
import inspect


# Set max recursion limit
sys.setrecursionlimit(10000)

# Debug output
def chkprint(*args):
    names = {id(v):k for k,v in inspect.currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

# Binary converter
def to_bin(x):
    return bin(x)[2:]

# Set 2 dimension list
def dim2input(N):
    li = []
    for _ in range(N):
        li.append(list(map(int, input())))
    return li

# --------------------------------------------

dp = None

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [float("inf")] * N
    dp[0] = 0

    for i in range(N):
        for j in range(1, K+1):
            if i + j < N:
                dp[i+j] = min(dp[i+j], dp[i] + abs(h[i] - h[i+j]))

    print(dp[-1])

main()
