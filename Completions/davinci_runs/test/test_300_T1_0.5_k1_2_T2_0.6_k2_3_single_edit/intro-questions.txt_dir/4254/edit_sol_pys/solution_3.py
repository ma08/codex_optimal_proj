#!/usr/bin/python3

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read the input from the user
    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__': # call main function
    main()
