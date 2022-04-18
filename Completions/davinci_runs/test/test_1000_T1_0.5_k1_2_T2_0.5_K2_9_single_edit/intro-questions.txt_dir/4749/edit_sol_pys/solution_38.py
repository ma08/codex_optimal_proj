import sys

def is_valid(grid):
    n = len(grid)
    for i in range(n):
        if grid[i].count('B') != n // 2 or grid[i].count('B') != grid[i].count('W'):
            return False

    # Check columns
    for j in range(n):
        countB = 0
        countW = 0
        for i in range(n):
            if grid[i][j] == 'B':
                countB += 1
            elif grid[i][j] == 'W':
                countW += 1
        if countB != n // 2 or countB != countW:
            return False

    # Check rows for consecutive squares
    for i in range(n):
        for j in range(n-2):
            if grid[i][j] == grid[i][j+1] and grid[i][j+1] == grid[i][j+2]:
                return False

    # Check columns for consecutive squares
    for j in range(n):
        for i in range(n-2):
            if grid[i][j] == grid[i+1][j] and grid[i+1][j] == grid[i+2][j]:
                return False

    return True

def solve(grid, i, j):
    if i == n:
        return is_valid(grid)

    if j == n:
        return solve(grid, i+1, 0)

    if grid[i][j] == '-':
        grid[i] = grid[i][:j] + 'B' + grid[i][j+1:]
        if solve(grid, i, j+1):
            return True
        grid[i] = grid[i][:j] + 'W' + grid[i][j+1:]
        if solve(grid, i, j+1):
            return True
        grid[i] = grid[i][:j] + '-' + grid[i][j+1:]
        return False

    return solve(grid, i, j+1)


n = int(input())

grid = []
for i in range(n):
    grid.append(input())

print(1 if solve(grid, 0, 0) else 0)
