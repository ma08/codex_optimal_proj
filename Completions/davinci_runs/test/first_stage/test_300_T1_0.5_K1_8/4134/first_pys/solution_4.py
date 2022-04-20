

def xor_paths(n, m, k, grid):
    """
    >>> xor_paths(3, 3, 11, [[2, 1, 5], [7, 10, 0], [12, 6, 4]])
    3
    >>> xor_paths(3, 4, 2, [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]])
    5
    >>> xor_paths(3, 4, 10**18, [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]])
    0
    """
    memo = {}
    def xor_paths_helper(i, j, xor_so_far):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == n - 1 and j == m - 1:
            if xor_so_far ^ grid[i][j] == k:
                memo[(i, j)] = 1
            else:
                memo[(i, j)] = 0
        else:
            if xor_so_far ^ grid[i][j] == k:
                memo[(i, j)] = 1
            else:
                memo[(i, j)] = 0
            if i < n - 1:
                memo[(i, j)] += xor_paths_helper(i + 1, j, xor_so_far ^ grid[i][j])
            if j < m - 1:
                memo[(i, j)] += xor_paths_helper(i, j + 1, xor_so_far ^ grid[i][j])
        return memo[(i, j)]
    return xor_paths_helper(0, 0, 0)

if __name__ == "__main__":
    n, m, k = [int(x) for x in input().split()]
    grid = []
    for i in range(n):
        grid.append([int(x) for x in input().split()])
    print(xor_paths(n, m, k, grid))