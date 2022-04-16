
import sys

def main():
    N = int(sys.stdin.readline().strip())
    A = [int(x) for x in sys.stdin.readline().strip().split()]
    B = [int(x) for x in sys.stdin.readline().strip().split()]
    C = [int(x) for x in sys.stdin.readline().strip().split()]
    dp = [[0] * 3 for _ in range(N)]
    dp[0][0] = A[0]
    dp[0][1] = B[0]
    dp[0][2] = C[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + A[i]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + B[i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + C[i]
    print(max(dp[N-1]))

if __name__ == "__main__":
    main()
