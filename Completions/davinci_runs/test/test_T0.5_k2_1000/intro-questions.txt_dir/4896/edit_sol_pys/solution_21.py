import sys

def main():
    num_bricks = int(sys.stdin.readline().strip()) # read in number of bricks
    bricks = [int(x) for x in sys.stdin.readline().strip().split()] # read in bricks

    min_width = bricks[0] # set minimum width to first brick
    num_towers = 1 # set number of towers to 1

    for brick in bricks[1:]:
        if brick > min_width: # if brick is larger than the minimum width
            num_towers += 1
            min_width = brick

    print(num_towers) # print number of towers

if __name__ == '__main__':
    main()
