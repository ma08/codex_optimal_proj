import math

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]
    dp = [0] * N
    dp[0] = A[0]
    dp[1] = A[1]
    for i in range(2, N):
        dp[i] = max(dp[i - 1], dp[i - 2]) + A[i]
    print(dp[N - 1])

if __name__ == "__main__":
    main()
