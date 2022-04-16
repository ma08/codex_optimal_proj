import sys
sys.setrecursionlimit(10 ** 5)

A, B = map(int, input().split())

def dfs(N, n):
    if n > N:
        return 0
    elif n == N:
        return 1
    else:
        return dfs(N, n + 1) + dfs(N, n + 2)

print(dfs(B, A))
