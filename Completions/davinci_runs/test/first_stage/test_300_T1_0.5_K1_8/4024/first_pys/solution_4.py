
import sys
sys.setrecursionlimit(1000000000)

def find_subsequence(s, t, i, j, n, m, dp):
    if i >= n or j >= m:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == t[j]:
        return dp[i][j] = 1 + find_subsequence(s, t, i+1, j+1, n, m, dp)
    else:
        return dp[i][j] = max(find_subsequence(s, t, i+1, j, n, m, dp), find_subsequence(s, t, i, j+1, n, m, dp))

def solve(s, k):
    n = len(s)
    if k > n:
        return -1
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = find_subsequence(s[i:j+1], s[j:], 0, 0, j-i+1, j-i+1, dp)
            max_len = max(max_len, dp[i][j])
    if max_len < k:
        return -1
    else:
        return n*(k-1) - (n-max_len)*(k-1)

n, k = map(int, input().split())
s = input()
print(solve(s, k))