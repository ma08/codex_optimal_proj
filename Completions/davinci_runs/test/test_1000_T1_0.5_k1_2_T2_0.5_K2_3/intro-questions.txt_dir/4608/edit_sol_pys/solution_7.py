from collections import deque

N = int(input())
a = list(map(int, sys.stdin.read().split()))

g = [[] for _ in range(N)]
visited = [False] * N

while len(queue) > 0:
    num = queue.popleft()
    if num == 2:
        print(visited[num]-1)
        sys.exit()
    if not visited[a[num-1]-1]:
        visited[a[num-1]-1] = visited[num] + 1
        queue.append(a[num-1])

print(-1)
