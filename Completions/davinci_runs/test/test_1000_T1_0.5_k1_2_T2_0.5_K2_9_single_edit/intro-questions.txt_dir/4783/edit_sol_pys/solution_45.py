

def main():
    """
    Given a grid of heights, find the minimum length ladder needed to climb from
    (0,0) to (N,M)
    """
    m, n = map(int, input().split())
    grid = []
    for _ in range(m):
        grid.append(list(map(int, input().split())))
    print(min_ladder(grid, m, n))

def min_ladder(grid, m, n):
    """
    Find the minimum length ladder needed to climb from (0,0) to (N,M)
    """
    grid = [[0 for _ in range(n+2)] for _ in range(m+2)]
    grid[0] = [0]*(n+2)
    grid[-1] = [0]*(n+2)
    for i in range(1, m+1):
        grid[i] = [0] + grid[i] + [0] # add zeroes at the sides
    # print(grid)
    for i in range(1, m+1):
        for j in range(1, n+1):
            grid[i][j] = max(grid[i-1][j], grid[i][j-1], grid[i][j]) - grid[i][j] # add the difference
    # print(grid)
    return grid[-1][-1]

if __name__ == "__main__":
    main()
