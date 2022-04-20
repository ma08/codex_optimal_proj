
def main():
    N, M, K = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0] * (K + 1) for i in range(M + 1)]
    for i in range(N):
        for j in range(M):
            for x in range(K):
                dp[j + 1][(x + A[i][j]) % K] = max(dp[j + 1][(x + A[i][j]) % K], dp[j][x] + A[i][j])
    print(dp[M][0])

main()
