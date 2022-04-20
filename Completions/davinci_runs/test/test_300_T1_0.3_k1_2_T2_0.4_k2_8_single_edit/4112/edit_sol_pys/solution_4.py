import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

if x < k:
    print(-1)
else:
    dp = [f_inf] * (x + 1)
    dp[0] = 0
    for _ in range(n):
        tmp = [f_inf] * (x + 1)
        for i in range(x + 1):
            if i - 1 >= 0:
                tmp[i] = min(tmp[i], dp[i - 1] + sum(a[i * k:(i + 1) * k]))
            tmp[i] = min(tmp[i], dp[i])
        dp = tmp
    print(dp[-1])
