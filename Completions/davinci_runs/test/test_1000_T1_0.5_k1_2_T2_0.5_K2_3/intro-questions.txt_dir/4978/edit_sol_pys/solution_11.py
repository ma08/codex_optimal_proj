
# https://dmoj.ca/problem/ccc08s1
import sys

def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split()]
    grid = []
    for i in range(N):
        grid.append([x for x in sys.stdin.readline().strip()])
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'V':
                grid[i][j] = '.'
                if i < N - 1 and grid[i + 1][j] == '.':
                    grid[i + 1][j] = 'V'
                if j > 0 and j < M - 1 and grid[i][j - 1] == '.' and grid[i][j + 1] == '.':
                    grid[i][j - 1] = 'V'
                    grid[i][j + 1] = 'V'
    for i in range(N):
        print("".join(grid[i]))

main()
