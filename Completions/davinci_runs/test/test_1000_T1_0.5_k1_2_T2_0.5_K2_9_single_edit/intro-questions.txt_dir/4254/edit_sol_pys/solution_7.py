

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split())

    if sheep < wolves:
        print("unsafe") # This is a comment
    else:
        print("safe") # This is a comment

if __name__ == '__main__':
    main()
