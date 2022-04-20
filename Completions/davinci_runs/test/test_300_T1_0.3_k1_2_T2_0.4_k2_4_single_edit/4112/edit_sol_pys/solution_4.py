
import sys, collections

def main():
    n, k, x = map(int, sys.stdin.readline().split())
    a = collections.deque(map(int, sys.stdin.readline().split()))
    dp = [[[0 for _ in range(x+1)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(x+1):
                if i == j: dp[i][j][l] = max(dp[i][j][l], dp[i][j][l-1] + a[i])
                else:
                    if i - j + 1 >= k: dp[i][j][l] = max(dp[i][j][l], dp[i][j][l-1] + a[i])
                    if l > 1: dp[i][j][l] = max(dp[i][j][l], dp[i][i][l-1] + a[i])
                    dp[i][j][l] = max(dp[i][j][l], dp[i][j][l-1])
    print(max(dp[n-1][i][x] for i in range(n)))

if __name__ == '__main__':
    main()
