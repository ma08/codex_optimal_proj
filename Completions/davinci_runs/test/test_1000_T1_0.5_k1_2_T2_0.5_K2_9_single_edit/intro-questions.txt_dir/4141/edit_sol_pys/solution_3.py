import math


def main():
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            if A[i] == B[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + C[A[i]-1])

    print(dp[N][M])

if __name__ == '__main__':
    main()
