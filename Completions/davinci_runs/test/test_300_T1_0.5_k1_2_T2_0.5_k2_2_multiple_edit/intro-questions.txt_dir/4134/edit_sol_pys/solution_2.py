

def solve(n, m, k, grid, dp):
    if dp[n][m][k] != -1: # if dp table is not empty
    # do dp
        return dp[n][m][k]
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[-1 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    print(solve(n, m, k, grid, dp))

if __name__ == '__main__':
    main()
