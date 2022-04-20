

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i + 1 < n:
                dp[i + 1][j] += dp[i][j]
            if j + 1 < m:
                dp[i][j + 1] += dp[i][j]
    print(dp)

if __name__ == '__main__':
    main()
