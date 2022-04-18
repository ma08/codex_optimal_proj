

import sys

def main():
    n, m = [int(j) for j in sys.stdin.readline().split()]
    grid = []
    for i in range(n):
        grid.append(sys.stdin.readline().strip())
    count = 0
    for i in range(n):
        if grid[i][0] == '_':
            count += 1
            while i < n and grid[i][0] == '_':
                i += 1
    print(count)

main()
