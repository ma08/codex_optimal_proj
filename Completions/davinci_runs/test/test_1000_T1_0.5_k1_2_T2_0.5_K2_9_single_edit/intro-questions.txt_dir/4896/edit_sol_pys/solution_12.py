
import sys

def main():
    num_bricks = int(input())
    bricks = [int(x) for x in input().split()]

    min_width = bricks[0]
    num_towers = 1

    for brick in bricks[1:]:
        if brick > min_width:
            num_towers += 1
            min_width = brick

    print(num_towers)

if __name__ == '__main__':
    main()
