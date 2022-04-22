

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read the sheep and wolves
    # check if the number of sheep is less than the wolves

    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
