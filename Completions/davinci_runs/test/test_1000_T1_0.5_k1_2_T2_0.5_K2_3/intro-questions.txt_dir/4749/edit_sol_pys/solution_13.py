

n = int(input())
grid = [input() for _ in range(n)]

# check rows
for row in grid:
    # check colors
    if row.count('B') != row.count('W'):
        print(0)
        exit()

# check columns
for j in range(n):
    column = [grid[i][j] for i in range(n)]
    # check colors
    if column.count('B') != column.count('W'):
        print(0)
        exit()

print(1)
