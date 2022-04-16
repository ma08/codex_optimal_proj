
import itertools

def main():
    n, k = map(int, input().split())
    tiles = [list(map(int, input().split())) for _ in range(n)]

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
        path_length = 0
        start_tile = None
        for tile in path:
            if start_tile is None:
                # Find the first tile
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:
                            start_tile = (i, j)
                            break
                    if start_tile is not None:
                        break
            else:
                # Find the next tile
                next_tile = []
                for i in range(n):
                    for j in range(n):
                        if tiles[i][j] == tile:
                            next_tile.append((i, j))
                            break
                    if next_tile:
                        break
                if len(next_tile) > 1:
                    # Find the closest next tile
                    min_dist = n**2
                    closest_tile = None
                    for tile in next_tile:
                        dist = abs(tile[0] - start_tile[0]) + abs(tile[1] - start_tile[1])
                        if dist < min_dist:
                            min_dist = dist
                            closest_tile = tile
                    next_tile = closest_tile
                # Add the distance
                path_length += abs(next_tile[0] - start_tile[0]) + abs(next_tile[1] - start_tile[1])
                start_tile = next_tile
        if best_path == -1 or path_length < best_path:
            best_path = path_length
    print(best_path)

if __name__ == "__main__":
    main()
