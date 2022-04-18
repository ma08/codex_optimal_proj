

import sys

def main():
    N, M, X = map(int, sys.stdin.readline().split())
    C = []
    A = []
    for _ in range(N):
        c = list(map(int, sys.stdin.readline().split()))
        C.append(c[0])
        A.append(c[1:])
    
    INF = float("inf")
    dp = [[INF] * (M+1) for _ in range(N+1)] # dp[i][j] := i番目までの本を読んだ時にj冊読むのにかかる最小コスト
    dp[0][0] = 0
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + C[i]) # i番目の本を読む
            for k in range(M):
                dp[i+1][k] = min(dp[i+1][k], dp[i][j] + C[i] - A[i][j] + A[i][k]) # i番目の本を読まない
    
    if X in dp[N]:
        print(dp[N][X])
    else:
        print(-1)

if __name__ == "__main__":
    main()
