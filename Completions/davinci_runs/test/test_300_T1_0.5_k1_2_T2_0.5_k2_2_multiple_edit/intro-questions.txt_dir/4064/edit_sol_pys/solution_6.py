import sys
sys.setrecursionlimit(10**6)

n,h,l,r = map(int, input().split()) # n,h,l,rの入力
a = list(map(int, input().split())) # aの入力

def dfs(i,t):
    if i >= n:
        return 0
    t += a[i]
    t = t % h
    if l <= t <= r:
        return max(dfs(i+1,t)+1,dfs(i+1,t-1)+1)
    else:
        return max(dfs(i+1,t),dfs(i+1,t-1))

print(dfs(0,0))
