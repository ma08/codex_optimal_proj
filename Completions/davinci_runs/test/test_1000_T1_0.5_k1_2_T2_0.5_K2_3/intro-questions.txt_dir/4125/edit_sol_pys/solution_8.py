import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = [0] * N

def dfs(i, m):
    if m == 0:
        return True
    if i >= N:
        return False
    res = dfs(i + 1, m) or dfs(i + 1, m - A[i])
    if res:
        ans[i] = 1
    return res

if dfs(0, M):
    print('Yes')
    for a in ans:
        print(a)
else:
    print('No')

