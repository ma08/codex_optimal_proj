import sys
sys.setrecursionlimit(10**6)


N = int(input())
A = list(map(int, input().split()))


def dfs(i, m):
    if m == 0:
        return 1
    if i >= N:
        return 0
    res = dfs(i+1, m) or dfs(i+1, m-A[i])
    return res


Q = int(input())
M = list(map(int, input().split()))
for m in M:
    if dfs(0, m):
        print('yes')
    else:
        print('no')
