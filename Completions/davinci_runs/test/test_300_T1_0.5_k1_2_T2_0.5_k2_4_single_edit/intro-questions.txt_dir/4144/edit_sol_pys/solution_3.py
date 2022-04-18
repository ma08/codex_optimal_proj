
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def dfs(start, n):
    if start > 9:
        return 0
    if n == 1:
        return 1
    res = dfs(start + 1, n - 1) + dfs(start, n - 1)
    return res % MOD


def solve():
    return dfs(1, N - 1) * 2 % MOD


print(solve())
