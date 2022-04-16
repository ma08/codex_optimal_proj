
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def solve(n):
    if n == 1:
        return 1
    res = solve(n - 1) + solve(n - 1)
    return res % MOD


print(solve(N - 1) * 2 % MOD)
