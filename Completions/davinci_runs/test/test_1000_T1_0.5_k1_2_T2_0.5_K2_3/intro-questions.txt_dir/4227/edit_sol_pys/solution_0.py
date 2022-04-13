

from collections import deque
N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False] * N
    visited[start] = True
    while queue:
        v = queue.popleft()
        for child in graph[v]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True
    return all(visited)

visited = set()
bfs(0)

if len(visited) != N:
    print(0)
    sys.exit()

ans = 1
for i in range(N):
    if i == 0:
        continue
    if len(tree[i]) > 1:
        ans *= len(tree[i])

print(ans)
