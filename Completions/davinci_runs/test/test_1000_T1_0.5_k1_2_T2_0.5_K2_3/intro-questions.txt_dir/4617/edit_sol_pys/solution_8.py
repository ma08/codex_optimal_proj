

# -----CONSTANTS-----
YES = 'YES'
NO = 'NO'

# -----FUNCTIONS-----
def is_same_grid(grid):
    if grid[0][0] == grid[1][1] and grid[0][1] == grid[1][0] and grid[0][2] == grid[1][2]:
        return True
    else:
        return False

# -----INPUT AND OUTPUT-----
grid = []
for i in range(2):
    grid.append(list(input()))

if is_same_grid(grid):
    print(YES)
else:
    print(NO)
