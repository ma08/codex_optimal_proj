
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
    curr, dis = que.get()
    if visited[curr]:
        continue
    visited[curr] = True
    if curr - a[curr] >= 0:
        que.put((curr - a[curr], dis + 1))
    if curr + a[curr] < n:
        que.put((curr + a[curr], dis + 1))

for i in range(n):
    if a[i] % 2 == 0:
        if visited[i]:
            print(dis)
        else:
            print(-1)
    else:
        if visited[i]:
            print(dis)
        else:
            print(-1)
