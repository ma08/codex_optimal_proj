
#
import sys

def main():
    n = int(input())
    bricks = [int(x) for x in input().split()]
    towers = 0
    base_level = 0

    for brick in bricks:
        if brick > base_level:
            towers += 1
            base_level = brick

    print(towers)

if __name__ == '__main__':
    main()
