
import sys

def solve(a):
    n = len(a)
    dp = [1] * n
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            if a[j] == a[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    return dp


def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = solve(a)
    print(max(dp))
    for i, d in enumerate(dp):
        if d == max(dp):
            print(i - d + 2, i + 1)


if __name__ == '__main__':
    main()
