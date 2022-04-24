
def solve(s, t):
    # dp[i][j] = length of the longest common subsequence from first i chars of s and first j chars of t.
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)] # O(|s| * |t|)

    for i in range(1, len(s) + 1): # O(|s|)
        for j in range(1, len(t) + 1): # O(|t|)
            if s[i - 1] == t[j - 1]: # O(1)
                dp[i][j] = dp[i - 1][j - 1] + 1 # O(1)
            else: # O(1)
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # O(1)

    return len(s) - dp[-1][-1] # O(1)

s = input()
t = input()
print(solve(s, t)) # O(|s| + |t|)
