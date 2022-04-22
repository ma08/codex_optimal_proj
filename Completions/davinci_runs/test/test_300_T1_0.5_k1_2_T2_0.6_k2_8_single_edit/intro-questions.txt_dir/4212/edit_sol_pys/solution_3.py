
def main():
    N, M, Q = map(int, input().split())
    abcd = [list(map(int, input().split())) for _ in range(Q)]
    abcd.sort(key=lambda x: (x[1], -x[0]))
    dp = [[0 for _ in range(M)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(M):
            dp[i][j] = dp[i-1][j]

    for a, b, c, d in abcd:
        for j in range(c, M):
            dp[b][j] = max(dp[b][j], dp[a][j-c] + d)

    print(max(dp[N]))


if __name__ == '__main__':
    main()
