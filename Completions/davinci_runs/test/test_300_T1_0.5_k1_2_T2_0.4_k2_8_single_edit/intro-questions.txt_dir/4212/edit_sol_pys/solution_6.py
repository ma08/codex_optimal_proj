

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for i in range(q)]
    abcd.sort(key=lambda x: x[1])
    dp = [[0 for j in range(m)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(m):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:  # a < b, c <= d
        for j in range(m-1, c-1, -1):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)

    print(max(dp[n]))

if __name__ == '__main__':
    main()
