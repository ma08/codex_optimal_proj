
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read the first line

    if sheep < wolves:
        print("unsafe") # print unsafe if there are more wolves than sheep
    else:
        print("safe") # print safe if there are more sheep than wolves

if __name__ == '__main__':
    main()
