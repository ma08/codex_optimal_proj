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

def main_2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    global dp
    dp = [[0] * (N+1) for _ in range(N+1)]

    def rec(i, j):
        if dp[i][j] > 0:
            return dp[i][j]
        if i == j:
            dp[i][j] = 0
            return dp[i][j]
        if i > j:
            dp[i][j] = 0
            return dp[i][j]
        tmp = float("inf")
        for k in range(i, j):
            tmp = min(tmp, rec(i, k) + rec(k+1, j) + A[j] - A[i])
        dp[i][j] = tmp
        return dp[i][j]

    print(rec(0, N-1))

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    dp = [[0] * (N+1) for _ in range(N+1)]

    for k in range(N):
        for i in range(N):
            j = i + k
            if j >= N:
                continue
            if i == j:
                dp[i][j] = 0
                continue
            tmp = float("inf")
            for l in range(i, j):
                tmp = min(tmp, dp[i][l] + dp[l+1][j] + A[j] - A[i])
            dp[i][j] = tmp

    print(dp[0][N-1])

def main_org():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    dp = [[0] * (N+1) for _ in range(N+1)]

    for k in range(N):
        for i in range(N):
            j = i + k
            if j >= N:
                continue
            if i == j:
                dp[i][j] = 0
                continue
            tmp = float("inf")
            for l in range(i, j):
                tmp = min(tmp, dp[i][l] + dp[l+1][j] + A[j] - A[i])
            dp[i][j] = tmp

    print(dp[0][N-1])

def main_org2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    dp = [[0] * (N+1) for _ in range(N+1)]

    for k in range(1, N):
        for i in range(N-k):
            j = i + k
            if i == j:
                dp[i][j] = 0
                continue
            tmp = float("inf")
            for l in range(i, j):
                tmp = min(tmp, dp[i][l] + dp[l+1][j] + A[j] - A[i])
            dp[i][j] = tmp

    print(dp[0][N-1])

if __name__ == '__main__':
    main()
