

def hopscotch(n, k, tiles):
    """
    Returns the minimum distance to complete a game of hopscotch, or -1 if the game is not possible.

    :param n: The size of the square board.
    :param k: The number of tiles.
    :param tiles: The tiles on the board.
    :return: The minimum distance to complete a game of hopscotch, or -1 if the game is not possible.
    """

    # Check if game is possible
    if not possible(n, k, tiles):
        return -1

    # Create a dictionary to store the minimum distance to each tile
    min_distance = {}

    # Create a list to store the tiles to visit in order
    tiles_to_visit = []

    # Loop through the tiles
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            curr_tile = tiles[i][j]

            # If the current tile is the first tile
            if curr_tile == 1:
                min_distance[curr_tile] = 0
                tiles_to_visit.append(curr_tile)

            # If the current tile is the last tile
            elif curr_tile == k:
                tiles_to_visit.append(curr_tile)

            # If the current tile is not the first or last tile
            else:
                tiles_to_visit.append(curr_tile)

    # Loop through the tiles in order
    for tile in tiles_to_visit:
        # Loop through the tiles
        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                curr_tile = tiles[i][j]

                # If the current tile is the tile to visit
                if curr_tile == tile:
                    # Loop through the tiles
                    for i2 in range(len(tiles)):
                        for j2 in range(len(tiles[i2])):
                            curr_tile2 = tiles[i2][j2]

                            # If the current tile is the previous tile
                            if curr_tile2 == tile - 1:
                                # Update the minimum distance to the current tile
                                min_distance[tile] = min(min_distance[tile - 1] + abs(i - i2) + abs(j - j2), min_distance[tile])

    # Return the minimum distance to the last tile
    return min_distance[k]


def possible(n, k, tiles):
    """
    Returns whether or not a game of hopscotch is possible.

    :param tiles: The tiles on the board.
    :param k: The number of tiles.
    :return: Whether or not a game of hopscotch is possible.
    """

    # Loop through the tiles
    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            curr_tile = tiles[i][j]

            # If the current tile is the first tile
            if curr_tile == 1:
                # Loop through the tiles
                for i2 in range(len(tiles)):
                    for j2 in range(len(tiles[i2])):
                        curr_tile2 = tiles[i2][j2]

                        # If the current tile is the second tile
                        if curr_tile2 == 2:
                            # Loop through the tiles
                            for i3 in range(len(tiles)):
                                for j3 in range(len(tiles[i3])):
                                    curr_tile3 = tiles[i3][j3]

                                    # If the current tile is the third tile
                                    if curr_tile3 == 3:
                                        # Loop through the tiles
                                        for i4 in range(len(tiles)):
                                            for j4 in range(len(tiles[i4])):
                                                curr_tile4 = tiles[i4][j4]

                                                # If the current tile is the last tile
                                                if curr_tile4 == k:
                                                    # Return whether or not the game is possible
                                                    return (abs(i - i2) + abs(j - j2)) + (abs(i2 - i3) + abs(j2 - j3)) + (abs(i3 - i4) + abs(j3 - j4)) < k

    # Return that the game is not possible
    return False


def main():
    # Read the input
    n, k = [int(x) for x in input().split()]
    tiles = [[int(x) for x in input().split()] for i in range(n)]

    # Solve the problem
    ans = hopscotch(n, k, tiles)

    # Print the solution
    print(ans)


if __name__ == "__main__":
    main()
