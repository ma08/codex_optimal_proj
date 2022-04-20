

def is_star(grid, i, j, size):
    if grid[i][j] == '.':
        return False
    if i - size < 0 or i + size >= len(grid):
        return False
    if j - size < 0 or j + size >= len(grid[0]):
        return False
    for idx in range(i - size, i + size + 1):
        if grid[idx][j] == '.':
            return False
    for idx in range(j - size, j + size + 1):
        if grid[i][idx] == '.':
            return False
    return True

def draw_star(grid, i, j, size):
    for idx in range(i - size, i + size + 1):
        grid[idx][j] = '.'
    for idx in range(j - size, j + size + 1):
        grid[i][idx] = '.'

def is_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                return False
    return True

def compute_grid(grid):
    stars = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            size = 0
            while is_star(grid, i, j, size):
                draw_star(grid, i, j, size)
                stars.append((i, j, size + 1))
                size += 1
    if is_empty(grid):
        print(len(stars))
        for star in stars:
            print(star[0] + 1, star[1] + 1, star[2])
    else:
        print("-1")

def read_input():
    n, m = [int(x) for x in input().split(" ")]
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    return grid

if __name__ == "__main__":
    grid = read_input()
    compute_grid(grid)