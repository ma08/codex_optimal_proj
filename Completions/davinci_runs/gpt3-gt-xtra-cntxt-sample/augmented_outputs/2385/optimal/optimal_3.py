from sys import stdin
from queue import PriorityQueue
from collections import defaultdict

class Node:
    def __init__(self, x, y, color, direction):
        self.x = x
        self.y = y
        self.color = color
        self.direction = direction

def next_direction(d):
    if d == 'U':
        return 'R'
    elif d == 'R':
        return 'D'
    elif d == 'D':
        return 'L'
    elif d == 'L':
        return 'U'

def is_valid_move(x, y, n, m):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    return False

def next_move(x, y, d):
    if d == 'U':
        return (x-1, y)
    elif d == 'R':
        return (x, y+1)
    elif d == 'D':
        return (x+1, y)
    elif d == 'L':
        return (x, y-1)

def get_next_move(x, y, n, m, d, grid):
    if d == 'U':
        if is_valid_move(x, y, n, m) and grid[x][y].direction != 'D':
            return (x-1, y)
    elif d == 'R':
        if is_valid_move(x, y, n, m) and grid[x][y].direction != 'L':
            return (x, y+1)
    elif d == 'D':
        if is_valid_move(x, y, n, m) and grid[x][y].direction != 'U':
            return (x+1, y)
    elif d == 'L':
        if is_valid_move(x, y, n, m) and grid[x][y].direction != 'R':
            return (x, y-1)
    return None

def get_cycle(x, y, n, m, d, grid):
    cycle = []
    while True:
        cycle.append((x, y))
        next_move_ = get_next_move(x, y, n, m, d, grid)
        if next_move_ == None:
            break
        x, y = next_move_
        d = next_direction(d)
    return cycle

def get_cycles(n, m, grid):
    cycles = []
    for i in range(n):
        for j in range(m):
            cycle = get_cycle(i, j, n, m, grid[i][j].direction, grid)
            if len(cycle) > 0:
                cycles.append(cycle)
    return cycles

def get_robot_placements(n, m, grid):
    cycles = get_cycles(n, m, grid)
    placements = []
    for cycle in cycles:
        if len(cycle) == 2:
            placements.append(cycle)
    return placements

def get_black_cells_before_movement(placement, n, m, grid):
    x, y = placement[0]
    return grid[x][y].color

def get_max_black_cells_before_movement(n, m, grid):
    placements = get_robot_placements(n, m, grid)
    black_cells = 0
    for placement in placements:
        black_cells += int(get_black_cells_before_movement(placement, n, m, grid))
    return black_cells

def get_max_robots(n, m, grid):
    placements = get_robot_placements(n, m, grid)
    return len(placements)

def solve(n, m, grid):
    return get_max_robots(n, m, grid), get_max_black_cells_before_movement(n, m, grid)

def get_input():
    t = int(stdin.readline())
    for _ in range(t):
        n, m = [int(x) for x in stdin.readline().split()]
        grid = []
        for i in range(n):
            color_row = stdin.readline().strip()
            direction_row = stdin.readline().strip()
            grid_row = []
            for j in range(m):
                grid_row.append(Node(i, j, color_row[j], direction_row[j]))
            grid.append(grid_row)
        yield (n, m, grid)

def main():
    for n, m, grid in get_input():
        print("{} {}".format(*solve(n, m, grid)))

if __name__ == '__main__':
    main()