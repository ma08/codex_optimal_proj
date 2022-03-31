

import sys
import math
from collections import defaultdict

def main():
    N, M, X = map(int, sys.stdin.readline().split())
    A = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    C = [int(x) for x in sys.stdin.readline().split()]
    dp = defaultdict(lambda: 10**10)
    dp[0] = 0
    for i in range(N):
        for j in range(1 << M):
            dp[j | A[i][0]] = min(dp[j | A[i][0]], dp[j] + C[i])
    if dp[(1 << M) - 1] == 10**10:
        print(-1)
    else:
        print(dp[(1 << M) - 1])

if __name__ == '__main__':
    main()