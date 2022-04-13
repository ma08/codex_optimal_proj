n, k = map(int, input().split())
tiles = []
for i in range(n):
    tiles.append(list(map(int, input().split())))


def find_start(tiles, k):
    """
    Finds the starting tile (1)
    """
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == 1:
                return (i, j)
def find_end(tiles, k):
    """
    Finds the ending tile (k)
    """
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == k:
                return (i, j)
def find_next(tiles, current_tile, current_number, k):
    """
    Finds the next tile (current_number + 1)
    """
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == current_number + 1:
                if abs(current_tile[0] - i) + abs(current_tile[1] - j) == 1:
                    return (i, j)
def find_path(tiles, current_tile, current_number, k):
    """
    Finds the path from current_tile to the end
    """
    if current_number == k:
        return 0
    else:
        next_tile = find_next(tiles, current_tile, current_number, k)
        return 1 + find_path(tiles, next_tile, current_number + 1, k)
start_tile = find_start(tiles, k)
end_tile = find_end(tiles, k)
if abs(start_tile[0] - end_tile[0]) + abs(start_tile[1] - end_tile[1]) == 1:
    print(0)
else:
    path = find_path(tiles, start_tile, 1, k)
    if path > 0:
        print(path)
    else:
        print(-1)
