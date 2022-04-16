
import sys
import os

def main():
    s = sys.stdin.readline()
    s = s.split(' ')
    N = int(s[0])
    M = int(s[1])
    A = [int(x) for x in sys.stdin.readline().split(' ')] 
    B = [int(x) for x in sys.stdin.readline().split(' ')] 

    # We solve this problem by using the following dynamic programming matrix:
    # dp[i][j] = the minimum number of coins needed to make change for i cents
    # using coins from the first j denominations.
    #
    # We then fill this matrix in row-major order.
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(1, N+1):
            # If the coin value is greater than the amount of change we need to make,
            # then we can't use this coin, so we just copy the previous solution.
            if A[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                # Otherwise, we have two options:
                # 1. Use the coin.
                # 2. Don't use the coin.
                # We take the minimum of these two options and add one to it.
                dp[i][j] = min(dp[i-1][j], dp[i][j-A[i-1]]) + 1

    # The answer is the last element in the matrix.
    print(dp[M][N])

if __name__ == '__main__':
    main()
