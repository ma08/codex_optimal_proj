
# read the input data
n = int(input())
grid = [list(input()) for i in range(n)]

# check the first condition (the number of black and white cells must be equal)
black_white_count = 0
for i in range(n):
    black_white_count += grid[i].count('B') - grid[i].count('W')
if black_white_count != 0:
    print(0)
    exit()

# check the second condition (the number of black and white cells in each row and column must be equal)
black_white_count = 0
for i in range(n):
    black_white_count += [row[i] for row in grid].count('B') - [row[i] for row in grid].count('W')
if black_white_count != 0:
    print(0)
    exit()

# check the third condition (there must be no 3 consecutive cells of the same color in a row or column)
for i in range(n):
    for j in range(n-2):
        if grid[i][j] == grid[i][j+1] == grid[i][j+2] or [row[i] for row in grid][j] == [row[i] for row in grid][j+1] == [row[i] for row in grid][j+2]:
            print(0)
            exit()

# if the grid is correct, print 1
print(1)
