
import sys

def main():
    sheeps, wolves = map(int, sys.stdin.readline().split()) # read two integers

    if sheeps < wolves:
        print("unsafe") # print unsafe if sheeps < wolves
    else:
        print("safe") # print safe if sheeps >= wolves

if __name__ == '__main__':
    main()
