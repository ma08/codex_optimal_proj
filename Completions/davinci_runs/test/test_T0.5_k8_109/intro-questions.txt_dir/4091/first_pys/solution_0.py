

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [0 for _ in range(n+1)]
    for i in range(n):
        dp[i+1] = max(dp[i], a[i])
    dp2 = [0 for _ in range(n+1)]
    for i in range(n):
        dp2[i+1] = max(dp2[i], a[n-1-i])
    ans = 0
    for i in range(k):
        ans += dp[n-i]
    for i in range(k):
        ans += dp2[n-i]
    print(ans)
    t = [1]*k
    t[0] = n-k+1
    print(" ".join(map(str, t)))

main()