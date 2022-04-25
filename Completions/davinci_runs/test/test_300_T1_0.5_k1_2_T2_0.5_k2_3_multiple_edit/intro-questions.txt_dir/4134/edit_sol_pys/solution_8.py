
def solve(n, m, k, grid):
    dp = [[0 for _ in range(m)] for _ in range(n)]
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
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            max_value = max(max_value, dp[i][j])
    return max_value

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
