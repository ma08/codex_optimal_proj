

import sys

def main():
    n, a, b, c = map(int, sys.stdin.readline().split())
    ls = []
    for i in range(n):
        ls.append(int(sys.stdin.readline()))

    if a < b < c:
        a, b, c = c, b, a

    dp = [[[float("inf") for i in range(101)] for j in range(101)] for k in range(101)]
    dp[0][0][0] = 0

    for l in ls:
        for i in range(a+1):
            for j in range(b+1):
                for k in range(c+1):
                    if dp[i][j][k] != float("inf"):
                        dp[i][j][k] += 1
                        dp[i][j][k+l] = min(dp[i][j][k+l], dp[i][j][k] + (l-1))
                        dp[i][j+l][k] = min(dp[i][j+l][k], dp[i][j][k] + (l-1))
                        dp[i+l][j][k] = min(dp[i+l][j][k], dp[i][j][k] + (l-1))
                        dp[i+l][j+l][k] = min(dp[i+l][j+l][k], dp[i][j][k] + 10 + (l-2))
                        dp[i+l][j][k+l] = min(dp[i+l][j][k+l], dp[i][j][k] + 10 + (l-2))
                        dp[i][j+l][k+l] = min(dp[i][j+l][k+l], dp[i][j][k] + 10 + (l-2))

    print(dp[a][b][c])


if __name__ == '__main__':
    main()