

def main(n, a):
    dp = [0] * n
    for i in range(n):
        dp[i] = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = a[i]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1] + a[i] + a[j])
    print(dp[0][n - 1])


n = int(input())
a = [int(x) for x in input().split()]
main(n, a)
