

import queue as q

n = int(input())
a = list(map(int, input().split()))

que = q.Queue()

for i in range(n):
    if a[i] % 2 == 0:
        que.put((i, 0))

for i in range(n):
    if a[i] % 2 == 1:
        que.put((i, 0))

visited = [False] * n

while not que.empty():
    curr, dist = que.get()
    if visited[curr]:
        continue
    visited[curr] = True
    if curr - a[curr] >= 0:
        que.put((curr - a[curr], dist + 1))
    if curr + a[curr] < n:
        que.put((curr + a[curr], dist + 1))

for i in range(n):
    if a[i] % 2 == 1:
        if visited[i]:
            print(dist)
        else:
            print(-1)
    else:
        if visited[i]:
            print(dist)
        else:
            print(-1)


