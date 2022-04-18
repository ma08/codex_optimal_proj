

#!/usr/bin/env python3

import sys

def main():
    start = [int(i) for i in sys.stdin.readline().split()]
    end = [int(i) for i in sys.stdin.readline().split()]
    charge = int(sys.stdin.readline())
    print("Y" if (charge - abs(end[0] - start[0]) - abs(end[1] - start[1])) % 2 == 0 else "N")

if __name__ == "__main__":
    main()
