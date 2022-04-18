import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = 0
def dfs(v, p):
    global ans
    cnt = 0
    for v2 in g[v]:
        if v2 == p:
            continue
        cnt += dfs(v2, v)
    if cnt % 2 == 0:
        ans += 1
        return 0
    else:
        return 1

dfs(0, -1)
print(ans)
