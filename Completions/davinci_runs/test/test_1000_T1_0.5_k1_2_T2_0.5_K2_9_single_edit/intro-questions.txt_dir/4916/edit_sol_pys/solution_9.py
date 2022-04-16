

import itertools

def main():
    n, k = map(int, input().split())  # n: number of rows, k: number of types of tiles
    tiles = [list(map(int, input().split())) for _ in range(n)]  # tiles[i][j]: type of tile in row i and column j

    # Check if there are enough tiles to play
    if k > n**2:
        print(-1)
        return

    # Check if there are enough tiles of each number
    tile_counts = [0]*(k+1)
    for i in range(n):
        for j in range(n):
            tile_counts[tiles[i][j]] += 1
    for tile in range(1, k+1):
        if tile_counts[tile] == 0:
            print(-1)
            return

    # Find the best path
    best_path = -1
    for path in itertools.permutations(range(1, k+1)):
        # print(path)
        path_length = 0
        start_tile = None
        for tile in path:
            if start_tile == None:
                # Find the first tile
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:
                            start_tile = (i, j)
                            break
                    if start_tile != None:
                        break
            else:
                # Find the next tile
                next_tile = None
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:
                            next_tile = (i, j)
                            break
                    if next_tile != None:
                        break
                # Add the distance
                path_length += abs(next_tile[0] - start_tile[0]) + abs(next_tile[1] - start_tile[1])
                # print(start_tile, next_tile, path_length)
                start_tile = next_tile
        # print(path_length)
        if best_path == -1 or path_length < best_path:
            best_path = path_length
    print(best_path)

if __name__ == "__main__":
    main()
