

from collections import defaultdict
from queue import Queue

n, m, D = map(int, input().split())

adj_list = defaultdict(list)
for _ in range(m):
    v, u = map(int, input().split())
    adj_list[v].append(u)
    adj_list[u].append(v)

visited = set()

def bfs(start):
    q = Queue()
    q.put(start)
    visited.add(start)
    while q.qsize():
        curr = q.get()
        for nbr in adj_list[curr]:
            if nbr not in visited:
                visited.add(nbr)
                q.put(nbr)

bfs(1)

if len(visited) != n:
    print('NO')
else:
    if D == 0:
        print('YES')
    else:
        for nbr in adj_list[1]:
            if nbr in visited:
                visited.remove(nbr)
        if len(visited) == D:
            print('YES')
            for v in visited:
                print(1, v)
        else:
            print('NO')