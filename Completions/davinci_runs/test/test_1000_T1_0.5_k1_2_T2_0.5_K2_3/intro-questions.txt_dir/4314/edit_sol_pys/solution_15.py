


import sys

def main():
    h, w = list(map(int, sys.stdin.readline().split()))
    grid = [list(sys.stdin.readline().split()[0]) for i in range(h)]
    for i in range(h):
        if grid[i].count('#') == 0:
            grid.pop(i)
            h -= 1
            i -= 1
    for i in range(w - 1, -1, -1):
        column = [grid[j][i] for j in range(h) if grid[j][i] == '#']
        if len(column) == 0:
            for j in range(h - 1, -1, -1):
                grid[j].pop(i)
            w -= 1
    for i in range(h):
        print(''.join(grid[i]))


if __name__ == '__main__':
    main()
