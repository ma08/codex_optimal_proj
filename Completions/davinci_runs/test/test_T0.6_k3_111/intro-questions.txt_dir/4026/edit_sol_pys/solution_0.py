

def check_rows_for_symmetry(rows):
    # check if rows are symmetric (m x m)
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            if rows[j][i] != value:
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
    # make grid
    tile_grid = []
    for i in range(m):
        row = []
        for j in range(m):
            row.append(tiles[i%2][j%2])
        tile_grid.append(row)
    return tile_grid

def solve(n, m, tiles_list):
    # check all combinations
    for tiles in tiles_list:
        tile_grid = get_tile_grid(tiles, m)
        if check_for_symmetry(tile_grid):
            return True
    return False

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tiles_list = []
    for i in range(n):
        tile = []
        for j in range(2):
            tile.append(list(map(int, input().split())))
        tiles_list.append(tile)
    if solve(n, m, tiles_list):
        print("YES")
    else:
        print("NO")
