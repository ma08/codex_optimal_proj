

import sys
import math

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        print(int(math.floor(n/2)))

if __name__ == '__main__':
    main()