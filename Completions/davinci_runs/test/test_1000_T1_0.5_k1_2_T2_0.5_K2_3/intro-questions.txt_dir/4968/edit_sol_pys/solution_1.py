

import sys
import math

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        x, y = [int(i) for i in sys.stdin.readline().split()]
        print(int(math.ceil(math.log(y/x, 2))))

if __name__ == "__main__":
    main()
