
import sys

def main():
    num_rows = int(sys.stdin.readline().strip())
    bricks = [int(x) for x in sys.stdin.readline().strip().split()] # read in the bricks

    min_width = bricks[0] # min width of a tower
    num_towers = 1 # number of towers

    for brick in bricks[1:]:
        if brick > min_width: # if the brick is wider than the min width of a tower, then it becomes the new min width
            num_towers += 1
            min_width = brick

    print(num_towers)

if __name__ == '__main__':
    main()
