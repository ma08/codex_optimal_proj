
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split())  # read input

    if sheep < wolves:  # check if sheep are less than wolves
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
