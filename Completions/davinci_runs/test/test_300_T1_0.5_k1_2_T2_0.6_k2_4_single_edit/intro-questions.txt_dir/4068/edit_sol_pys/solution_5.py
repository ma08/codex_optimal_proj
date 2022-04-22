

import numpy as np

def main():
    N, M = map(int, input().split()) #N:全体の段数 M:壊れている段数
    broken_steps = [int(input()) for _ in range(M)]
    dp = np.zeros((N+1), dtype=np.int64)
    dp[0] = 1 #0段目には着地できる
    dp[1] = 1 #1段目には着地できる
    for i in range(2, N+1):
        if i in broken_steps:
            dp[i] = 0
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007 #着地できるパターンの数は前の段の着地パターンとその前の段の着地パターンの和
    print(dp[N])

if __name__ == "__main__":
    main()
