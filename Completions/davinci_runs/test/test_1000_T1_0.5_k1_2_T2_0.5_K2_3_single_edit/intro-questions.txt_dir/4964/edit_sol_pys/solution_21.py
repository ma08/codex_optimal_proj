import sys
sys.setrecursionlimit(10**6)

# Solution
def solve():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    start = 0
    ans = [0] * N
    for i in range(N):
        if len(edges[i]) > len(edges[start]):
            start = i
    def dfs(v, p, d):
        ans[v] = d
        for u in edges[v]:
            if u != p:
                dfs(u, v, d+1)
    dfs(start, -1, 0)
    print(ans.index(max(ans)) + 1)

solve()
