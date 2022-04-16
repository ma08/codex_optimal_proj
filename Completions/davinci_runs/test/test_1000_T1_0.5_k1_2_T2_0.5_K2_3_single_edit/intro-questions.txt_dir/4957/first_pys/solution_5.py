

from collections import deque

def main():
    n, m = [int(x) for x in input().split()]
    grid = [input() for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dq = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                visited[i][j] = True
                dq.append((i, j))
                break
        if len(dq) > 0:
            break
    while len(dq) > 0:
        row, col = dq.popleft()
        for x, y in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
            if (0 <= x < n and 0 <= y < m and grid[x][y] == '.' and not visited[x][y]):
                dq.append((x, y))
                visited[x][y] = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                grid[i][j] = 'E'
    for i in range(n):
        print(grid[i])

if __name__ == '__main__':
    main()