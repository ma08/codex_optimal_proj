
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read in the input

    if sheep < wolves: # if the number of sheep is less than the number of wolves, print unsafe
        print("unsafe")
    else: # otherwise, print safe
        print("safe")

if __name__ == '__main__': # call the main function
    main()
