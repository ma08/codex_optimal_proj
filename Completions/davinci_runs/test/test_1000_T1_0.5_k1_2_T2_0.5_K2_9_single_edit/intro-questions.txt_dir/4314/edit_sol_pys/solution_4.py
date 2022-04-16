
import sys

def main():
    h, w = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().split()[0]) for i in range(h)]
    for i in range(h):
        if '#' not in grid[i]:
            grid.pop(i)
            h -= 1
            i -= 1
    for i in range(w):
        column = [grid[j][i] for j in range(h)]
        if '#' not in column:
            for j in range(h):
                grid[j].pop(i)
            w -= 1
            i -= 1
    for i in range(h):
        print(''.join(grid[i]))

if __name__ == '__main__':
    main()
