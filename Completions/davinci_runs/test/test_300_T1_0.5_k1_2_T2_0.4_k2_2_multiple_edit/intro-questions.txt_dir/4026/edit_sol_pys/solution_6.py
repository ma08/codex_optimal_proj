
def check_square(tiles, grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                for tile in tiles:
                    if check_tile(tile, grid, i, j):
                        grid[i][j] = tile[0][0]
                        grid[i][j+1] = tile[0][1]
                        grid[i+1][j] = tile[1][0]
                        grid[i+1][j+1] = tile[1][1]
                        break
                else:
                    return False
    return True

def check_tile(tile, grid, i, j):
    if i+1 < len(grid) and j+1 < len(grid):
        if grid[i][j+1] == tile[0][0] and grid[i+1][j+1] == tile[1][0] and grid[i+1][j] == tile[0][1] and grid[i][j] == tile[1][1]:
            return True
        if grid[i+1][j] == tile[0][0] and grid[i+1][j+1] == tile[1][0] and grid[i][j+1] == tile[0][1] and grid[i][j] == tile[1][1]:
            return True
        if grid[i][j] == tile[0][0] and grid[i][j+1] == tile[1][0] and grid[i+1][j+1] == tile[0][1] and grid[i+1][j] == tile[1][1]:
            return True
        if grid[i][j] == tile[0][0] and grid[i+1][j] == tile[1][0] and grid[i][j+1] == tile[0][1] and grid[i+1][j+1] == tile[1][1]:
            return True
    return False

def main():
    cases = int(input())
    for case in range(cases):
        n, m = map(int, input().split())
        tiles = []
        for i in range(n):
            tiles.append([list(map(int, input().split())) for i in range(2)])
        grid = [[0 for i in range(m)] for j in range(m)]
        if check_square(tiles, grid):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
