

import sys

def solve(a):
    n = len(a) + 1
    dp = [1] * n
    for i in range(1, n + 1):
        for j in range(i - 1, 0, -1):
            if a[i] == a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[1:]

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = solve(a)
    for i, d in enumerate(dp):
        if d == max(dp) and a[i] == a[i - 1]:
            print(a[i])
            break

if __name__ == '__main__':
    main()
