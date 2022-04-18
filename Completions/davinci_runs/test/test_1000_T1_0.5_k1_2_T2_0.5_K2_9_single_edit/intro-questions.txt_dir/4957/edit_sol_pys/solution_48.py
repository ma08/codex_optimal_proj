
from collections import deque

def main():
    n = int(input())
    for _ in range(n):
        m, n = [int(x) for x in input().split()]
        grid = [input() for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '.':
                    visited[i][j] = True
                    dq.append((i, j))
                    break
            if len(dq) > 0:
                break
        while len(dq) > 0:
            row, col = dq.popleft()
            for x, y in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
                if (0 <= x < m and 0 <= y < n and grid[x][y] == '.' and not visited[x][y]):
                    dq.append((x, y))
                    visited[x][y] = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '.':
                    grid[i][j] = 'E'
        for i in range(m):
            print(grid[i])

if __name__ == '__main__':
    main()
