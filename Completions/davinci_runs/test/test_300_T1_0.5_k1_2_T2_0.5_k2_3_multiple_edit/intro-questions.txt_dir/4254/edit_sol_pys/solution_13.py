

import sys

def main():
    sheep, wolf = map(int, sys.stdin.readline().split()) # read the first line of stdin
    if sheep < wolf: # check if the number of sheep is less than the number of wolves
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
