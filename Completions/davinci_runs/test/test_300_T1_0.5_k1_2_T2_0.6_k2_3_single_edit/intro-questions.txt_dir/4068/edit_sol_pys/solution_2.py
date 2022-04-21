

import numpy as np


def main():
    n, m = map(int, input().split())
    broken_steps = [int(input()) for _ in range(m)]
    dp = np.zeros((n+1), dtype=np.int64)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        if i not in broken_steps:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    print(dp[n])


if __name__ == "__main__":
    main()
