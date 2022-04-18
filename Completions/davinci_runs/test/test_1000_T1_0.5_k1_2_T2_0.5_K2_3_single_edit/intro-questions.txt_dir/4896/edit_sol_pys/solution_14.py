

from sys import stdin

def main():
    N = int(stdin.readline())
    bricks = [int(x) for x in stdin.readline().split()]

    towers = 1
    current_height = 0
    for brick in bricks[1:]:
        if brick > current_height:
            towers += 1
            current_height = brick
    print(towers)

if __name__ == '__main__':
    main()
