

import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    grid = []
    for i in range(n):
        grid.append(sys.stdin.readline().strip())
    count = 0
    for j in range(m - 1):
        if grid[0][j] == '_' and grid[0][j + 1] == '_':
            count += 1 
    print(count)

main()
