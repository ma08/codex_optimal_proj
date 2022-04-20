

import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    broken_steps = set(map(int, sys.stdin.read().split()))
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i - 1 not in broken_steps:
            dp[i] += dp[i - 1]
        if i - 2 not in broken_steps:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000007
    print(dp[-1])


if __name__ == '__main__':
    main()