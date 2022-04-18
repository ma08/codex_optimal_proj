# fix spelling mistakes
import sys


def main():
    num = int(sys.stdin.readline())
    grid = []
    spy_coord = None
    for i in range(num):
        row = sys.stdin.readline().strip()
        grid.append(row)
        if "S" in row:
            spy_coord = (i, row.index("S"))

    spy_dist = []
    for row in range(num):
        for col in range(num):
            if grid[row][col] == "H":
                spy_dist.append(abs(spy_coord[0] - row) + abs(spy_coord[1] - col))
    print(max(spy_dist))


if __name__ == "__main__":
    main()
