
import sys

def max_beauty_sum(n, k, x, a):
    dp = [[0 for i in range(x+1)] for j in range(n)]
    dp[0][1] = a[0]
    for i in range(n):
        for j in range(x):
            dp[i][j+1] = dp[i][j]
            if i >= k-1:
                for r in range(j+1):
                    dp[i][j+1] = max(dp[i][j+1], dp[i-k+1][r] + a[i])
    return dp[n-1][x]

def main():
    line = sys.stdin.readline()
    n, k, x = [int(x) for x in line.split()]
    line = sys.stdin.readline()
    a = [int(x) for x in line.split()]
    print(max_beauty_sum(n, k, x, a))

if __name__ == '__main__':
    main()
