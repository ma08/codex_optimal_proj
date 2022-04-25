from collections import deque

n, m = map(int, input().split())

a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))

b = [0] * n
for i in range(n):
    b[i] = list(map(int, input().split()))

d = deque()
d.append(a[0])

c = [[0] * m for _ in range(n)]

while d:
    x, y = d.popleft()
    if x == n - 1 and y == m - 1:
        break

    for dx, dy in (0, 1), (1, 0):
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and b[nx][ny] == 0:
            b[nx][ny] = 1
            d.append((nx, ny))

            c[nx][ny] = c[x][y] + a[nx][ny]

print(c[-1][-1])
