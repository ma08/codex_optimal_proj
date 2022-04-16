

import sys

h, w = map(int, sys.stdin.readline().split())

grid = []
for i in range(h):
    grid.append(list(sys.stdin.readline().strip()))

for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            count = 0
            count += (1 if i > 0 and j > 0 and grid[i-1][j-1] == '#' else 0) # top left
            count += (1 if i > 0 and grid[i-1][j] == '#' else 0) # top center
            count += (1 if i > 0 and j < w-1 and grid[i-1][j+1] == '#' else 0) # top right
            count += (1 if j > 0 and grid[i][j-1] == '#' else 0) # center left
            count += (1 if j < w-1 and grid[i][j+1] == '#' else 0) # center right
            count += (1 if i < h-1 and j > 0 and grid[i+1][j-1] == '#' else 0) # bottom left
            count += (1 if i < h-1 and grid[i+1][j] == '#' else 0) # bottom center
            count += (1 if i < h-1 and j < w-1 and grid[i+1][j+1] == '#' else 0) # bottom right
            grid[i][j] = str(count)

for i in range(h):
    print(''.join(grid[i]))
