

# dp[i][j] = max(dp[i][j-1], dp[i-a_j][j-1] + 1)

def main():
    a = map(int, raw_input().split())
    dp = [[0 for _ in xrange(len(a) + 1)] for _ in xrange(max(a) + 1)]
    for i in xrange(len(a)):
        for j in xrange(1, max(a) + 1):
            dp[j][i+1] = dp[j][i]
            if a[i] <= j:
                dp[j][i+1] = max(dp[j][i+1], dp[j - a[i]][i] + 1)
    print max(dp[max(a)])
    return 0


if __name__ == "__main__":
    main()