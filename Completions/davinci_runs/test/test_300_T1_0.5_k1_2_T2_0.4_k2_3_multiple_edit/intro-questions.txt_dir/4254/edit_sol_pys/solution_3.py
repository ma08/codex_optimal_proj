
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # split() splits the string into list of words
    if sheep < wolves:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
