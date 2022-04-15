

import sys

def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    grid = []
    for i in range(n):
        grid.append(list(sys.stdin.readline().strip()))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                # Check if adjacent to a coffee shop
                if i > 0 and grid[i-1][j] == 'E':
                    grid[i][j] = 'E'
                elif i < n-1 and grid[i+1][j] == 'E':
                    grid[i][j] = 'E'
                elif j > 0 and grid[i][j-1] == 'E':
                    grid[i][j] = 'E'
                elif j < m-1 and grid[i][j+1] == 'E':
                    grid[i][j] = 'E'

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E':
                # Check if adjacent to another coffee shop
                if i > 0 and grid[i-1][j] == 'E':
                    grid[i][j] = '.'
                elif i < n-1 and grid[i+1][j] == 'E':
                    grid[i][j] = '.'
                elif j > 0 and grid[i][j-1] == 'E':
                    grid[i][j] = '.'
                elif j < m-1 and grid[i][j+1] == 'E':
                    grid[i][j] = '.'

    for i in range(n):
        for j in range(m):
            sys.stdout.write(grid[i][j])
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()