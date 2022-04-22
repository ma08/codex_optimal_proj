import sys
sys.setrecursionlimit(10**6)


def dfs(n):
    if n == 1:
        return 1
    else:
        return n*dfs(n-1)


n = int(input())
print(dfs(n))
