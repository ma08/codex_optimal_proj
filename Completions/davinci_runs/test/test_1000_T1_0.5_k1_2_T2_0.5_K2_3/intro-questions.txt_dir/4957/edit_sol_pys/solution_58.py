import sys
import math

def main():
    lines = sys.stdin.readlines()
    n, m = map(int, lines[0].split())
    grid = [list(line.rstrip()) for line in lines[1:]]
    for i in range(n-1):
        for j in range(m-1):
            if grid[i][j] == 'E':
                grid[i][j] = 'E'
            else:
                if grid[i+1][j] == 'E' and grid[i][j+1] == 'E':
                    grid[i][j] = 'E'
                elif grid[i+1][j+1] == 'E' and grid[i][j+1] == 'E':
                    grid[i][j] = 'E'
                elif grid[i+1][j+1] == 'E' and grid[i+1][j] == 'E':
                    grid[i][j] = 'E'
                else:
                    grid[i][j] = '.'
    for i in range(n-1):
        print(''.join(grid[i]) + '.')
    print(''.join(grid[n-1]))

if __name__ == "__main__":
    main()
