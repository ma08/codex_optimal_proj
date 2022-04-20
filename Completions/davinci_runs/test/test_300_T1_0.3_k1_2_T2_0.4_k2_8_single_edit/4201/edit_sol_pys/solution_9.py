

import sys

def main():
    h, w, k = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(h):
        grid.append(sys.stdin.readline().strip())
    count = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for r in range(h):
                for c in range(w):
                    if (i >> r) & 1 == 1 or (j >> c) & 1 == 1:
                        cnt += 1
                    if grid[r][c] == '#':
                        cnt += 1
            if cnt == k:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
