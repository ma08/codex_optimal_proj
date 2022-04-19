
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7


def main():
    return 0


def solve():
    return dfs(1, N - 1) * 2 % MOD


print(solve())
