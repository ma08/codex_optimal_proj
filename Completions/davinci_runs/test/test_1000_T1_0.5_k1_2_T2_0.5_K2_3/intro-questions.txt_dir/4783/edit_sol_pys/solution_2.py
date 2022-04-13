

def main():
    m, n = [int(x) for x in input().split()]
    grid = []
    for i in range(m):
        grid.append([int(x) for x in input().split()])

    ladder_lengths = [[None for j in range(n)] for i in range(m)] 

    ladder_lengths[-1][-1] = 0
    max_height = 0
    # We move left.
    for i in range(n - 2, -1, -1):
        # We calculate the height of the coins we have to climb to get to the bottom right corner.
        max_height = max(max_height, grid[-1][i + 1])
        # We calculate the length of the ladder needed to get to the bottom right corner from the top left corner.
        ladder_lengths[-1][i] = max(0, max_height - grid[-1][i])
    # We move up.
    for i in range(m - 2, -1, -1):
        # We calculate the height of the coins we have to climb to get to the bottom right corner.
        max_height = max(max_height, grid[i + 1][-1])
        # We calculate the length of the ladder needed to get to the bottom right corner from the top left corner.
        ladder_lengths[i][-1] = max(0, max_height - grid[i][-1])
    # We move up and left.
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            # We calculate the height of the coins we have to climb to get to the bottom right corner.
            max_height = max(max_height, grid[i + 1][j], grid[i][j + 1])
            # We calculate the length of the ladder needed to get to the bottom right corner from the top left corner.
            ladder_lengths[i][j] = max(0, max_height - grid[i][j])
    # We print the result.
    print(ladder_lengths[0][0])

main()
