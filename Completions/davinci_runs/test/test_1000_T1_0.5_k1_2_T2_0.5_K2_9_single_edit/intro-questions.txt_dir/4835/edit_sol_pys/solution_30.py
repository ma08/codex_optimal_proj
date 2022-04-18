

from collections import deque

def get_neighbors(grid, x, y):
    neighbors = []
    if x > 0 and grid[x-1][y] not in ['1', 'U', 'D', 'L', 'R'] and (x-1, y) not in visited:
        neighbors.append((x-1, y))
    if x < len(grid) - 1 and grid[x+1][y] not in ['1', 'U', 'D', 'L', 'R'] and (x+1, y) not in visited:
        neighbors.append((x+1, y))
    if y > 0 and grid[x][y-1] not in ['1', 'U', 'D', 'L', 'R'] and (x, y-1) not in visited:
        neighbors.append((x, y-1))
    if y < len(grid[0]) - 1 and grid[x][y+1] not in ['1', 'U', 'D', 'L', 'R'] and (x, y+1) not in visited:
        neighbors.append((x, y+1))
    return neighbors

def get_time(grid, t, x, y):
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
        return 0
    if grid[x][y] == 'S':
        return t
    if grid[x][y] == '0':
        return t + 1
    if grid[x][y] == 'U':
        return t + 1 if x > 0 and grid[x-1][y] != 'D' else t + 2
    if grid[x][y] == 'D':
        return t + 1 if x < len(grid) - 1 and grid[x+1][y] != 'U' else t + 2
    if grid[x][y] == 'L':
        return t + 1 if y > 0 and grid[x][y-1] != 'R' else t + 2
    if grid[x][y] == 'R':
        return t + 1 if y < len(grid[0]) - 1 and grid[x][y+1] != 'L' else t + 2

def bfs(grid, t, x, y, visited):
    visited = set()
    q = deque()
    q.append((x, y, 0))
    while len(q) > 0:
        node, t_curr = q.popleft()
        if node not in visited and t_curr <= t:
            visited.add(node, t_curr)
            for neighbor in get_neighbors(grid, node[0], node[1], visited):
                t_next = get_time(grid, t_curr, neighbor[0], neighbor[1])
                if t_next <= t:
                    q.append((neighbor, t_next))
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
    visited = bfs(grid, t, x, y, set())
    if len(visited) == n * m:
        print('NOT POSSIBLE')
    else:
        print(len(visited))

if __name__ == '__main__':
    main()
