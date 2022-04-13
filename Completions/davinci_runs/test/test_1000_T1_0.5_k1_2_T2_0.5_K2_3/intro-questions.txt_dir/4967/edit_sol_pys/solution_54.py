
import math
import sys

    grid = []
def main():
    num = int(sys.stdin.readline())
    for i in range(num):
        row = sys.stdin.readline().strip()
        grid.append(row)

    spy_coords = None
    for i in range(num):
        for j in range(num):
            if grid[i][j] == "S":
                spy_coords = (i, j)
                break
        if spy_coords:
            break

    spy_dist = 0
    for i in range(num):
        for j in range(num):
            if grid[i][j] == "H":
                spy_dist = max(spy_dist, math.sqrt((spy_coords[0] - i)**2 + (spy_coords[1] - j)**2))
    print(spy_dist)


if __name__ == "__main__":
    main()
