

from collections import Counter

def solve(a):
    c = Counter(a)
    vals = sorted(c.values())
    dp = [1]*len(vals)
    dp[0] = vals[0] + 1
    for i in range(1, len(vals)):
        dp[i] = (dp[i-1] * (vals[i] + 1)) % 998244353
    return dp[-1]

n = int(input())
a = list(map(int, input().split()))
print(solve(a))