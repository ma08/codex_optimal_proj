
import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [int(x) for x in sys.stdin.readline().rstrip().split()]
    B = [int(x) for x in sys.stdin.readline().rstrip().split()]
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = A[0]
    dp[0][1] = B[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + A[i]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + B[i]
    print(max(dp[N - 1][0], dp[N - 1][1]))

if __name__ == "__main__":
    main()
