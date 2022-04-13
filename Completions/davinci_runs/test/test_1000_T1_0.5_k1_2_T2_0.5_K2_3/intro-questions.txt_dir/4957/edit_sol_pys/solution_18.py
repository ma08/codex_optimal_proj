
from collections import deque

def main():
    n, m, k = [int(x) for x in input().split()]
    grid = [[int(x) for x in input().split()] for _ in range(n)]
    visited = [[False] * m for _ in range(n)] # visited[i][j] = True iff (i, j) has been visited
    dq = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                visited[i][j] = True
                dq.append((i, j, 1))
                break
        if len(dq) > 0:
            break
    while len(dq) > 0:
        row, col, cnt = dq.popleft()
        for x, y in ((row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)):
            if (0 <= x < n and 0 <= y < m and grid[x][y] == 1 and not visited[x][y]):
                dq.append((x, y, cnt + 1))
                visited[x][y] = True
                if cnt >= k:
                    grid[x][y] = 0
    print(sum([sum(row) for row in grid]))

if __name__ == '__main__':
    main()
