import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)



def dfs(v, p, d):
    depth[v] = d
    for u in edges[v]:  # 隣接する頂点を探索
        if u == p:  # 親は探索しない
            continue  # 次の隣接する頂点に進む
        dfs(u, v, d + 1)  # 再帰的に探索


def bfs(s):
    q = deque([s])  # 先頭から要素を取り出す
    seen = [False] * n
    seen[s] = True
    while q:
        v = q.popleft()
        for u in edges[v]:
            if seen[u]:
                continue
            seen[u] = True
            q.append(u)


n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dfs(0, -1)
