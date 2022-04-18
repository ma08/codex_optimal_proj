

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # map() is used to map a function to a list of parameters

    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
