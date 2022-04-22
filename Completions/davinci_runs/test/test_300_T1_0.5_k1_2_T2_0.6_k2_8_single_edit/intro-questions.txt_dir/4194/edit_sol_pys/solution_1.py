

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[-1] >= n:
    print(-1)
    exit()


def dfs(i, s):
    if i == m:
        return n - s

    if s + a[i] >= n:
        return 0

    return max(dfs(i+1, s), dfs(i+1, s + a[i]))


print(dfs(0, 0))
