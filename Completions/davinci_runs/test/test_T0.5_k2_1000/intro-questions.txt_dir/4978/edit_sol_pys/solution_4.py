import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    grid = [list(sys.stdin.readline().strip()) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'V': grid[i][j] = '.'
            if i < n - 1 and grid[i + 1][j] == '.': grid[i + 1][j] = 'V'
            if j > 0 and j < m - 1 and grid[i][j - 1] == '.' and grid[i][j + 1] == '.':
                grid[i][j - 1] = 'V'
                grid[i][j + 1] = 'V'
    for i in range(n): print("".join(grid[i]))

main()
