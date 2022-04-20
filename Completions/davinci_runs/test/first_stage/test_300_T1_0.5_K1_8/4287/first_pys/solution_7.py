

import sys

def solve(a, n, m, l, r, x, p):
    # dp[i] = (min_fatigue, min_fatigue_with_umbrella)
    # dp[i][0] = min(dp[i-1][0] + p[i], dp[i-1][1])
    # dp[i][1] = min(dp[i-1][0] + p[i], dp[i-1][1] + p[i])
    dp = [[0, 0] for _ in range(m)]
    for i in range(m):
        if i == 0:
            dp[i][0] = sys.maxsize
            dp[i][1] = p[i]
        else:
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])
            dp[i][1] = min(dp[i-1][0] + p[i], dp[i-1][1] + p[i])
    # print(dp)
    min_fatigue = sys.maxsize
    for i in range(m):
        if l[i] <= 0 and 0 <= r[i]:
            min_fatigue = min(min_fatigue, dp[i][1])
        else:
            min_fatigue = min(min_fatigue, dp[i][0])
    return min_fatigue if min_fatigue != sys.maxsize else -1

if __name__ == '__main__':
    a, n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    x = []
    p = []
    for _ in range(m):
        x_i, p_i = map(int, input().split())
        x.append(x_i)
        p.append(p_i)
    print(solve(a, n, m, l, r, x, p))