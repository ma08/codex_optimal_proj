
import sys

def shortest_ladder(grid, m, n):
    """
    Returns the length of the shortest ladder that allows you to get from the north west corner to the south east corner.
    :param grid: a m x n list of lists of integers
    :param m: int
    :param n: int
    :return: int
    """
    # initialize ladder_length array
    # initialize the first row
    for j in range(n):
        ladder_length[0][j] = abs(grid[0][j] - grid[0][j - 1]) if j > 0 else 0
    ladder_length = [[0 for _ in range(n)] for _ in range(m)]
    # initialize the first column
    for i in range(m):
        ladder_length[i][0] = abs(grid[i][0] - grid[i - 1][0]) if i > 0 else 0
    # fill in the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            ladder_length[i][j] = max(abs(grid[i][j] - grid[i - 1][j]), abs(grid[i][j] - grid[i][j - 1]),
                                      ladder_length[i - 1][j], ladder_length[i][j - 1])
    return ladder_length[m - 1][n - 1]

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
