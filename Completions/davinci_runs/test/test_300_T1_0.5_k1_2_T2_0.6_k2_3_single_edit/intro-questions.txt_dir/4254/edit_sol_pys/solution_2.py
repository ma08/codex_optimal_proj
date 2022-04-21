

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline())

    print("safe" if sheep > wolves else "unsafe")

if __name__ == '__main__':
    main()
