

def check_rows_for_symmetry(tile_grid):
    # check if rows are symmetric
    for i, row in enumerate(tile_grid): # for each row
        for j, value in enumerate(row): # for each value in the row
            if tile_grid[j][i] != value:
                return False
    return True

def check_for_symmetry(tile_grid):
    # check the rows for symmetry
    if check_rows_for_symmetry(tile_grid):
        # check the columns for symmetry
        col_grid = [[row[i] for row in tile_grid] for i in range(len(tile_grid))]
        if check_rows_for_symmetry(col_grid):
            return True
    return False

def get_tile_grid(tiles, m):
    # make grid from tiles
    tile_grid = []
    for i in range(m): # for each row
        row = []
        for j in range(m): # for each column
            row.append(tiles[i%2][j%2]) # get the tile
        tile_grid.append(row)
    return tile_grid

def solve(n, m, tiles_list):
    # check all combinations
    for tiles in tiles_list: # for each tile
        tile_grid = get_tile_grid(tiles, m)
        if check_for_symmetry(tile_grid):
            return True
    return False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tiles_list = []
    for i in range(n): # for each tile
        tile = []
        for j in range(2): # for each row
            tile.append(list(map(int, input().split()))) # get the row
        tiles_list.append(tile)
    if solve(n, m, tiles_list):
        print("YES")
    else:
        print("NO")
