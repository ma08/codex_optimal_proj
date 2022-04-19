

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read input

    if sheep < wolves: # if sheep are less then wolves
        print("unsafe") # print unsafe
    else:
        print("safe")

if __name__ == '__main__':
    main()
