import sys

def main():
    start = map(int, sys.stdin.readline().split())
    end = map(int, sys.stdin.readline().split())
    charge = int(sys.stdin.readline())

    if abs(start[0] - end[0]) + abs(start[1] - end[1]) == charge:
        print "Y"
    else:
        print "N"

if __name__ == "__main__":
    main()
