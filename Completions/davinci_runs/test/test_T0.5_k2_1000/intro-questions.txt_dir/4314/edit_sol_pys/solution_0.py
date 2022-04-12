# https://atcoder.jp/contests/abc085/tasks/abc085_b

import sys

def main():
    h, w = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().split()[0]) for i in range(h)]
    for i in range(h):
        if grid[i].count('#') == 0:
            grid.pop(i)
            h -= 1
            i -= 1
    for i in range(w):
        column = [grid[j][i] for j in range(h)]
        if column.count('#') == 0:
            for j in range(h):
                grid[j].pop(i)
            w -= 1
            i -= 1
    for i in range(h):
        print(''.join(grid[i]))

if __name__ == '__main__':
    main()
