
def solve(n, m, k, grid, dp):
    return dp

def main():
    n, m, k = map(int, input().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    grid = [list(map(int, input().split())) for _ in range(n)]

    max_value = -1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j] + k
            max_value = max(max_value, dp[i][j])
    print(max_value)

if __name__ == '__main__':
    main()
