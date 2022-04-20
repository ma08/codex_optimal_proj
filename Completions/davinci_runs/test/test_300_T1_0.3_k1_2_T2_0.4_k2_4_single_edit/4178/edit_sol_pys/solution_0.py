

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

def dfs(i, m, s):
    if m == 0:
        return s
    if i >= N:
        return 10**10
    res = dfs(i+1, m, s)
    res = min(res, dfs(i+1, m-1, s+A[i]))
    return res

ans = dfs(0, M, 0)
print(ans)
