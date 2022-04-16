

import sys

class Node:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

def read_input():
    t, n, m = [int(x) for x in sys.stdin.readline().split()]
    start_x = -1
    start_y = -1
    grid = []
    for i in range(n):
        row = sys.stdin.readline().strip()
        if "S" in row:
            start_x = i
            start_y = row.index("S")
        grid.append(row)
    return t, n, m, start_x, start_y, grid

def is_valid(x, y, n, m):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= m:
        return False
    return True

def get_next(x, y, n, m, grid):
    nexts = []
    if is_valid(x-1, y, n, m) and grid[x-1][y] != '1':
        if grid[x-1][y] == 'U' or grid[x][y] == 'D':
            nexts.append(Node(x-1, y, 1))
        else:
            nexts.append(Node(x-1, y, 0))
    if is_valid(x+1, y, n, m) and grid[x+1][y] != '1':
        if grid[x+1][y] == 'D' or grid[x][y] == 'U':
            nexts.append(Node(x+1, y, 1))
        else:
            nexts.append(Node(x+1, y, 0))
    if is_valid(x, y-1, n, m) and grid[x][y-1] != '1':
        if grid[x][y-1] == 'L' or grid[x][y] == 'R':
            nexts.append(Node(x, y-1, 1))
        else:
            nexts.append(Node(x, y-1, 0))
    if is_valid(x, y+1, n, m) and grid[x][y+1] != '1':
        if grid[x][y+1] == 'R' or grid[x][y] == 'L':
            nexts.append(Node(x, y+1, 1))
        else:
            nexts.append(Node(x, y+1, 0))
    return nexts

def get_min_path(t, n, m, start_x, start_y, grid):
    q = []
    q.append(Node(start_x, start_y, 0))
    visited = [[False for j in range(m)] for i in range(n)]
    visited[start_x][start_y] = True
    while len(q) > 0:
        curr = q.pop(0)
        if curr.x == 0 or curr.x == n-1 or curr.y == 0 or curr.y == m-1:
            return curr.num
        nexts = get_next(curr.x, curr.y, n, m, grid)
        for next in nexts:
            if not visited[next.x][next.y] and next.num <= t:
                q.append(next)
                visited[next.x][next.y] = True
    return -1

def main():
    t, n, m, start_x, start_y, grid = read_input()
    path = get_min_path(t, n, m, start_x, start_y, grid)
    if path == -1:
        print("NOT POSSIBLE")
    else:
        print(path)

if __name__ == "__main__":
    main()
