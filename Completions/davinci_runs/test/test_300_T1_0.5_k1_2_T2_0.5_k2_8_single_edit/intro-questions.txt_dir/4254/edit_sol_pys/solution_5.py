

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # Reads a line from stdin and returns a list of words.

    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
