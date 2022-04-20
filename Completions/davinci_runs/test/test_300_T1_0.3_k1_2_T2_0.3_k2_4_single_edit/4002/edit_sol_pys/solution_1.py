

def main():
    n, m, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    dp = [[0] * (k + 1) for i in range(m + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for x in range(k + 1):
                dp[j][(x + a[i - 1][j - 1]) % k] = max(dp[j][(x + a[i - 1][j - 1]) % k], dp[j - 1][x] + a[i - 1][j - 1])
    print(dp[m][0])

main()
