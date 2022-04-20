

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    # print(grid)

    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # print(dp)
    ans = 0
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i == 0:
                if grid[i][j] ^ grid[i][j-1] == k:
                    ans += dp[i][j-1]
            elif j == 0:
                if grid[i][j] ^ grid[i-1][j] == k:
                    ans += dp[i-1][j]
            else:
                if grid[i][j] ^ grid[i-1][j] == k:
                    ans += dp[i-1][j]
                if grid[i][j] ^ grid[i][j-1] == k:
                    ans += dp[i][j-1]
    print(ans)


if __name__ == '__main__':
    main()