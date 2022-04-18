
import sys

def main(n, bricks):
    bricks = [int(x) for x in bricks.split()]
    towers = 1
    base = bricks[0]

    for brick in bricks[1:]:
        if brick > base:
            towers += 1
            base = brick

    return towers

if __name__ == '__main__':
    n = int(input())
    bricks = input()
    print(main(n, bricks))
