

import sys

def main():
    N, M, X = map(int, sys.stdin.readline().split())
    c = []
    a = []
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        c.append(line[0])
        a.append(line[1:])
    
    INF = float("inf")
    dp = [[INF] * (M+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + c[i])
            for k in range(M):
                dp[i+1][k] = min(dp[i+1][k], dp[i][j] + c[i] - a[i][j] + a[i][k])
    
    if X in dp[N]:
        print(dp[N][X])
    else:
        print(-1)

if __name__ == "__main__":
    main()
