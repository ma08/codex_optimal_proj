

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i >= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][k])
    i = n
    j = k
    result = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            result.append(i-j+1)
            i -= i-j+1
            j -= 1
    result.reverse()
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()