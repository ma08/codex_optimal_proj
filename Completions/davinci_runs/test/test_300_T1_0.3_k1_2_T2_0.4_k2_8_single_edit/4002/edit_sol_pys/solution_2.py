

def main():
    n, m, k = map(int, input().split())
    a = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = int(input())
    dp = [[0] * (k + 1) for i in range(m + 1)]
    for i in range(n):
        for j in range(m):
            for x in range(k):
                dp[j + 1][(x + a[i][j]) % k] = max(dp[j + 1][(x + a[i][j]) % k], dp[j][x] + a[i][j])
    print(dp[m][0])

main()
