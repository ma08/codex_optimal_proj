

import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(0, i):
            if a[i] > a[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    print(max(dp))


if __name__ == "__main__":
    main()