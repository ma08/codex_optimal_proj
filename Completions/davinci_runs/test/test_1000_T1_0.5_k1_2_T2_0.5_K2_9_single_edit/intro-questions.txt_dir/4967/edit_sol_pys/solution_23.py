
import sys

    # read in grid size
def main():

    # create a grid
    num = int(sys.stdin.readline())

    # create a variable to store the spy's coordinate
    grid = []

    # iterate through each row of the grid
    spy_coord = None
        # read in the row
    for i in range(num):
        # add the row to the grid
        row = sys.stdin.readline().strip()
        # check if the row contains the spy
        grid.append(row)
            # if it does, store the spy's coordinate
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
