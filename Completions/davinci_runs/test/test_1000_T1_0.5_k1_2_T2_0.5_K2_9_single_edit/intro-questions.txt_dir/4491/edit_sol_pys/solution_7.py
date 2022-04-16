
import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    A = [[int(x) for x in sys.stdin.readline().rstrip().split()] for _ in range(2)]
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = A[0][0]
    dp[1][0] = A[1][0]
    for i in range(1, N):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1]) + A[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + A[1][i]
    print(max(dp[0][N - 1], dp[1][N - 1]))

if __name__ == "__main__":
    main()
