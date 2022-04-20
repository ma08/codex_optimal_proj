

import sys

def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[0] * M] * N
    for i in range(N):
        c = list(map(int, input().split()))
        C[i] = c[0]
        A[i] = c[1:]
    
    INF = float("inf")
    dp = [[INF] * (M+1) for i in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + C[i])
            for k in range(M):
                dp[i+1][k] = min(dp[i+1][k], dp[i][j] + C[i] - A[i][j] + A[i][k])
    
    if X in dp[N]:
        print(dp[N][X])
    else:
        print(-1)

if __name__ == "__main__":
    main()
