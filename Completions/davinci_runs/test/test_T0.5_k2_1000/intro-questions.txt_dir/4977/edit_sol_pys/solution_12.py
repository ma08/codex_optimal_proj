

import sys

def main():
    start = list(map(int, sys.stdin.readline().split())) #start position
    end = list(map(int, sys.stdin.readline().split())) #end position
    charge = int(sys.stdin.readline()) #charge

    if abs(start[0] - end[0]) + abs(start[1] - end[1]) == charge:
        print "Y" #Yes
    else:
        print "N" #No

if __name__ == "__main__":
    main()
