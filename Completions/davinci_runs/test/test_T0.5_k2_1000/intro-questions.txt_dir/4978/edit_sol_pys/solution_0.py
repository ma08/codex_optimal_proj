N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

for row in range(N):
    for col in range(M):
        if grid[row][col] == "V":
            if row == 0:
                pass
            elif grid[row-1][col] == ".":
                grid[row-1][col] = "V"
            elif grid[row-1][col] == "#":
                if col > 0 and grid[row][col-1] == ".":
                    grid[row][col-1] = "V"
                if col < M-1 and grid[row][col+1] == ".":
                    grid[row][col+1] = "V"

for row in range(N):
    print("".join(grid[row]))
