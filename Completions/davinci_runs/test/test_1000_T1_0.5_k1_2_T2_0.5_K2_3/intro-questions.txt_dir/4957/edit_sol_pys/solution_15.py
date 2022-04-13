

from collections import deque

def main():
    n, m = [int(x) for x in input().split()]
    grid = [input() for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dq = deque()
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                x, y = i, j
                break;
    visited[x][y] = True
    dq.append((x, y))
    while len(dq) > 0:
        row, col = dq.popleft()
        for x, y in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
            if (0 <= x < n and 0 <= y < m and grid[x][y] == '.' and not visited[x][y]):
                dq.append((x, y))
                visited[x][y] = True
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '.':
                grid[row][col] = 'E'
    for i in range(n):
        print(grid[i])

if __name__ == '__main__':
    main()
