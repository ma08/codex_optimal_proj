import sys

def main():
    N = int(sys.stdin.readline())
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % 1000000007
        dp[i][1] = dp[i-1][0]
    print((dp[N][0] + dp[N][1]) % 1000000007)

if __name__ == '__main__':
    main()
