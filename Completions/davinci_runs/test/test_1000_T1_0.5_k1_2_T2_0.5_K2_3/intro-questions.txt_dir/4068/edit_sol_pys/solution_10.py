import numpy as np

def main():
    N, M = map(int, input().split())
    broken_steps = [int(input()) for _ in range(M)]
    dp = np.zeros((N+1), dtype=np.int64)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in broken_steps:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])

if __name__ == "__main__":
    main()
