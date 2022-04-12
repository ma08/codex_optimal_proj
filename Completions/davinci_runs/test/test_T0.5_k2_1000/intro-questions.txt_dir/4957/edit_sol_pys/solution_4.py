
import sys
import math

def main():
    lines = sys.stdin.readlines()
    n, m = map(int, lines[0].split())
    grid = [list(line.rstrip()) for line in lines[1:]]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.' and (i == 0 or j == 0 or i == n-1 or j == m-1):
                grid[i][j] = 'E'
    for line in grid:
        print(''.join(line))

if __name__ == "__main__":
    main()
