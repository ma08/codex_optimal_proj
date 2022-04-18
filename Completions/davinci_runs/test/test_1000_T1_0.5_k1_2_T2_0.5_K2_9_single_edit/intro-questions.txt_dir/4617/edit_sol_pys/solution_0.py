
# -----Constants-----
YES = "YES"
NO = "NO"

# -----Functions-----
def is_same_grid(grid):
    return (
        grid[0][0] == grid[1][1]
        and grid[0][1] == grid[1][0]
        and grid[0][2] == grid[1][2]
    )


# -----Input and Output-----
grid = []
for i in range(2):
    grid.append(list(input()))

if is_same_grid(grid):
    print(YES)
else:
    print(NO)
