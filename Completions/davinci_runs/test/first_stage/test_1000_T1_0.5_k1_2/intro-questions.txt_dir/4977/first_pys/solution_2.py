

#!/usr/bin/env python3

import sys

def main():
    start = [int(i) for i in sys.stdin.readline().split()]
    end = [int(i) for i in sys.stdin.readline().split()]
    charge = int(sys.stdin.readline())
    if (charge - abs(end[0] - start[0]) - abs(end[1] - start[1])) % 2 == 0:
        print("Y")
    else:
        print("N")

if __name__ == "__main__":
    main()