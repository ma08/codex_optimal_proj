
import numpy as np

def main():
    N, M = map(int, input().split())
    broken_steps = [int(input()) for _ in range(M)]
    broken_steps.sort()
    dp = np.zeros(N+1, dtype=np.int64)
    dp[0] = 1
    for i in range(1, N):
        if i+1 not in broken_steps:
            dp[i+1] = (dp[i-1] + dp[i]) % 1000000007
    print(dp[N])

if __name__ == "__main__":
    main()
