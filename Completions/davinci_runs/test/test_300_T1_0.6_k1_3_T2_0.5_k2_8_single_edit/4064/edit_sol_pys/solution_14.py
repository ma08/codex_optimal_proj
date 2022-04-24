

def solve_dp(n, h, l, r, a):
    dp = [0] * h
    dp[a[0]] = 1
    for i in range(n):
        nxt = [0] * h
        for j in range(h):
            if dp[j] == 0:
                continue 
            nxt[(j + a[i + 1]) % h] = max(nxt[(j + a[i + 1]) % h], dp[j] + (l <= (j + a[i + 1]) % h <= r))
            nxt[(j + a[i + 1] - 1) % h] = max(nxt[(j + a[i + 1] - 1) % h], dp[j] + (l <= (j + a[i + 1] - 1) % h <= r))
        dp = nxt
    return max(dp)


n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(solve_dp(n, h, l, r, a))
