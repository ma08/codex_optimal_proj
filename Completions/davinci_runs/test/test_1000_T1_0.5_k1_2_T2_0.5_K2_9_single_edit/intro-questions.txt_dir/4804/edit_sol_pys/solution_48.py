

import math
import sys

def main():
    s = int(sys.stdin.readline())
    print(s, ":")
    for i in range(2, int(math.sqrt(s))+1):
        if s % i == 0:
            print(i, int(s/i))

if __name__ == "__main__":
    main()
