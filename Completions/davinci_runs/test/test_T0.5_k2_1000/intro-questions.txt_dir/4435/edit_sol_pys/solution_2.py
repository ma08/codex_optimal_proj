
# https://codeforces.com/contest/1325/problem/B
import queue

n = int(input())
a = list(map(int, input().split()))

q = queue.Queue()

for i in range(n):
    if a[i] % 2 == 0:
        q.put((i, 0))  # (index, distance)

for i in range(n):
    if a[i] % 2 == 1:
        q.put((i, 0))

visited = [False] * n

while not q.empty():
    curr, dist = q.get()
    if visited[curr]:
        continue
    visited[curr] = True
    if curr - a[curr] >= 0:  # if index is not out of bounds
        q.put((curr - a[curr], dist + 1))
    if curr + a[curr] < n:  # if index is not out of bounds
        q.put((curr + a[curr], dist + 1))

for i in range(n):
    if a[i] % 2 == 0:
        if visited[i]:
            print(dist)  # print distance
        else:
            print(-1)  # print -1 if not visited
    else:
        if visited[i]:
            print(dist)  # print distance
        else:
            print(-1)  # print -1 if not visited
