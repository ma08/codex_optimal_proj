
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def dfs(s, n):
    if s > 9:
        return 0
    if n == 1:
        return 1
    res = dfs(s + 1, n - 1) + dfs(s, n - 1)
    return res % MOD


def solve():
    return dfs(0, N)


print(solve())
