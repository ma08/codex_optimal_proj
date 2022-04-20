

from collections import deque
from itertools import combinations
from sys import stdin
from typing import Deque, Iterable, List, Tuple


def main() -> None:
    n, a, b, c = map(int, stdin.readline().split())
    ls: List[int] = [int(stdin.readline()) for _ in range(n)]

    # dp[i][j]: i: the length of the bamboo, j: the number of bamboos with the length i
    # dp[i][j] = min(dp[i - 1][j], dp[i - 2][j] + 1, dp[i - 1][j - 1] + 10)
    dp: List[List[int]] = [[float("inf") for _ in range(n + 1)] for _ in range(a + 1)]
    dp[0][0] = 0
    for i in range(1, a + 1):
        for j in range(n + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i - 2][j] + 1, dp[i - 1][j - 1] + 10)

    def solve(a: int, b: int, c: int, ls: Iterable[int]) -> int:
        if a < b or b < c:
            return float("inf")

        count: int = 0
        for l in ls:
            count += 1 if l >= a else 0

        return dp[a][count] + dp[b][count] + dp[c][count]

    print(min(solve(a, b, c, ls),
              solve(a, c, b, ls),
              solve(b, a, c, ls),
              solve(b, c, a, ls),
              solve(c, a, b, ls),
              solve(c, b, a, ls)))


if __name__ == '__main__':
    main()