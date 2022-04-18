
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read in the input

    if sheep < wolves: # determine if safe or unsafe
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
