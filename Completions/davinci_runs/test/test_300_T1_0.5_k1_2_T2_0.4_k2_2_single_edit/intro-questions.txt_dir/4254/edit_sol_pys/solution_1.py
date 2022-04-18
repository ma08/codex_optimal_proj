
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read in sheep and wolves

    if sheep < wolves: # check if sheep are less than wolves
        print("unsafe")
    else:
        print("safe") # print safe if not

if __name__ == '__main__': # call main
    main()
