
import numpy as np

def main():
    n, m = map(int, input().split())
    broken_steps = [0] * (n + 1)
    for _ in range(m):
        broken_steps[int(input())] = 1
    dp = np.zeros((n + 1), dtype=np.int64)
    dp[1] = 1 if broken_steps[1] == 0 else 0
    for i in range(2, n + 1):
        if broken_steps[i] == 1:
            dp[i] = 0
        else: dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    print(dp[n])

if __name__ == "__main__":
    main()
