


def check_rows(grid):
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


def check_columns(grid):
    for i in range(n):
        count = 0
        for j in range(n-1):
            if grid[j][i] == grid[j+1][i]:
                count += 1
            else:
                count = 0
            if count == 2:
                print(0)
                exit()


n = int(input())
grid = []
for i in range(n):
    grid.append(input())

check_rows(grid)
check_columns(grid)

# if all conditions are satisfied
print(1)
