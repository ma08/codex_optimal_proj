

import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    grid = []
    for i in range(n):
        grid.append(sys.stdin.readline().strip())
    print(grid)

main()
