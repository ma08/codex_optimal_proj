import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
a = list(map(int, input().split()))[::-1]

def dfs(i, sum):
    if i == n:
        return sum == k
    if dfs(i+1, sum):
        return True
    if dfs(i+1, sum + a[i]):
        return True
    return False

if dfs(0, 0):
    print('Yes')
else:
    print('No')
