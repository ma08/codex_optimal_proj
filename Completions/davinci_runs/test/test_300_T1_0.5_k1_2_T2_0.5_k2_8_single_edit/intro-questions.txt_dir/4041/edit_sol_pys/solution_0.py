from collections import defaultdict
from collections import deque


# Read input
n, m = map(int, input().split())
edges = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# Perform a BFS to determine if there is a cycle
visited = [False for _ in range(n+1)]
q = deque()
q.append(1)
visited[1] = True
while q:
    cur = q.popleft()
    for child in edges[cur]:
        if visited[child]:
            print('NO')
            exit()
        else:
            visited[child] = True
            q.append(child)

print('YES')
