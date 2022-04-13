
import sys

def main():
    num_bricks = int(sys.stdin.readline().strip()) # number of bricks
    bricks = [int(x) for x in sys.stdin.readline().strip().split()] # width of each brick

    min_width = bricks[0] # minimum width of a tower
    num_towers = 1 # number of towers

    for brick in bricks[1:]:
        if brick > min_width:
            num_towers += 1 # increase number of towers
            min_width = brick # set minimum width of tower

    print(num_towers)

if __name__ == '__main__':
    main()
