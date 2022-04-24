

def solve(s):
    # dp[i] = min number of operations to make s[:i] palindrome
    dp = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0 and s[:i // 2] == s[i // 2:i][::-1]:
            dp[i] = min(dp[i], dp[i // 2])
        if i % 3 == 0 and s[:i // 3] == s[i // 3 * 2:i][::-1]:
            dp[i] = min(dp[i], dp[i // 3 * 2])
    return dp[-1]


print(solve(input()))
