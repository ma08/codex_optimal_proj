from collections import deque
import sys


def main():
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(input()))

    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            print("Yes")
            sys.exit(0)
        if x + 1 < n and not visited[x + 1][y] and maze[x + 1][y] == '.':
            visited[x + 1][y] = True
            q.append((x + 1, y))
        if y + 1 < m and not visited[x][y + 1] and maze[x][y + 1] == '.':
            visited[x][y + 1] = True
            q.append((x, y + 1))
        if x - 1 >= 0 and not visited[x - 1][y] and maze[x - 1][y] == '.':
            visited[x - 1][y] = True
            q.append((x - 1, y))
        if y - 1 >= 0 and not visited[x][y - 1] and maze[x][y - 1] == '.':
            visited[x][y - 1] = True
            q.append((x, y - 1))

    print("No")


if __name__ == '__main__':
    main()
