import sys


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    dp = [0] * n
    dp[0] = a[0]
    for i in range(1, n):
        dp[i] = a[i] + dp[i - 1]
    ans = 0
    for i in range(n):
        ans += dp[i]
    print(ans)


if __name__ == "__main__":
    main()
