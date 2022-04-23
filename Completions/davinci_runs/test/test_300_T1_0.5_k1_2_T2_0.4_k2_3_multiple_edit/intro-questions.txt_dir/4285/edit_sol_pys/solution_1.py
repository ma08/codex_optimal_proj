
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def solve():
    n = int(input())
    s = input().strip()
    mod = 10 ** 9 + 7

    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3):
            if s[i] == '?':
                for k in range(3):
                    dp[i + 1][k] += dp[i][j]
                    dp[i + 1][k] %= mod
            else:
                dp[i + 1][ord(s[i]) - ord('a')] += dp[i][j]
                dp[i + 1][ord(s[i]) - ord('a')] %= mod

    return sum(dp[n]) % mod


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(solve(n, s))
