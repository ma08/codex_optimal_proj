import sys
sys.setrecursionlimit(10**6)

n = int(input())
s = list(map(int, input().split()))

def dfs(i, visited):
    global n
    global s
    if visited[i]:
        return 0
    visited[i] = True
    next_i = s[i] - 1
    return dfs(next_i, visited) + 1

ans = 0
for i in range(n):
    visited = [False] * n
    res = dfs(i, visited)
    ans = max(ans, res)

print(ans)
