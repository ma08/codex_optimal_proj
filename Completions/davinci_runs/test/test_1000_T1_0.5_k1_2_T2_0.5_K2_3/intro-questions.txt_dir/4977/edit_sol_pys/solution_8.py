

import sys 

def main():
    start = list(map(int, sys.stdin.readline().split())) # read starting point
    end = list(map(int, sys.stdin.readline().split())) # read ending point
    charge = int(sys.stdin.readline()) # read battery charge 

    if abs(start[0] - end[0]) + abs(start[1] - end[1]) == charge: # if the distance is equal to the charge 
        print "Y"
    else:
        print "N"

if __name__ == "__main__":
    main()
