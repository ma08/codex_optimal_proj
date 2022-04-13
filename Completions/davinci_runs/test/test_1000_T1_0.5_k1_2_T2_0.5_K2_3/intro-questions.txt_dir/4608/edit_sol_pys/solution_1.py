
import sys


from collections import deque

N = int(input())
a = list(map(int, sys.stdin.read().split()))

visited = [0] * N
visited[0] = 1
queue = deque([0])

while len(queue) > 0:
    num = queue.popleft()
    if num == 2:
        print(visited[num]-1)
        sys.exit()
    if not visited[a[num-1]-1]:
        visited[a[num-1]-1] = visited[num] + 1
        queue.append(a[num-1])

print(-1)
