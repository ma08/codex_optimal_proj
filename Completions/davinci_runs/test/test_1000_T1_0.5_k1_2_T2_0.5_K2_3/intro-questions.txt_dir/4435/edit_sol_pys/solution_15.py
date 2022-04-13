
import queue

n = int(input())
a = list(map(int, input().split()))

q = queue.Queue()

for i in range(n):
    if a[i] % 2 == 1:
        q.put((i, 0))

for i in range(n):
    if a[i] % 2 == 0:
        q.put((i, 0))

visited = [False] * n

while not q.empty():
    print("here")
    curr, dist = q.get()
    if visited[curr]:
        continue
    visited[curr] = True
    if curr - a[curr] >= 0:
        q.put((curr - a[curr], dist + 1))
    if curr + a[curr] < n:
        q.put((curr + a[curr], dist + 1))

for i in range(n):
    if visited[i]:
        print(dist)
    else:
        print(-1)
