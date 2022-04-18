

import sys
import math

def main():
    x = int(sys.stdin.readline().strip())
    k = 0
    while x > 1:
        k += 1
        x = x / 2
    print(k+1)

if __name__ == '__main__':
    main()
