
import sys

def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[0] * M] * N
    for _ in range(N):
        c = list(map(int, input().split()))
        C[_] = c[0]
        A[_] = c[1:]
    
    INF = float("inf")
    dp = [[INF] * (M+1) for _ in range(N)]
    dp[0][0] = 0
        for j in range(M+1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + C[i])
                for k in range(M):
                    dp[i][k] = min(dp[i][k], dp[i][j-1] + C[i] - A[i][j-1] + A[i][k])
    
    if X in dp[N-1]:
        print(dp[N-1][X])
    else:
        print(-1)

if __name__ == "__main__":
    main()
