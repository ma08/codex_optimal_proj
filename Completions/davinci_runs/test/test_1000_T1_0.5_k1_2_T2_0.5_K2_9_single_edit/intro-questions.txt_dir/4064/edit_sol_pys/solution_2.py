import sys
sys.setrecursionlimit(10**6)

n,h,l,r = map(int, input().split())
a = list(map(int, input().split()))

def dfs(i, t):
    if i == n:
        return 0
    t += a[i]
    t %= h
    if l <= t <= r:
        return dfs(i+1, t) + 1
    else:
        return dfs(i+1, t)

print(max(dfs(1, a[0]), dfs(1, a[0]-1)))
