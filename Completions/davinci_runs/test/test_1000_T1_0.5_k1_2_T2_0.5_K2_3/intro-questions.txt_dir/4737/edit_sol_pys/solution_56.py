

import sys

def main():
    N, M, K = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(N):
        grid.append(list(map(int, sys.stdin.readline().split())))
    print(grid)

main()
