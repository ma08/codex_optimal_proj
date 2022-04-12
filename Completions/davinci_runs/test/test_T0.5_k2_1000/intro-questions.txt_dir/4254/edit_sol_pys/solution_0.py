
import sys

def main():
    sheep, wolf = map(int, sys.stdin.readline().split()) # read input
    if sheep < wolf: # if sheep < wolf, print "unsafe"
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()
