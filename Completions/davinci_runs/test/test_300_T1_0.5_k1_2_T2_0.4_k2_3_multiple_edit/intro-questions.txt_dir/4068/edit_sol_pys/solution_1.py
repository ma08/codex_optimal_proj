

import numpy as np

def main():
    N, M = map(int, input().split())
    broken_stairs = [int(input()) - 1 for _ in range(M)]
    broken_stairs.sort()
    dp = np.zeros((N+1), dtype=np.int32)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        if i in broken_stairs:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[N])

if __name__ == "__main__":
    main()
