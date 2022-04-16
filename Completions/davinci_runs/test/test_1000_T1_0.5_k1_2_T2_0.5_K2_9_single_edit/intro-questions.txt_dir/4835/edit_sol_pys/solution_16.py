
from collections import deque

def get_neighbors(grid, x, y):
    neighbors = []
    if x > 0 and grid[x-1][y] not in ['1', 'U', 'D', 'L', 'R']:
        neighbors.append((x-1, y))
    if x < len(grid) - 1 and grid[x+1][y] not in ['1', 'U', 'D', 'L', 'R']:
        neighbors.append((x+1, y))
    if y > 0 and grid[x][y-1] not in ['1', 'U', 'D', 'L', 'R']:
        neighbors.append((x, y-1))
    if y < len(grid[0]) - 1 and grid[x][y+1] not in ['1', 'U', 'D', 'L', 'R']:
        neighbors.append((x, y+1))
    return neighbors

def get_time(grid, t, x, y):
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
        return 0
    if grid[x][y] == 'S':
        return t
    if grid[x][y] == '.':
        return t + 1
    if grid[x][y] == 'U':
        return t + 1 if x > 0 and grid[x-1][y] != 'D' else t + 2
    if grid[x][y] == 'D':
        return t + 1 if x < len(grid) - 1 and grid[x+1][y] != 'U' else t + 2
    if grid[x][y] == 'L':
        return t + 1 if y > 0 and grid[x][y-1] != 'R' else t + 2
    if grid[x][y] == 'R':
        return t + 1 if y < len(grid[0]) - 1 and grid[x][y+1] != 'L' else t + 2

def bfs(grid, t, x, y):
    visited = set()
    q = deque()
    q.append((x, y))
    while len(q) > 0:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in get_neighbors(grid, node[0], node[1]):
                if get_time(grid, t, neighbor[0], neighbor[1]) <= t:
                    q.append(neighbor)
    return visited

def main():
    t, n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    x, y = None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                x, y = i, j
    visited = bfs(grid, t, x, y)
    if len(visited) == n * m:
        print('NOT POSSIBLE')
    else:
        print(len(visited))

if __name__ == '__main__':
    main()
