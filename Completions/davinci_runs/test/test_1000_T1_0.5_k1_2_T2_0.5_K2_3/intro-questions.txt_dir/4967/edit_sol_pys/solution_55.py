

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

    spy_dist = [0]
    for row in range(num):
        for col in range(num):
            if grid[row][col] == "H":
                for coord in spy_coord:
                    spy_dist.append(abs(coord[0] - row) + abs(coord[1] - col))
    print(max(spy_dist))

if __name__ == "__main__":
    main()
