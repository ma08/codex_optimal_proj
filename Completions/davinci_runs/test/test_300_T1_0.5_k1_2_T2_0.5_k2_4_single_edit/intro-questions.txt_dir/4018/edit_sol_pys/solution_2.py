


import sys

sys.setrecursionlimit(1000000)

def dfs(i, k):
    if i == n:
        return 0
    if (i, k) in dp:
        return dp[i, k]
    ans = 10**9
    if k & (1 << i):
        ans = min(ans, dfs(i + 1, k) + n - i)
    ans = min(ans, dfs(i + 1, k) + 1)
    if k & (1 << i):
        ans = min(ans, dfs(i + 1, k ^ (1 << i)) + n - i + 1)
    ans = min(ans, dfs(i + 1, k ^ (1 << i)) + 2)
    dp[i, k] = ans
    return ans
# -*- coding: utf-8 -*

def main():
    n, k = map(int, raw_input().split())
    s = raw_input()
    # print n, k, s
    global n
    global dp
    dp = {}
    print dfs(0, k)
        
if __name__ == '__main__':
    main()
