

n = int(input())
grid = []
for i in range(n):
    grid.append(input())

# check columns
for row in grid:
    count = 0
    for i in range(n-1):
        if row[i] == row[i+1]:
            count += 1
        else:
            count = 0
        if count == 2:
            print(0)
            exit()

# check rows
for i in range(n):
    for j in range(n-2):
        if grid[j][i] == grid[j+1][i]:
            if grid[j+1][i] == grid[j+2][i]:
                print(0)
                exit()

# if all conditions are satisfied
print(1)
