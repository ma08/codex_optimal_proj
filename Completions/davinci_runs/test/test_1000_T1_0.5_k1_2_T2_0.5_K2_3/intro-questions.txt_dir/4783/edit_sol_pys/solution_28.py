

import sys

def shortest_ladder(grid, m, n):
    """
    Returns the length of the shortest ladder that allows you to get from the north west corner to the south east corner.
    :param grid: a m x n list of lists of integers
    :param m: int
    :param n: int
    :return: int
    """
    # initialize ladder_lengths matrix
    ladder_lengths = [[0 for _ in range(n)] for _ in range(m)]  # m rows, n columns; _ means throw away the variable
    # initialize the first column
    for i in range(m):
        ladder_lengths[i][0] = abs(grid[i][0] - grid[i - 1][0])
    # initialize the first row (can't use for i in range(m) because you will get an IndexError)
    for j in range(n):
        ladder_lengths[0][j] = abs(grid[0][j] - grid[0][j - 1])
    # fill in the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            ladder_lengths[i][j] = max(abs(grid[i][j] - grid[i - 1][j]), abs(grid[i][j] - grid[i][j - 1]), ladder_lengths[i - 1][j], ladder_lengths[i][j - 1])
    return ladder_lengths[m - 1][n - 1]

def main():
    # read input
    m, n = [int(x) for x in sys.stdin.readline().split()]
    grid = []
    for _ in range(m):
        grid.append([int(x) for x in sys.stdin.readline().split()])
    # print shortest ladder length
    print(shortest_ladder(grid, m, n))

if __name__ == '__main__':
    main()
