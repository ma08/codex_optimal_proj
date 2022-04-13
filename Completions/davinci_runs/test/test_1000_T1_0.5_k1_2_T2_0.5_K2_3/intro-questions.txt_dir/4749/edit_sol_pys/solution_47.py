

n = int(input())
n2 = n * n

grid = []
for i in range(n):
    grid.append(input())

# Check rows
for i in range(n):
    if grid[i].count('B') != n // 2 or grid[i].count('B') != grid[i].count('W') or grid[i].count('B') != grid[i].count('W'):
        print(0)
        exit()

# Check columns
for j in range(n):
    countB = 0
    countW = 0
    for i in range(n):
        if grid[i][j] == 'B':
            countB += 1
        elif grid[i][j] == 'W':
            countW += 1
    if countB != n // 2 or countB != countW or countB != countW:
        print(0)
        exit()

# Check rows for consecutive squares.
for i in range(n):
    for j in range(n-2):
        if grid[i][j] == grid[i][j+1] and grid[i][j+1] == grid[i][j+2]:
            print(0)
            exit()

# Check columns for consecutive squares.
for j in range(n):
    for i in range(n-2):
        if grid[i][j] == grid[i+1][j] and grid[i+1][j] == grid[i+2][j]:
            print(0)
            exit()

print(1)
