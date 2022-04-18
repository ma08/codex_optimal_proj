
# check row
def check_row(n, grid):
    for row in grid:
        # check color
        if row.count('B') != row.count('W'):
            print(0)
            exit()
        # check consecutive
        for i in range(n-2):
            if row[i] == row[i+1] == row[i+2]:
                print(0)
                exit()

# check column
def check_column(n, grid):
    for j in range(n):
        column = [grid[i][j] for i in range(n)]
        # check color
        if column.count('B') != column.count('W'):
            print(0)
            exit()
        # check consecutive
        for i in range(n-2):
            if column[i] == column[i+1] == column[i+2]:
                print(0)
                exit()

# main

n = int(input())
grid = [input() for _ in range(n)]

check_row(n, grid)
check_column(n, grid)

print(1)
