
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

tree = [[] for _ in range(N)]
for _ in range(M):
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

def dfs(v, visited, parent):
    visited[v] = True
    for child in tree[v]: # vから行ける頂点
        if not visited[child]:
            dfs(child, visited, v)
        elif child != parent: # 親からも行ける頂点でなければ、それは別のループ
            print(0)
            sys.exit()

visited = [False for _ in range(N)]
dfs(0, visited, -1)

ans = 1
for i in range(1, N):
    ans *= len(tree[i])
    if ans > 10**9 + 7:
        ans %= 10**9 + 7

if not all(visited):
    print(0)
    sys.exit()

print(ans)
