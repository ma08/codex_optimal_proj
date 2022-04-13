

def main():
    n, m, q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(q)]
    abcd.sort(key=lambda x: (x[1], x[0]))
    dp = [[0] * m for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i] = dp[i-1][:]

    for a, b, c, d in abcd:
        for j in range(c, m):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)

    print(max(dp[n]))

if __name__ == '__main__':
    main()
