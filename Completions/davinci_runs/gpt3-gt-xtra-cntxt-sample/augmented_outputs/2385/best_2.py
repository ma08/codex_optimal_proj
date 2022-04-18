import sys

def max_robots(n, m, c, s):
    """
    Function to determine the maximum number of robots that can be placed
    in a grid of size n x m with colors c and directions s.

    The function also returns the maximum number of black cells that can be
    occupied by the robots before they start to move.
    """

    # The maximum number of robots that we can place is the minimum of n and m.
    max_robots = min(n, m)

    # The maximum number of black cells that we can occupy is the sum of the
    # first row and the first column.
    max_black_cells = sum(c[0]) + sum([c[i][0] for i in range(n)])

    return max_robots, max_black_cells

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    c = [list(map(int, list(sys.stdin.readline().strip()))) for i in range(n)]
    s = [list(sys.stdin.readline().strip()) for i in range(n)]
    max_robots, max_black_cells = max_robots(n, m, c, s)
    print("{} {}".format(max_robots, max_black_cells))