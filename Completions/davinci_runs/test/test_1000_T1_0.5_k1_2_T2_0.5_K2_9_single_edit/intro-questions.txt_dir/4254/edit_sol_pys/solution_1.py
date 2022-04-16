
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # sheep and wolves are integers
    if sheep < wolves: # if sheep are less than wolves
        print("unsafe") # print unsafe
    else: # else
        print("safe") # print safe

if __name__ == '__main__':
    main()
