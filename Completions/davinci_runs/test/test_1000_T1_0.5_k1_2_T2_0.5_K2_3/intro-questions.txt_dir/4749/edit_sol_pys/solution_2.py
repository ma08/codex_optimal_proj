

n = int(input())

grid = []
for _ in range(n):
    grid.append(list(input()))

# Check for equal number of black and white squares in each row and column
num_black = sum([grid[i].count('B') for i in range(n)])
num_white = sum([grid[i].count('W') for i in range(n)])
if (num_black != num_white):
    print(0)
    exit()

for i in range(n):
    num_black = sum([grid[j][i] == 'B' for j in range(n)])
    num_white = sum([grid[j][i] == 'W' for j in range(n)])
    if (num_black != num_white):
        print(0)
        exit()

# Check for 3 consecutive squares of the same colour in any row or column
for i in range(n):
    if (grid[i][0] == grid[i][1] == grid[i][2]):
        print(0)
        exit()
    for j in range(n-2):
        if (grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j+2]):
            print(0)
            exit()
    if (grid[i][n-3] == grid[i][n-2] == grid[i][n-1]):
        print(0)
        exit()

for i in range(n):
    if (grid[0][i] == grid[1][i] == grid[2][i]):
        print(0)
        exit()
    for j in range(n-2):
        if (grid[j][i] == grid[j+1][i] and grid[j][i] == grid[j+2][i]):
            print(0)
            exit()
    if (grid[n-3][i] == grid[n-2][i] == grid[n-1][i]):
        print(0)
        exit()

print(1)
