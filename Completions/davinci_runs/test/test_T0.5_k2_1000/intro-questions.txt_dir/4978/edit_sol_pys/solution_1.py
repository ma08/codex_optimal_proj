
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

for row in range(n):
    for col in range(m):
        if grid[row][col] == "V":
            if row == 0:
                pass
            elif grid[row-1][col] == ".":
                grid[row-1][col] = "V"
            elif grid[row-1][col] == "#":
                if col > 0 and grid[row][col-1] == ".":
                    grid[row][col-1] = "V"
                if col < m-1 and grid[row][col+1] == ".":
                    grid[row][col+1] = "V"

for row in range(n):
    print("".join(grid[row]))
