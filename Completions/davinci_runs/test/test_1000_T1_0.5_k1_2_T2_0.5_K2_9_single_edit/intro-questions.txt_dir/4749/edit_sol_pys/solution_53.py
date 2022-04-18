

n = int(input())
grid = []
for i in range(n):
    grid.append(input())

# check rows
for row in grid:
    count = 1
    for i in range(n-1):
        if row[i] == row[i+1] and row[i]!='.':
            count += 1
        else:
            count = 1
        if count == 2:
            print(0)
            exit()

# check columns
for i in range(n):
    count = 1
    for j in range(n-1):
        if grid[j][i] == grid[j+1][i] and grid[j][i]!='.':
            count += 1
        else:
            count = 1
        if count == 2:
            print(0)
            exit()

# if all conditions are satisfied
print(1)
