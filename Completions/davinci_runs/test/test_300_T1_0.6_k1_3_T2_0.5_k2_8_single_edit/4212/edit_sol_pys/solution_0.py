

from collections import deque, defaultdict

n, m, k = map(int, input().split())

# the adjacency list
adj_list = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)

# the queue
queue = deque()
queue.append(1)

# the visited array
visited = [False for _ in range(n+1)]
visited[1] = True

# the distance array
dist = [-1 for _ in range(n+1)]
dist[1] = 0

# the number of nodes at each level
nodes_at_level = [0 for _ in range(n+1)]
nodes_at_level[0] = 1

while queue:
    u = queue.popleft()

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            queue.append(v)
            dist[v] = dist[u] + 1
            nodes_at_level[dist[v]] += 1

# the answer is the sum of the nodes at the first k levels
print(sum(nodes_at_level[:k]))
