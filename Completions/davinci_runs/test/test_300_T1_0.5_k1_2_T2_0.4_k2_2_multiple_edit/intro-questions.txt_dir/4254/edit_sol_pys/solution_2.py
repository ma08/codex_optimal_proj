
import sys


def main():
    sheep, wolf = map(int, sys.stdin.readline().split())  # read the input
    if sheep < wolf:  # if sheep is less than wolf
        print("unsafe")  # print unsafe
    else:  # if sheep is more than wolf
        print("safe")  # print safe


if __name__ == '__main__':
    main()
