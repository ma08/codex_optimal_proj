
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # split on whitespace

    if sheep < wolves:
        print("unsafe") # print string
    else:
        print("safe")

if __name__ == '__main__':
    main()
