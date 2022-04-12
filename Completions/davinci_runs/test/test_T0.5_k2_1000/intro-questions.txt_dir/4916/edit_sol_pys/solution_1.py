n, k = map(int, input().split())

tiles = []
for i in range(n):
    tiles.append(list(map(int, input().split())))

print(tiles)


def find_start(tiles):
    """
    Finds the starting tile (1)
    """
    for i in range(n):
        for j in range(n):
            if tiles[i][j] == 1:
                return (i, j)


def find_end(tiles, n, k):
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
    if current_tile[0] > 0 and tiles[current_tile[0] - 1][current_tile[1]] == current_number + 1:
        return (current_tile[0] - 1, current_tile[1])
    elif current_tile[0] < n - 1 and tiles[current_tile[0] + 1][current_tile[1]] == current_number + 1:
        return (current_tile[0] + 1, current_tile[1])
    elif current_tile[1] > 0 and tiles[current_tile[0]][current_tile[1] - 1] == current_number + 1:
        return (current_tile[0], current_tile[1] - 1)
    elif current_tile[1] < n - 1 and tiles[current_tile[0]][current_tile[1] + 1] == current_number + 1:
        return (current_tile[0], current_tile[1] + 1)
    else:
        return False


def find_path(tiles, current_tile, current_number, k):
    """
    Finds the path from current_tile to the end
    """
    if current_number == k:
        return 0
    else:
        next_tile = find_next(tiles, current_tile, current_number, k)
        if next_tile:
            return 1 + find_path(tiles, next_tile, current_number + 1, k)
        else:
            return -1


start_tile = find_start(tiles)
end_tile = find_end(tiles, n, k)

if start_tile and end_tile:
    if abs(start_tile[0] - end_tile[0]) + abs(start_tile[1] - end_tile[1]) == 1:
        print(0)
    else:
        path = find_path(tiles, start_tile, 1, k)
        if path > 0:
            print(path)
        else:
            print(-1)
else:
    print(-1)
