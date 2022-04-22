

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # split by space

    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == "__main__":
    main()
