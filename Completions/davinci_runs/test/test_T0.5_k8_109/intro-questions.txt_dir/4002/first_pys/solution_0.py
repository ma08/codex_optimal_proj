

def get_max_sum(n, m, k, a):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if j <= m//2:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + a[i-1][j-1])
    return max(dp[n])

def main():
    n, m, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(get_max_sum(n, m, k, a))


if __name__ == '__main__':
    main()