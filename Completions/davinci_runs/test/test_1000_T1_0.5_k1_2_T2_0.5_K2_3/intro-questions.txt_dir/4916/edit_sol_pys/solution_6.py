

import itertools

def main():
    n, k = map(int, input().split())
    tiles = [list(map(int, input().split())) for _ in range(n)]
    # print(tiles)

    # Check if there are enough tiles to place
    if k > n*n:
        print(-1)
        return

    # Check if there are enough tiles of each number
    tile_counts = [0]*(k+1)
    for i in range(n):
        for j in range(n):
            tile_counts[tiles[i][j]] += 1
    for tile_count in tile_counts:
        if tile_count == 0:
            print(-1)
            return

    # Find the best path
    best_path = -1
    for path in itertools.permutations(range(1, k+1)):
        # print(path)
        path_length = 0
        start_tile_i = None
        start_tile_j = None
        for tile in path:
            if start_tile_i == None:
                # Find the first tile
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:
                            start_tile = (i, j)
                            break
                    if start_tile_i != None:
                        break
            else:
                # Find the next tile
                next_tile_i = None
                next_tile_j = None
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:
                            next_tile_i = i
                            next_tile_j = j
                            break
                    if next_tile_i != None:
                        break
                # Add the distance
                path_length += abs(next_tile_i - start_tile_i) + abs(next_tile_j - start_tile_j)
                # print(start_tile_i, start_tile_j, next_tile_i, next_tile_j, path_length)
                start_tile_i = next_tile_i
                start_tile_j = next_tile_j
        # print(path_length)
        if best_path == -1 or path_length < best_path:
            best_path = path_length
    print(best_path)

if __name__ == "__main__":
    main()
