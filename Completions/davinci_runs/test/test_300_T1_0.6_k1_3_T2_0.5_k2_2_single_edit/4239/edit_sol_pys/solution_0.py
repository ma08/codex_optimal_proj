

import sys
import math

def main():
    n = int(sys.stdin.readline())
    count = 0
    while n != 0:
        if n % 6 == 0:
            n -= 6
        elif n % 9 == 0:
            n -= 9
        else:
            n -= 1
        count += 1
    sys.stdout.write(str(count) + '\n')

if __name__ == '__main__':
    main()
