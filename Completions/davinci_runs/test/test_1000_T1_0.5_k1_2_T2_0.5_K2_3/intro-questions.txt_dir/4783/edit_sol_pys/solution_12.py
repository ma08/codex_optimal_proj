

def main():
    m, n = [int(x) for x in input().split()]
    grid = []
    for i in range(m):
        grid.append([int(x) for x in input().split()])
    # The idea is to use dynamic programming.
    # We start with the bottom right corner, and calculate the length of the ladder needed to reach it from the top left corner.
    # Then we move to the left, and calculate the length of the ladder needed to reach the bottom right corner from the top left corner
    # from that point. We also keep track of the maximum height of the coins we have to climb to get to the bottom right corner.
    # Then we move up, and do the same.
    # We create a 2D array to store the lengths of the ladders needed to get to each point.
    ladder_lengths = [[None for j in range(n)] for i in range(m)] 
    # We start with the bottom right corner.
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
