

n = int(input())

grid = []
for _ in range(n):
    grid.append(input())

# Check for the same number of black and white squares
# in each row and column
row_count = []
col_count = []
for i in range(n):
    row_count.append(grid[i].count('B'))
    col_count.append(0)
    for j in range(n):
        col_count[i] += 1 if grid[j][i] == 'B' else 0

# Check for adjacent squares of the same color
for i in range(n):
    if 'BBB' in grid[i] or 'WWW' in grid[i]:
        print(0)
        exit()
    for j in range(n-2):
        if grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j+2]:
            print(0)
            exit()

# Check for the same number of black and white squares
# in each row and column
for i in range(n):
    if row_count[i] != n//2:
        print(0)
        exit()
    if col_count[i] != n//2:
        print(0)
        exit()

print(1)
