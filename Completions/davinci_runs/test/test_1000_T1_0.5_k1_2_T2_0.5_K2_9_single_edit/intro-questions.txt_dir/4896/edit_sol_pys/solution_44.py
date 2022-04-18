
import sys


def main():
    n = int(sys.stdin.readline())
    bricks = list(map(int, sys.stdin.readline().split()))
    towers = []

    for brick in bricks:
        if len(towers) == 0:
            towers.append(brick)
            continue
        if brick > towers[-1]:
            towers.append(brick)
        else:
            for i in range(len(towers)):
                if brick < towers[i]:
                    towers[i] = brick
                    break
    print(len(towers))


if __name__ == '__main__':
    main()
