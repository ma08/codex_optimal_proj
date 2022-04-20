

import sys
import math
input = sys.stdin.readline

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    if x < k or x > n or sum(a) < x:
        print(-1)
        return
    if k == 1:
        print(sum(a))
        return
    dp = [[0 for _ in range(x+1)] for _ in range(k)]
    for i in range(n):
        for j in range(1, k):
            dp[j][1] = max(dp[j][1], dp[j-1][1]+a[i])
        for j in range(2, x+1):
            dp[1][j] = max(dp[1][j], dp[0][j-1]+a[i])
        for j in range(2, k):
            for p in range(2, x+1):
                dp[j][p] = max(dp[j][p], dp[j-1][p-1]+a[i])
    print(dp[k-1][x])

if __name__ == '__main__':
    main()