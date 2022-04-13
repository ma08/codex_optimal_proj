
import sys

def main():
    n = int(sys.stdin.readline())
    grid = []
    spy_coords = None
    for i in range(n):
        row = sys.stdin.readline().strip()
        grid.append(row)
        if "S" in row:
            spy_coords = (i, row.index("S"))

    spy_dist = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] == "H":
                spy_dist.append(abs(spy_coords[0] - row) + abs(spy_coords[1] - col))
    print(max(spy_dist))

if __name__ == "__main__":
    main()
