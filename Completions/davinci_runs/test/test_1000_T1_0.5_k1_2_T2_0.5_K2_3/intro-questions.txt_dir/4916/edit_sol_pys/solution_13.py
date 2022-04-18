
import math
import itertools

def main():
    n, k = map(int, input().split())  # n = number of rows/columns, k = number of tiles
    tiles = [list(map(int, input().split())) for _ in range(n)]  # tile numbers
    # print(tiles)  # print the tiles

    # Check if there are enough tiles to place
    if k > n**2:  # if there are more tiles than squares
        print(-1)
        return

    # Check if there are enough tiles of each number
    tile_counts = [0]*(k+1)  # count the number of each tile
    for i in range(n):
        for j in range(n):
            tile_counts[tiles[i][j]] += 1
    for tile in range(1, k+1):
        if tile_counts[tile] == 0:  # if there are no tiles of that number
            print(-1)
            return

    # Find the best path
    best_path = -1
    for path in itertools.permutations(range(1, k+1)):  # try all possible paths
        # print(path)  # print the path
        path_length = 0  # length of the path
        start_tile = None  # start tile
        for tile in path:
            if start_tile == None:  # if there is no start tile
                # Find the first tile
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:  # if this is the tile
                            start_tile = (i, j)  # set it as the start tile
                            break
                    if start_tile != None:  # if there is a start tile
                        break
            else:  # if there is a start tile
                # Find the next tile
                next_tile = None
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:  # if this is the tile
                            next_tile = (i, j)  # set it as the next tile
                            break
                    if next_tile != None:  # if there is a next tile
                        break
                # Add the distance
                path_length += math.sqrt((next_tile[0] - start_tile[0])**2 + (next_tile[1] - start_tile[1])**2)
                # print(start_tile, next_tile, path_length)
                start_tile = next_tile  # set the next tile as the start tile for next time
        # print(path_length)
        if best_path == -1 or path_length < best_path:  # if this is the best path
            best_path = path_length
    print(best_path)

if __name__ == "__main__":
    main()
