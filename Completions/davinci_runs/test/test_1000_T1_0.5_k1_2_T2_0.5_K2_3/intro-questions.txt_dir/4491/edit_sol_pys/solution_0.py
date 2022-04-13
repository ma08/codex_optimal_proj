

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(2)]
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = A[0][0] # dp[i][j] : i번째 행에서 j번째 열에 있을 때 최대값
    dp[1][0] = A[1][0] # dp[i][j] : i번째 행에서 j번째 열에 있을 때 최대값
    for i in range(1, N):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1]) + A[0][i] # dp[0][i]는 dp[0][i - 1]과 dp[1][i - 1]중 큰 값에서 오는 것이다.
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + A[1][i] # dp[1][i]는 dp[0][i - 1]과 dp[1][i - 1]중 큰 값에서 오는 것이다.
    print(max(dp[0][N - 1], dp[1][N - 1]))

if __name__ == "__main__":
    main()
