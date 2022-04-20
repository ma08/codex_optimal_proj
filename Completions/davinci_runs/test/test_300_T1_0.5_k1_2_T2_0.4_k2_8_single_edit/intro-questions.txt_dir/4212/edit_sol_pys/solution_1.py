

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = a[i]
    for i in range(n-1):
        dp[i][i+1] = max(a[i], a[i+1])
    for k in range(2, n):
        for i in range(n-k):
            j = i + k
            dp[i][j] = max(a[i] + min(dp[i+2][j], dp[i+1][j-1]), a[j] + min(dp[i+1][j-1], dp[i][j-2]))
    print(dp[0][n-1])

if __name__ == '__main__':
    main()
