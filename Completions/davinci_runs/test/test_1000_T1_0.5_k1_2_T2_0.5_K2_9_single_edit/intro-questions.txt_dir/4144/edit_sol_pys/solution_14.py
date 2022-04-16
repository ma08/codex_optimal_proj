
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def dfs(x, n):
    if x > 9:
        return 0
    if n == 1:
        return 1
    res = dfs(x + 1, n - 1) + dfs(x, n - 1)
    return res % MOD


def solve():
    return dfs(1, N - 1) * 2 % MOD


print(solve())
