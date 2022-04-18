
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def dfs(i, n):
    if i > 9:
        return 0
    if n == 1:
        return 1
    res = dfs(i + 1, n - 1) + dfs(i, n - 1)
    return res % MOD


def solve():
    return dfs(0, N) * 2 % MOD


print(solve())
