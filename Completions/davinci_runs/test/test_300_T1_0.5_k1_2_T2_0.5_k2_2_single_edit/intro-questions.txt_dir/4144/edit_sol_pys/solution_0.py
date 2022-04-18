
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def dfs(digit, n):
    if digit > 9:
        return 0
    if n == 1:
        return 1
    res = dfs(digit + 1, n - 1) + dfs(digit, n - 1)
    return res % MOD


def solve():
    return dfs(1, N - 1) * 2 % MOD


print(solve())
