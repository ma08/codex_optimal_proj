

import sys

def main():
    num = int(sys.stdin.readline())
    grid = []
    spy_coord = []
    for i in range(num):
        row = sys.stdin.readline().strip()
        grid.append(row)
        if "S" in row:
            spy_coord.append((i, row.index("S")))

    for coords in spy_coord:
        spy_dist = []
        for row in range(num):
            for col in range(num):
                if grid[row][col] == "H":
                    spy_dist.append(abs(coords[0] - row) + abs(coords[1] - col))
        print(max(spy_dist))

if __name__ == "__main__":
    main()
