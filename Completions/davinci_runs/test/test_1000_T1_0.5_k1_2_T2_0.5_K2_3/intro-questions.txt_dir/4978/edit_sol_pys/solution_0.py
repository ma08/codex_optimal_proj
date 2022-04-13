

n = int(input())
m = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))

while True:
    new_grid = [['.' for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                new_grid[i][j] = '.'
            elif grid[i][j] == '#':
                new_grid[i][j] = '#'
            elif grid[i][j] == 'V':
                if i == 0:
                    new_grid[i][j] = 'V'
                elif grid[i-1][j] == '.':
                    new_grid[i-1][j] = 'V'
                elif grid[i-1][j] == '#':
                    if j > 0:
                        new_grid[i][j-1] = 'V'
                    if j < m-1:
                        new_grid[i][j+1] = 'V'
                new_grid[i][j] = 'V'
    if grid == new_grid:
        break
    grid = new_grid


for row in grid:
    print(''.join(row))
