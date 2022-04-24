import sys
sys.setrecursionlimit(10**6)

import math

def main():
    # Read Input
    N = int(input())
    h = list(map(int, input().split()))

    # Calc
    dp = [float("inf")] * N
    dp[0] = 0

    for i in range(1, N):
        dp[i] = min(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
        if i > 1:
            dp[i] = min(dp[i], dp[i-2] + abs(h[i] - h[i-2]))

    # Print Answer
    print(dp[-1])

if __name__ == '__main__':
    main()
