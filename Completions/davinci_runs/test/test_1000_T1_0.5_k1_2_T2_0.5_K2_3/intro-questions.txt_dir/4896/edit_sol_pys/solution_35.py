

import sys

def main():
    # read input
    n = int(sys.stdin.readline())
    bricks = [int(x) for x in sys.stdin.readline().split()] # read bricks
    assert(len(bricks) == n) # check input

    # count towers
    towers = 0 # initialize counter
    for i in range(n):
        if (i == 0) or (bricks[i] > bricks[i-1]): # check if i is the first brick or if brick i is greater than brick i-1
            towers += 1

    # print result
    print(towers)

if __name__ == '__main__':
    main()
