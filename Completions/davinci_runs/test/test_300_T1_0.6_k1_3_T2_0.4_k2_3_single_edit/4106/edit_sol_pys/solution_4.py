
import sys

def max_beauty_sum(n, k, x, a):
    dp = []
    for i in range(n):
        dp[i] = [0 for j in range(x+1)]
    dp[0][1] = a[0]
    for i in range(1, n):
        for j in range(1, x+1):
            dp[i][j] = dp[i-1][j]
            if i >= k-1:
                for r in range(1, j+1):
                    dp[i][j] = max(dp[i][j], dp[i-k][j-r] + a[i])
    return dp[n-1][x]

def main():
    line = sys.stdin.readline()
    n, k, x = [int(x) for x in line.split()]
    line = sys.stdin.readline()
    a = [int(x) for x in line.split()]
    print(max_beauty_sum(n, k, x, a))

if __name__ == '__main__':
    main()
