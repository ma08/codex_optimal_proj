
import sys


def input():
    return sys.stdin.readline().strip()


def main():
    s = list(input())
    t = list(input())
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(len(t)):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
    print(len(s) + len(t) - dp[len(s)][len(t)])


if __name__ == '__main__':
    main()
