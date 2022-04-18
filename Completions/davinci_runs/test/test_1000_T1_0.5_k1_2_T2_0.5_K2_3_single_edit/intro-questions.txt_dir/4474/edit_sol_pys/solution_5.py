
def good(n):
    if n == 1:
        return n
    powers = []
    i = 1
    while 3 ** i <= n:
        powers.append(3 ** i)
        i += 1
    dp = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i] = n + 1
    for i in range(2, n + 1):
        for x in powers:
            if i > x and dp[i - x] != n + 1:
                dp[i] = min(dp[i], dp[i - x] + x)
    return dp[n] if dp[n] != n + 1 else -1
if __name__ == '__main__':
    n = int(input())
    print(good(n))
