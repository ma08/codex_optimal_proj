

import sys

def main():
    sheep, wolf = map(int, sys.stdin.readline().split()) # split() returns a list of strings after breaking the given string by the specified separator.
    if sheep < wolf: # if statement
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
