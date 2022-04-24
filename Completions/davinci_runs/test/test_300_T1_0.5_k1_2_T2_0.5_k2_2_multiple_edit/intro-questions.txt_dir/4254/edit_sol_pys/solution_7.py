

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # Take input from the user.
    if sheep < wolves: # If sheep is less than wolves, print unsafe
        print("unsafe")
    else: # If not, print safe
        print("safe")

if __name__ == '__main__':
    main()
