

import sys

def solve(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if a[i] == a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n - 1]

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(a))

if __name__ == '__main__':
    main()
