import sys
sys.setrecursionlimit(10**6)

n,h,l,r = map(int, input().split())
a = list(map(int, input().split()))

def dfs(i, t):
    if i == n:
        if l <= t%h <= r:
            return 1
        else:
            return 0
    return max(dfs(i+1, t+a[i]), dfs(i+1, t))

print(dfs(0, 0))
