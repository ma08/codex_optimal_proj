

def main():
    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (k + 1) for _ in range(m + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for d in range(k):
                dp[j][(j * a[i - 1][j - 1] + d) % k] = max(dp[j][(j * a[i - 1][j - 1] + d) % k], dp[j - 1][d] + a[i - 1][j - 1])
    print(dp[m][0])

if __name__ == '__main__':
    main()