

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split()) # read line from stdin and split it into two integers

    if sheep < wolves: # if there are more wolves than sheep
        print("unsafe") # print "unsafe"
    else: # otherwise
        print("safe") # print "safe"

if __name__ == '__main__':
    main() # call main function
